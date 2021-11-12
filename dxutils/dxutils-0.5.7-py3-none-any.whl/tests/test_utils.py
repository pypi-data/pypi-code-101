from dxutils import utils

def test_polyprint():
    assert utils.polyprint([1,-2,3.141592,4,5]) == '1 x^{4} -2 x^{3} +3.1416 x^{2} +4 x +5'
