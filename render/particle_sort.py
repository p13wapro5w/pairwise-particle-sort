import math

def sort_key(depth, index):
    """稳定深度排序键。"""
    raise NotImplementedError("TODO: sort_key")

def soft_weight(delta, radius):
    """软粒子权重。"""
    raise NotImplementedError("TODO: soft_weight")

def child_velocity(parent, own, factor):
    """子发射器继承。"""
    raise NotImplementedError("TODO: child_velocity")

def pool_reset(velocity):
    """池复用清零。"""
    raise NotImplementedError("TODO: pool_reset")

def paused_dt(dt, paused):
    """暂停冻结 dt。"""
    raise NotImplementedError("TODO: paused_dt")

def alpha_test(alpha, cutoff):
    """alpha 测试。"""
    raise NotImplementedError("TODO: alpha_test")

def degrade_mode(quality):
    """降级模式。"""
    raise NotImplementedError("TODO: degrade_mode")

def swap_buffers(active, next_buffer):
    """双缓冲交换。"""
    raise NotImplementedError("TODO: swap_buffers")

def depth_key(z):
    """深度量化。"""
    raise NotImplementedError("TODO: depth_key")

def count_alive(flags):
    """存活计数。"""
    raise NotImplementedError("TODO: count_alive")

def emit_barrier(producer, consumer):
    """emit 与 sort 屏障。"""
    raise NotImplementedError("TODO: emit_barrier")

def world_velocity(velocity, scale):
    """世界速度。"""
    raise NotImplementedError("TODO: world_velocity")

def particle_lifetime(age, max_age):
    """生命周期。"""
    raise NotImplementedError("TODO: particle_lifetime")

def soft_reconstruct(depth, scene_depth, softness):
    """深度重建软衰减。"""
    raise NotImplementedError("TODO: soft_reconstruct")

def particle_id(seed, index):
    """粒子 id。"""
    raise NotImplementedError("TODO: particle_id")
