from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

class TestBurger:

    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = Bun("black bun", 100.0)
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] is ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "one", 1.0)
        ingredient2 = Ingredient("FILLING", "two", 2.0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] is ingredient2

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Ingredient("SAUCE", "one", 1.0)
        ingredient2 = Ingredient("FILLING", "two", 2.0)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] is ingredient2
        assert burger.ingredients[1] is ingredient1

    def test_get_price(self):
        burger = Burger()
        bun = Bun("black bun", 100.0)
        ingredient1 = Ingredient("SAUCE", "hot sauce", 50.0)
        ingredient2 = Ingredient("FILLING", "cutlet", 100.0)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert burger.get_price() == 350.0

    def test_get_receipt(self):
        burger = Burger()
        bun = Bun("black bun", 100.0)
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert "black bun" in receipt
        assert "hot sauce" in receipt
        assert "Price: 250.0" in receipt