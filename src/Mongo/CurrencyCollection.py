from src.Mongo.connection import client, DATABASE_NAME


class CurrencyCollection:

    __collection = "Currency"
    __currency_name_field = "currency_name"
    __currency_type_field = "currency_type"

    @staticmethod
    def get_currency_type(currency: str) -> int:
        data: dict = (
            client.get_database(DATABASE_NAME)
            .get_collection(CurrencyCollection.__collection)
            .find_one({CurrencyCollection.__currency_name_field: currency})
        )
        return data.get(CurrencyCollection.__currency_type_field, None)

    @staticmethod
    def get_currency_list(currency_type: int) -> list[str]:
        data: list[dict] = (
            client.get_database(DATABASE_NAME)
            .get_collection(CurrencyCollection.__collection)
            .find({CurrencyCollection.__currency_type_field: currency_type})
        )
        return [d.get(CurrencyCollection.__currency_name_field) for d in data]
