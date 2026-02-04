import requests
import sys

# Configuration
# Note: We use "nginx" as the hostname because Docker Compose will resolve this name 
# to the Nginx container's IP address automatically.
NGINX_HOST = "nginx"
SUCCESS_URL = f"http://{NGINX_HOST}:8080"
ERROR_URL = f"http://{NGINX_HOST}:8081"

def run_tests():
    print("Starting connectivity tests...")
    
    # --- Test 1: Check Success Endpoint (Port 8080) ---
    try:
        print(f"Testing {SUCCESS_URL}...")
        response = requests.get(SUCCESS_URL, timeout=5)
        
        # Verify status code is 200
        if response.status_code != 200:
            print(f"[FAIL] Expected status 200, got {response.status_code}")
            return False
            
        # Verify content matches what we expect
        if "Success!" not in response.text:
            print("[FAIL] Response content did not contain expected text")
            return False
            
        print("[PASS] Success endpoint works as expected.")
        
    except Exception as e:
        print(f"[FAIL] Connection error to success endpoint: {e}")
        return False

    # --- Test 2: Check Error Endpoint (Port 8081) ---
    try:
        print(f"Testing {ERROR_URL}...")
        response = requests.get(ERROR_URL, timeout=5)
        
        # Verify status code is an error (we configured 500)
        if response.status_code != 500:
            print(f"[FAIL] Expected status 500, got {response.status_code}")
            return False
            
        print("[PASS] Error endpoint works as expected (returned 500).")
        
    except Exception as e:
        print(f"[FAIL] Connection error to error endpoint: {e}")
        return False

    return True

if __name__ == "__main__":
    if run_tests():
        print("\nAll tests passed successfully!")
        sys.exit(0) # Success exit code
    else:
        print("\nSome tests failed.")
        sys.exit(1) # Failure exit code (Crucial for CI/CD)