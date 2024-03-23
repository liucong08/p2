# File_name: demo
# Date: 2024-03-20
import pytest

def test_demo():
    with pytest.assume:assert 1 == 2
    print(456)
    with pytest.assume:assert 2 == 3
    print(123)

if __name__ == '__main__':
    pytest.main([__file__, '-sv'])