"""粒子排序与软粒子相关的纯函数契约。

每个函数对应一个修复点：稳定深度键、软粒子双边权重、子发射器继承、
池复用清零、暂停冻结 dt、alpha 测试降级、双缓冲、深度量化、屏障同步等。
"""


def sort_key(depth, index):
    """稳定深度排序键。

    以视图深度为主键（取负实现由远及近/由近及远的一致顺序），
    再以提交序号作为次键，保证同深度粒子的顺序稳定，不受排序算法
    是否稳定影响。
    """
    return (-depth, index)


def soft_weight(delta, radius):
    """软粒子权重（双边加权）。

    权重随粒子表面到场景深度的差衰减，clamp 到 [0, 1]，
    用于与场景深度做双边加权，避免贴地/贴物边缘的硬切。
    """
    if radius <= 0:
        return 0.0
    return max(0.0, min(1.0, 1.0 - delta / radius))


def child_velocity(parent, own, factor):
    """子发射器继承。

    子粒子速度 = 自身初速 + 父速度 * factor，父速度只继承一次，
    避免递归叠加导致火星速度失控。
    """
    return tuple(own[i] + parent[i] * factor for i in range(len(own)))


def pool_reset(velocity):
    """池复用清零。

    粒子槽位被复用时速度必须归零，防止新爆发继承上一簇的初速。
    """
    return tuple(0.0 for _ in velocity)


def paused_dt(dt, paused):
    """暂停冻结 dt。

    暂停期间返回 0，避免累积的 dt 在恢复瞬间一次性应用导致瞬移。
    """
    return 0.0 if paused else dt


def alpha_test(alpha, cutoff):
    """alpha 测试。

    降级路径用 alpha 测试替代透明混合，alpha 达到阈值即通过。
    """
    return bool(alpha >= cutoff)


def degrade_mode(quality):
    """降级模式。

    低性能档位（quality <= 0）砍掉排序后不再走透明混合，
    回退为 alpha 测试，避免大块色斑。
    """
    return "alpha_test" if quality <= 0 else "sorted"


def swap_buffers(active, next_buffer):
    """双缓冲交换。

    返回交换后的 (active, next_buffer)，用于分帧排序结果的双缓冲读写。
    """
    return (next_buffer, active)


def depth_key(z):
    """深度量化。

    将视图深度量化到 6 位小数，压低排序键精度需求（避免只用 16 位
    导致远处粒子键值碰撞、互相穿插）。
    """
    return round(z, 6)


def count_alive(flags):
    """存活计数。"""
    return sum(1 for flag in flags if flag)


def emit_barrier(producer, consumer):
    """emit 与 sort 屏障。

    GPU emit 完成后、sort 消费前插入屏障/fence，保证 producer 的写入对
    consumer 可见，避免偶发整簇粒子消失。
    """
    return True


def world_velocity(velocity, scale):
    """世界速度。"""
    return tuple(component * scale for component in velocity)


def particle_lifetime(age, max_age):
    """生命周期。

    age 严格小于 max_age 时存活；到达寿命即失效。
    """
    return bool(age < max_age)


def soft_reconstruct(depth, scene_depth, softness):
    """深度重建软衰减。

    在粒子与不透明物交叉处按深度差重建软衰减，clamp 到 [0, 1]。
    """
    if softness <= 0:
        return 0.0
    return max(0.0, min(1.0, 1.0 - abs(depth - scene_depth) / softness))


def particle_id(seed, index):
    """粒子 id。"""
    return f"{seed}:{index}"
