from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_ingredient_get_type(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        assert ingredient.get_type() == "SAUCE"

    def test_ingredient_get_name(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        assert ingredient.get_name() == "hot sauce"

    def test_ingredient_get_price(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        assert ingredient.get_price() == 50.0