from src.Mongo.connection import client, DATABASE_NAME


class SecretCollection:

    __collection = "Secrets"

    @staticmethod
    def get_secret(secret_name: str) -> str:
        projection = {secret_name: 1}
        data: dict = (
            client.get_database(DATABASE_NAME)
            .get_collection(SecretCollection.__collection)
            .find_one({}, projection)
        )
        return str(data.get(secret_name, ""))
