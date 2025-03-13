# Use an official Python runtime based on Alpine as a parent image
FROM python:3.9-alpine

# Create a group and user
RUN addgroup -g 1000 appuser && \
    adduser -u 1000 -G appuser -D appuser

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py requirements.txt /app/

#Change ownership of the files.
RUN chown -R appuser:appuser /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set user
USER appuser

# Run the application
CMD ["python", "main.py"]