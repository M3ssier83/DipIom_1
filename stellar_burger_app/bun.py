import allure

class Bun:
    """
    Модель булочки для бургера.
    Булочке можно дать название и назначить цену.
    """

    @allure.step("Создаём булочку: {name} за {price}")
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @allure.step("Получаем название булочки")
    def get_name(self) -> str:
        return self.name

    @allure.step("Получаем цену булочки")
    def get_price(self) -> float:
        return self.price