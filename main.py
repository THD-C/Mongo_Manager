from concurrent import futures
import grpc
from grpc_health.v1 import health, health_pb2, health_pb2_grpc
from grpc_reflection.v1alpha import reflection
import secret.secret_pb2_grpc as secret_pb2_grpc
import secret.secret_pb2 as secret_pb2
import password.password_pb2_grpc as password_pb2_grpc
import password.password_pb2 as password_pb2
import currency.currency_pb2_grpc as currency_pb2_grpc
import currency.currency_pb2 as currency_pb2
import blog.blog_pb2_grpc as blog_pb2_grpc
import blog.blog_pb2 as blog_pb2

from opentelemetry.instrumentation.grpc import GrpcInstrumentorServer
from py_grpc_prometheus.prometheus_server_interceptor import PromServerInterceptor
from prometheus_client import start_http_server

import src.Service as Service
import src.Utils.OpenTelemetry.OpenTelemetry as oTEL
from src.config import SERVICE_NAME


def main() -> None:
    GrpcInstrumentorServer().instrument()
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=[PromServerInterceptor(enable_handling_time_histogram=True)],
    )
    secret_pb2_grpc.add_SecretStoreServicer_to_server(Service.SecretStore(), server)
    password_pb2_grpc.add_PasswordCheckerServicer_to_server(
        Service.PasswordChecker(), server
    )
    currency_pb2_grpc.add_CurrencyServicer_to_server(Service.Currency(), server)
    blog_pb2_grpc.add_BlogServiceServicer_to_server(Service.BlogService(), server)

    health_servicer = health.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)
    health_servicer.set(SERVICE_NAME, health_pb2.HealthCheckResponse.SERVING)

    # Enable reflection
    SERVICE_NAMES = (
        secret_pb2.DESCRIPTOR.services_by_name["SecretStore"].full_name,
        password_pb2.DESCRIPTOR.services_by_name["PasswordChecker"].full_name,
        currency_pb2.DESCRIPTOR.services_by_name["Currency"].full_name,
        blog_pb2.DESCRIPTOR.services_by_name["Blog"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    start_http_server(8111)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
