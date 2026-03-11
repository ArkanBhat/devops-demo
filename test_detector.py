# test_detector.py
from detector import check_url

def test_phishing_url():
    assert check_url("http://secure-login-verify.com") == "PHISHING"

def test_safe_url():
    assert check_url("http://google.com") == "SAFE"
