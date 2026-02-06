# DevOps Intern – Home Assignment

This repository contains a containerized Nginx server configuration and a Python-based test suite, orchestrated using Docker Compose. The project demonstrates infrastructure-as-code, automated testing, and CI/CD practices.

## How to Run
### Prerequisites
* Docker & Docker Compose installed on your machine.

### Execution
Run the following command to build the images and start the services:
```bash
docker compose up --build
```

Expected Output
The test runner will validate the following endpoints and behaviors:

* Port 8080: Returns a custom HTML success page (HTTP 200).
* Port 8081: Returns an HTTP error response (HTTP 500).
* Port 443 (HTTPS): Validates secure connection using a self-signed certificate.
* Rate Limiting: Validates that excessive requests (over 5/sec) are blocked with HTTP 503.

If all tests pass, the test-runner container will exit with code 0.

## Project Structure
* **docker-compose.yml**: Orchestrates the Nginx and Test services on a shared network.
* **nginx/**:
  * **Dockerfile**: Ubuntu-based image installing Nginx and OpenSSL.
  * **nginx.conf**: Configuration for HTTP/HTTPS servers and Rate Limiting.
  * **index.html**: Custom success page.
  * **ssl/**: Contains the self-signed certificate (nginx.crt) and key (nginx.key).
* **tests/**:
  * **Dockerfile**: Lightweight Python (3.9-slim) image.
  * **test_script.py**: Script using the requests library to validate status codes, content, SSL, and rate limiting.
* **.github/workflows/**: CI pipeline configuration.

### HTTPS Support
The server handles secure traffic on port 443 using self-signed certificates generated during the build process. The tests are configured to verify SSL connectivity.

### Rate Limiting Configuration
The server limits requests to 5 requests per second.

**How it works:** The configuration uses Nginx's limit_req_zone directive. It tracks request rates based on the client's IP address.

**How to change the threshold:**

1. Open nginx/nginx.conf.
2. Locate line 5:
```
limit_req_zone $binary_remote_addr zone=one:10m rate=5r/s;
```
3. Change 5r/s to your desired rate (e.g., 10r/s).

## Design Decisions & Trade-offs
* **Base Image:** The Nginx image is based on ubuntu:24.04 to follow the assignment requirements.

* **Test Script:** Python was chosen for the test script due to its simplicity and the readability of the requests library.
* **Implementation:** Used python:3.9-slim to minimize the test container footprint.

* **SSL Certificates:** Used pre generated key&crt to minimize image size

## GitHub Repository & CI
A GitHub Actions workflow is configured to automatically build and test the project on every push to the main branch.

* **Success:** If tests pass, an artifact named succeeded is uploaded.
* **Failure:** If tests fail, an artifact named fail is uploaded.
