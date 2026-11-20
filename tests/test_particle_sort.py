import pytest
from render import particle_sort as mod

CASES = [
    ("sort", 'm.sort_key(3.2, 5) == (-3.2, 5)'),
    ("soft", 'm.soft_weight(0.5, 2) == approx(0.75)'),
    ("child", 'm.child_velocity((1, 2), (3, 4), 0.5) == approx((3.5, 5.0))'),
    ("pool", 'm.pool_reset((1, 2, 3)) == (0.0, 0.0, 0.0)'),
    ("pause", 'm.paused_dt(0.016, True) == 0.0'),
    ("alpha", 'm.alpha_test(0.5, 0.5) is True'),
    ("degrade", 'm.degrade_mode(0) == "alpha_test"'),
    ("swap", 'm.swap_buffers("a", "b") == ("b", "a")'),
    ("depth", 'm.depth_key(1.23456789) == approx(1.234568)'),
    ("alive", 'm.count_alive([True, False, True]) == 2'),
    ("barrier", 'm.emit_barrier("emit", "sort") is True'),
    ("world", 'm.world_velocity((1, 2), 3) == (3, 6)'),
    ("life", 'm.particle_lifetime(2, 2) is False'),
    ("recon", 'm.soft_reconstruct(2, 1, 2) == approx(0.5)'),
    ("id", 'm.particle_id(7, 3) == "7:3"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
