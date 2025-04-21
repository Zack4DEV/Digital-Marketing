# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory to /app
WORKDIR /app

# Copy the directory containing the application into the container at /app
COPY assets/ /app/assets/
COPY migrations/ /app/migrations/
COPY pages/ /app/pages/
COPY utils/ /app/utils/

COPY *.py /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# (Not needed since this application does not use a network port, but left for reference)
# EXPOSE 80

# Define environment variables
ENV DB_URI=
ENV MENDABLE_API_KEY=${MENDABLE_API_KEY}

# Make sure the directory for SQLite database exists
RUN mkdir /app/data

# Set up a directory for the SQLite database
VOLUME /app/data

# Run streamlit_app.py when the container launches
CMD ["python", "streamlit_app.py"]
