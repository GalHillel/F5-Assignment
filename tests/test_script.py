import requests
import sys
import time
import urllib3

# suppress warnings about self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# config
success_url = "http://nginx:8080"
error_url = "http://nginx:8081"
https_url = "https://nginx:443"

def run_tests():
    print("starting tests")
    
    # test 1: basic http at 8080
    try:
        print(f"testing {success_url}")
        response = requests.get(success_url, timeout=5)
        if response.status_code != 200 or "Success!" not in response.text:
            print(f"http 8080 check failed. status: {response.status_code}")
            return False
        print("http 8080 endpoint works.")
    except Exception as e:
        print(f"connection error to http 8080: {e}")
        return False

    # test 2: error endpoint st 8081
    try:
        print(f"testing {error_url}")
        response = requests.get(error_url, timeout=5)
        if response.status_code != 500:
            print(f"expected 500, got {response.status_code}")
            return False
        print("error endpoint works (returned 500).")
    except Exception as e:
        print(f"connection error to error endpoint: {e}")
        return False

    # test 3: https support at 443
    try:
        print(f"testing {https_url} (ssl)")
        # verify=False is needed for self-signed certificates
        response = requests.get(https_url, timeout=5, verify=False)
        if response.status_code != 200 or "Success!" not in response.text:
            print(f"https check failed. status: {response.status_code}")
            return False
        print("https endpoint works.")
    except Exception as e:
        print(f"connection error to https: {e}")
        return False

    # test 4: rate limiting 5 r/s
    try:
        print("testing rate limiting")
        blocked = False
        # send 20 requests rapidly
        for i in range(20):
            response = requests.get(success_url, timeout=2)
            if response.status_code == 503:
                blocked = True
                print(f"request {i+1} was blocked (503) as expected.")
                break
        
        if blocked:
            print("rate limiting is active and blocking requests.")
        else:
            print("sent 20 requests fast but none were blocked. rate limit failed.")
            return False

    except Exception as e:
        print(f"error during rate limit test: {e}")
        return False

    return True

if __name__ == "__main__":
    if run_tests():
        print("\nall tests passed successfully!")
        sys.exit(0)
    else:
        print("\nsome tests failed.")
        sys.exit(1)