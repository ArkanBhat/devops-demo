# detector.py
def check_url(url):
    suspicious_keywords = ["login", "verify", "secure", "account", "update"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            return "PHISHING"
    return "SAFE"

if __name__ == "__main__":
    test_urls = [
        "http://secure-login-verify.com/account",
        "http://google.com",
        "http://update-your-account.net"
    ]
    for url in test_urls:
        print(f"{url} --> {check_url(url)}")