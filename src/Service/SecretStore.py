from secret.secret_pb2_grpc import SecretStoreServicer
from secret.secret_pb2 import SecretName, SecretValue

from src.Mongo.SecretCollection import SecretCollection


class SecretStore(SecretStoreServicer):

    def GetSecret(self, request: SecretName, context):
        try:
            return SecretValue(value=SecretCollection.get_secret(request.name))
        except Exception as e:
            print(e)
            return SecretValue(value="")
