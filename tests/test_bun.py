import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun", ""])
    def test_bun_get_name(self, name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [100.0, 200, 300.5, 0])
    def test_bun_get_price(self, price):
        bun = Bun("black bun", price)
        assert bun.get_price() == price