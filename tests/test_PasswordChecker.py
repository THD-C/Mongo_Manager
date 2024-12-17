import src.Service as Service
from password.password_pb2 import PasswordMessage


def test_password_checker_weak_1_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="password")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is True


def test_password_checker_weak_2_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="abcd123")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is True


def test_password_checker_weak_3_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="ewusia")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is True


def test_password_checker_strong_1_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="whyfbui34i43rif9k2j9")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is False


def test_password_checker_strong_2_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="wefufiub3i4u903ofwekjnv")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is False


def test_password_checker_strong_success():
    s = Service.PasswordChecker()
    msg = PasswordMessage(password="liepoinoiuve9e37kjbw")
    resp = s.CheckPassword(msg, None)
    assert resp.isCommon is False
