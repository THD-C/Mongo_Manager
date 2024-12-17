import src.Service as Service
from secret.secret_pb2 import SecretName


def test_secret_store_1_success():
    s = Service.SecretStore()
    msg = SecretName(name="test_token")

    resp = s.GetSecret(msg, None)

    assert resp.value == "AlaMaKota"


def test_secret_store_2_success():
    s = Service.SecretStore()
    msg = SecretName(name="test_token2")

    resp = s.GetSecret(msg, None)

    assert resp.value == "KotMaAle"


def test_secret_store_failure():
    s = Service.SecretStore()
    msg = SecretName(name="NOT_EXISTING_TOKEN")

    reps = s.GetSecret(msg, None)

    assert reps.value == ""
