from unittest.mock import Mock

from praktikum.database import Database

class TestDatabase:

    def test_database_init(self):
        database = Database()
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[5].get_name() == "sausage"

    def test_database_with_mock(self):
        database = Database()
        mock_method = Mock()
        mock_method.return_value = ["mocked_bun"]
        database.available_buns = mock_method
        result = database.available_buns()
        assert result == ["mocked_bun"]