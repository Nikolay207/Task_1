from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_ingredient_init(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 50.0)
        assert ingredient.get_type() == "SAUCE"
        assert ingredient.get_name() == "hot sauce"
        assert ingredient.get_price() == 50.0