import pytest

class TestFirstCls:

    def inc(self,x):
        return x + 1

    def f(self):
        raise SystemExit(1)

    def test_answer(self):
        assert self.inc(3) == 5

    def test_mytest(self):
        with pytest.raises(SystemExit):
            self.f()

    def test_one(self):
        x="hello"
        assert "l" in x

