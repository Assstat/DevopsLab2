from main import sum_fn
def test_sum_fn():
    assert sum_fn(2,2)==4
    assert sum_fn(0,-1)==-1
    assert sum_fn(100,-100)==0