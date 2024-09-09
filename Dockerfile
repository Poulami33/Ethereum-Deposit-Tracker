# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir web3 python-telegram-bot

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV ALCHEMY_URL=https://eth-mainnet.alchemyapi.io/v2/Dl9GcOc1Y-AzEiWZF42-ZHe3GlzbBZbJ
ENV BOT_TOKEN=7331501704:AAHlKQSwSZGiT8LpdhsVKW5StLuFmAgDFlM
ENV CHAT_ID=1123861818

# Run app.py when the container launches
CMD ["python", "ether.py"]