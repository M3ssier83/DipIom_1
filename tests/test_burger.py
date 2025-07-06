import allure
from stellar_burger_app.burger import Burger

class TestBurger:

    @allure.title("Проверка установки булки")
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, "Булка не установлена корректно методом set_buns()"

    @allure.title("Проверка добавления ингредиента")
    def test_add_ingredient(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients, "Ингредиент не добавлен в список методом add_ingredient()"

    @allure.title("Проверка удаления ингредиента")
    def test_remove_ingredient(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "Ингредиент не был удалён методом remove_ingredient()"

    @allure.title("Проверка перемещения ингредиента")
    def test_move_ingredient(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[0] == mock_ingredient, "Метод move_ingredient() не переместил ингредиент на нужную позицию"

    @allure.title("Проверка расчёта цены")
    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.price * 2 + mock_ingredient.price
        actual_price = burger.get_price()
        assert actual_price == expected_price, f"Метод get_price() должен вернуть {expected_price}, но вернул {actual_price}"

    @allure.title("Проверка получения чека")
    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        assert mock_bun.name in receipt, "Название булки не найдено в чеке, метод get_receipt() работает некорректно"
        assert mock_ingredient.name in receipt, "Название ингредиента не найдено в чеке, метод get_receipt() работает некорректно"
