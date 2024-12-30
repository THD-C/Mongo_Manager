import src.Service as Service
from currency.currency_type_pb2 import CurrencyType
from currency.currency_pb2 import CurrencyDetails, CurrencyTypeMsg, CurrencyList


def test_get_currency_type_usd_upper_success():
    s = Service.Currency()

    currency_type: CurrencyTypeMsg = s.GetCurrencyType(
        CurrencyDetails(currency_name="USD"),
        None,
    )
    assert currency_type.type == CurrencyType.CURRENCY_TYPE_FIAT


def test_get_currency_type_usd_lower_success():
    s = Service.Currency()

    currency_type: CurrencyTypeMsg = s.GetCurrencyType(
        CurrencyDetails(currency_name="usd"),
        None,
    )
    assert currency_type.type == CurrencyType.CURRENCY_TYPE_FIAT


def test_get_currency_type_failure():
    s = Service.Currency()

    currency_type: CurrencyTypeMsg = s.GetCurrencyType(
        CurrencyDetails(currency_name="fwqewfe"),
        None,
    )
    assert currency_type.type == CurrencyType.CURRENCY_TYPE_NOT_SUPPORTED


def test_get_currency_type_tether_upper_success():
    s = Service.Currency()

    currency_type: CurrencyTypeMsg = s.GetCurrencyType(
        CurrencyDetails(currency_name="TETHER"),
        None,
    )
    assert currency_type.type == CurrencyType.CURRENCY_TYPE_CRYPTO


def test_get_currency_type_tether_lower_success():
    s = Service.Currency()

    currency_type: CurrencyTypeMsg = s.GetCurrencyType(
        CurrencyDetails(currency_name="tether"),
        None,
    )
    assert currency_type.type == CurrencyType.CURRENCY_TYPE_CRYPTO


def test_get_supported_currencies_fiat_success():
    s = Service.Currency()

    currency_list: CurrencyList = s.GetSupportedCurrencies(
        CurrencyTypeMsg(type=CurrencyType.CURRENCY_TYPE_FIAT),
        None,
    )
    assert len(currency_list.currencies) == 46
    assert "usd" in [c.currency_name for c in currency_list.currencies]
    assert "eur" in [c.currency_name for c in currency_list.currencies]
    assert "pln" in [c.currency_name for c in currency_list.currencies]


def test_get_supported_currencies_crypto_success():
    s = Service.Currency()

    currency_list: CurrencyList = s.GetSupportedCurrencies(
        CurrencyTypeMsg(type=CurrencyType.CURRENCY_TYPE_CRYPTO),
        None,
    )
    assert len(currency_list.currencies) == 7
    assert "bitcoin" in [c.currency_name for c in currency_list.currencies]
    assert "ethereum" in [c.currency_name for c in currency_list.currencies]
    assert "tether" in [c.currency_name for c in currency_list.currencies]


def test_get_supported_currencies_failure():
    s = Service.Currency()

    currency_list: CurrencyList = s.GetSupportedCurrencies(
        CurrencyTypeMsg(type=12),
        None,
    )
    assert len(currency_list.currencies) == 0
