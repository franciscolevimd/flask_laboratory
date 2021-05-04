FROM python:3.9-alpine

# Set the working directory in the Docker container
WORKDIR /usr/src/flask_laboratory

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the working directory
COPY . .

# Run the container.
CMD [ "python", "app/main.py" ]
