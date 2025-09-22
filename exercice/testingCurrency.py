import pytest
from exercice.currency import CurrencyConverter

@pytest.fixture
def converter():
        return CurrencyConverter()

def test_convert_usd_to_eur(converter):
    assert converter.convert('USD', 'EUR', 100) == 92.0

def test_convert_eur_to_usd(converter):
    assert converter.convert('EUR', 'USD', 92) == 100.0
def test_convert_gbp_to_jpy(converter):
    assert converter.convert('GBP', 'JPY', 82) == 15025.0
def test_convert_jpy_to_inr(converter):
    assert converter.convert('JPY', 'INR', 15025) == 8312.0