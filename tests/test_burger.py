import allure
from stellar_burger_app.burger import Burger
from data import MOCK_BUN, MOCK_INGREDIENT

class TestBurger:

    @allure.title("Проверка установки булки")
    def test_set_buns(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        assert burger.bun == MOCK_BUN, "Булка не установлена корректно методом set_buns()"

    @allure.title("Проверка добавления ингредиента")
    def test_add_ingredient(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        burger.add_ingredient(MOCK_INGREDIENT)
        assert MOCK_INGREDIENT in burger.ingredients, "Ингредиент не добавлен в список методом add_ingredient()"

    @allure.title("Проверка удаления ингредиента")
    def test_remove_ingredient(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        burger.add_ingredient(MOCK_INGREDIENT)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "Ингредиент не был удалён методом remove_ingredient()"

    @allure.title("Проверка перемещения ингредиента")
    def test_move_ingredient(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        burger.add_ingredient(MOCK_INGREDIENT)
        burger.move_ingredient(0, 0)
        assert burger.ingredients[
                   0] == MOCK_INGREDIENT, "Метод move_ingredient() не переместил ингредиент на нужную позицию"

    @allure.title("Проверка расчёта цены")
    def test_get_price(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        burger.add_ingredient(MOCK_INGREDIENT)
        expected_price = MOCK_BUN.price * 2 + MOCK_INGREDIENT.price
        actual_price = burger.get_price()
        assert actual_price == expected_price, f"Метод get_price() должен вернуть {expected_price}, но вернул {actual_price}"

    @allure.title("Проверка получения чека")
    def test_get_receipt(self):
        burger = Burger()
        burger.set_buns(MOCK_BUN)
        burger.add_ingredient(MOCK_INGREDIENT)

        expected_receipt = (
            f"(==== {MOCK_BUN.name} ====)\n"
            f"= {MOCK_INGREDIENT.get_type().lower()} {MOCK_INGREDIENT.name} =\n"
            f"(==== {MOCK_BUN.name} ====)\n\n"
            f"Price: {MOCK_BUN.price * 2 + MOCK_INGREDIENT.price}"
        )

        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt, (
            f"Чек сформирован некорректно.\n"
            f"Ожидалось:\n{expected_receipt}\n"
            f"Получено:\n{actual_receipt}"
        )
