import pytest
from data import MOCK_BUN, MOCK_INGREDIENT

@pytest.fixture
def mock_bun():
    return MOCK_BUN

@pytest.fixture
def mock_ingredient():
    return MOCK_INGREDIENT
