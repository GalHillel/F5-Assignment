import requests
import sys

# config
# using nginx as hostname because docker compose resolves it automatically
nginx_host = "nginx"
success_url = f"http://{nginx_host}:8080"
error_url = f"http://{nginx_host}:8081"

def run_tests():
    print("starting connectivity tests...")
    
    # test 1: check success endpoint at 8080
    try:
        print(f"testing {success_url}...")
        response = requests.get(success_url, timeout=5)
        
        # check status 200
        if response.status_code != 200:
            print(f"[fail] expected status 200, got {response.status_code}")
            return False
            
        # check content
        if "Success!" not in response.text:
            print("[fail] response content did not contain expected text")
            return False
            
        print("[pass] success endpoint works as expected.")
        
    except Exception as e:
        print(f"[fail] connection error to success endpoint: {e}")
        return False

    # test 2: check error endpoint at 8081
    try:
        print(f"testing {error_url}...")
        response = requests.get(error_url, timeout=5)
        
        # check status 500
        if response.status_code != 500:
            print(f"[fail] expected status 500, got {response.status_code}")
            return False
            
        print("[pass] error endpoint works as expected (returned 500).")
        
    except Exception as e:
        print(f"[fail] connection error to error endpoint: {e}")
        return False

    return True

if __name__ == "__main__":
    if run_tests():
        print("\nall tests passed successfully!")
        sys.exit(0)
    else:
        print("\nsome tests failed.")
        sys.exit(1)