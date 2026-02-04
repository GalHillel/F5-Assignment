# use a lightweight python image
FROM python:3.9-slim

# set the working directory
WORKDIR /app

# install the requests library for http calls
RUN pip install requests --no-cache-dir

# copy the test script into the container
COPY test_script.py .

# run the script
CMD ["python", "test_script.py"]