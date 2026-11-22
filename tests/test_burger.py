from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_burger_get_price_empty_ingredients(self):
        burger = Burger()
        bun = Bun("black bun", 100.0)
        burger.set_buns(bun)
        assert burger.get_price() == 200.0

    def test_burger_add_ingredient(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100.0))
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 250.0

    def test_burger_remove_ingredient(self):
        burger = Burger()
        burger.set_buns(Bun("black bun", 100.0))
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.get_price() == 200.0