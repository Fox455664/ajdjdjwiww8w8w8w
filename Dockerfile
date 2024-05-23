FROM nikolaik/python-nodejs:python3.9-nodejs17

# Add the new GPG key for Yarn repository
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -

# Install ffmpeg and clean up in one layer to reduce image size
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the application files to the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install the Python dependencies
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

# Command to run the application
CMD ["python3", "main.py"]
