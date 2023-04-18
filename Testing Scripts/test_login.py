import pytest
import sys
@pytest.mark.xfail(sys.platform == "win64", reason="Can't work on windows 64 bit")
def test_login():
    print("Login Success!")
@pytest.mark.skipif(sys.version_info < (4,3),reason="requires python4.3")
def test_logout():
    print("Logout Success!")