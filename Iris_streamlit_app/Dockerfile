# Base image of python 3.8
FROM python:3.8

# Setup the working directory
WORKDIR /app

# Copy files fromj the current directory to the working directory
COPY . /app

# Install all the dependencies for the app
RUN pip install -r requirements.txt

# Expose port 8080 of the container for listening
EXPOSE 8080

# The command to launch streamlit app and expose it's port 8080, when container is up and running
CMD streamlit run app.py --server.port=8080
