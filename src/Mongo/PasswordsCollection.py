from src.Mongo.connection import client, DATABASE_NAME


class PasswordCollection:

    __collection = "CommonPasswords"

    @staticmethod
    def is_password_common(password: str) -> bool:
        data = (
            client.get_database(DATABASE_NAME)
            .get_collection(PasswordCollection.__collection)
            .find_one({"$or": [{"cert_pl": password}]})
        )
        return data is not None
