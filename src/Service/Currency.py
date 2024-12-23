from currency.currency_pb2_grpc import CurrencyServicer
from currency.currency_type_pb2 import CurrencyType
from currency.currency_pb2 import CurrencyDetails, CurrencyTypeMsg, CurrencyList

from src.Mongo.CurrencyCollection import CurrencyCollection


class Currency(CurrencyServicer):
    def GetCurrencyType(self, request: CurrencyDetails, context):
        currency_type: int = CurrencyCollection.get_currency_type(request.currency_name)
        if currency_type is None:
            return CurrencyTypeMsg(type=CurrencyType.CURRENCY_TYPE_NOT_SUPPORTED)
        return CurrencyTypeMsg(type=currency_type)

    def GetSupportedCurrencies(self, request: CurrencyTypeMsg, context):
        currency_list: list[str] = CurrencyCollection.get_currency_list(request.type)
        return CurrencyList(
            currencies=[CurrencyDetails(currency_name=c) for c in currency_list]
        )
