# Python image to use.
FROM python:3.10-alpine

# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]


# # Expose port 5000
 EXPOSE 5000
 ENV PORT 5000
# WORKDIR /app

# Start the app using gunicorn and gevent workers
CMD exec gunicorn --bind :$PORT --workers ${NUM_WORKERS:-1} --worker-class gevent --worker-connections 1000 --timeout 30 app:app


# #Use gunicorn as the entrypoint
# CMD exec gunicorn --bind :$PORT main:app --workers 1 --threads 1 --timeout 0

# # default run without gunicorn
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]