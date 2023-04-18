import pytest
import sys
@pytest.mark.xfail(sys.platform == "win64", reason="Can't work on windows 64 bit")
def test_login(param_setup):
    print("Login Success!")
@pytest.mark.skipif(sys.version_info < (3,3),reason="requires python4.3")
def test_logout():
    print("Logout Success!")

@pytest.mark.parametrize("a,b,sum",[(2,3,5),(2,3,8)])
def test_sum(a,b,sum):
    assert a+b==sum