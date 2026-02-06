# DevOps Intern – Home Assignment

## Project Structure
The project consists of the following files and directories:

- **docker-compose.yml**: This file defines the services, networks, and volumes for the application. It builds and runs the Nginx and test containers.
- **nginx/**: This directory contains the Dockerfile and configuration files for the Nginx server.
  - **Dockerfile**: The Dockerfile for building the Nginx image based on Ubuntu. It installs and configures Nginx with two server blocks.
  - **nginx.conf**: The Nginx configuration file that sets up the server blocks.
  - **index.html**: A custom HTML response for one of the server blocks.
  - **ssl/**: Directory for SSL certificates.
- **tests/**: This directory contains the Dockerfile and the test script.
  - **Dockerfile**: The Dockerfile for building the test image that runs the test script.
  - **test_script.py**: A Python script that sends HTTP requests to the Nginx servers and verifies their responses.

## How to Build and Run the Project
1. **Build the Docker Images and Run the Containers**:
   ```bash
   docker compose up --build
   ```

2. **Check Test Results**: The test script will exit with a non-zero code if any tests fail.

## GitHub Repository & CI
- A GitHub Actions workflow set up to build the Docker images and run the tests. Based on the test results, it will decide to push or not.

## Advanced Requirements
- Implement HTTPS support for the Nginx server using a self-signed certificate.
- Add rate limiting to the Nginx server, limiting requests to 5 requests per second.
- Extend the test script to validate the rate limiting behavior.
- Document the rate limiting configuration, including how it works and how to change the threshold.
