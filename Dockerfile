# Use an official Python runtime as a parent image
FROM python:3.8.19-slim

# Set work directory
WORKDIR /wham-selenium-gpt/

# Copy requirements.txt early to cache dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /wham-selenium-gpt


ENTRYPOINT [ "python3", "main.py" ]