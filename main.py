from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection
import secret.secret_pb2_grpc as secret_pb2_grpc
import secret.secret_pb2 as secret_pb2

import src.Service as Service


def main() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    secret_pb2_grpc.add_SecretStoreServicer_to_server(Service.SecretStore(), server)

    # Enable reflection
    SERVICE_NAMES = (
        secret_pb2.DESCRIPTOR.services_by_name["SecretStore"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
