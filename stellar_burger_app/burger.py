from typing import List
import allure
from .bun import Bun
from .ingredient import Ingredient

class Burger:
    @allure.step("Создаём новый бургер")
    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    @allure.step("Устанавливаем булку")
    def set_buns(self, bun: Bun):
        self.bun = bun
        allure.attach(f"Булка: {bun.get_name()}", name="Булка")

    @allure.step("Добавляем ингредиент")
    def add_ingredient(self, ingredient: Ingredient):
        allure.attach(f"Ингредиент: {ingredient.get_name()}", name="Ингредиент")
        self.ingredients.append(ingredient)

    @allure.step("Удаляем ингредиент по индексу: {index}")
    def remove_ingredient(self, index: int):
        del self.ingredients[index]

    @allure.step("Перемещаем ингредиент с позиции {index} на позицию {new_index}")
    def move_ingredient(self, index: int, new_index: int):
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    @allure.step("Вычисляем цену бургера")
    def get_price(self) -> float:
        price = self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    @allure.step("Генерируем чек")
    def get_receipt(self) -> str:
        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']
        for ingredient in self.ingredients:
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')
        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price()}')
        return '\n'.join(receipt)
