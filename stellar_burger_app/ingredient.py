import allure

class Ingredient:
    """
    Модель ингредиента.
    Ингредиент: начинка или соус.
    У ингредиента есть тип (начинка или соус), название и цена.
    """

    @allure.step("Создаём ингредиент: {ingredient_type} {name} за {price}")
    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    @allure.step("Получаем цену ингредиента")
    def get_price(self) -> float:
        return self.price

    @allure.step("Получаем название ингредиента")
    def get_name(self) -> str:
        return self.name

    @allure.step("Получаем тип ингредиента")
    def get_type(self) -> str:
        return self.type