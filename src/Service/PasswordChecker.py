from password.password_pb2_grpc import PasswordCheckerServicer
from password.password_pb2 import CheckResponse, PasswordMessage

from src.Mongo.PasswordsCollection import PasswordCollection


class PasswordChecker(PasswordCheckerServicer):
    def CheckPassword(self, request: PasswordMessage, context):
        password = request.password
        is_common = PasswordCollection.is_password_common(password)
        return CheckResponse(isCommon=is_common)
