# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the bot script and install dependencies
COPY bot.py /app/bot.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Run the bot
CMD ["python3", "bot.py"]
