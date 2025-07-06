import pytest
import allure
from stellar_burger_app.bun import Bun
from data import available_buns

class TestBun:

    @allure.title("Проверка метода get_name() у Bun")
    @pytest.mark.parametrize("name, price", available_buns)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name, f"Метод get_name() должен вернуть '{name}', но вернул '{bun.get_name()}'"

    @allure.title("Проверка метода get_price() у Bun")
    @pytest.mark.parametrize("name, price", available_buns)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price, f"Метод get_price() должен вернуть {price}, но вернул {bun.get_price()}"
