class MockBun:
    def __init__(self):
        self.name = "black bun"
        self.price = 100

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class MockIngredient:
    def __init__(self):
        self.name = "hot sauce"
        self.price = 100
        self.type = "sauce"

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type


class MockIngredient2:
    def __init__(self):
        self.name = "cutlet"
        self.price = 200
        self.type = "filling"

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type


MOCK_BUN = MockBun()
MOCK_INGREDIENT = MockIngredient()
MOCK_INGREDIENT2 = MockIngredient2()
MOCK_TWO_INGREDIENTS = [MOCK_INGREDIENT, MOCK_INGREDIENT2]

# Для параметризации тестов булок
available_buns = [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
]


# Для параметризации тестов ингредиентов
available_ingredients = [
    ("sauce", "hot sauce", 100),
    ("sauce", "sour cream", 200),
    ("sauce", "chili sauce", 300),
    ("filling", "cutlet", 100),
    ("filling", "dinosaur", 200),
    ("filling", "sausage", 300)
]


