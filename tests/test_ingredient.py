import pytest
import allure
from stellar_burger_app.ingredient import Ingredient
from data import available_ingredients

class TestIngredient:

    @allure.title("Проверка метода get_name() у Ingredient")
    @pytest.mark.parametrize("ingredient_type, name, price", available_ingredients)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, f"Метод get_name() должен вернуть '{name}', но вернул '{ingredient.get_name()}'"

    @allure.title("Проверка метода get_price() у Ingredient")
    @pytest.mark.parametrize("ingredient_type, name, price", available_ingredients)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, f"Метод get_price() должен вернуть {price}, но вернул {ingredient.get_price()}"

    @allure.title("Проверка метода get_type() у Ingredient")
    @pytest.mark.parametrize("ingredient_type, name, price", available_ingredients)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Метод get_type() должен вернуть '{ingredient_type}', но вернул '{ingredient.get_type()}'"
