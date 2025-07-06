import allure
from stellar_burger_app.database import Database

class TestDatabase:

    @allure.title("Проверка получения списка доступных булочек")
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list), "Метод available_buns() должен возвращать список"
        assert all(hasattr(bun, "get_name") for bun in buns), "Все булки должны иметь метод get_name()"

    @allure.title("Проверка получения списка доступных ингредиентов")
    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list), "Метод available_ingredients() должен возвращать список"
        assert all(hasattr(ing, "get_name") for ing in ingredients), "Все ингредиенты должны иметь метод get_name()"
