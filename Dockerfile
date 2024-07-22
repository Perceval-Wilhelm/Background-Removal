# Use an official Python runtime as a parent image
FROM python:3.8.19

# Set the working directory in the container
WORKDIR /app

# Copy the requirements files into the container
COPY requirements.txt .

# Install any needed packages specified in requirements files
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Copy the model files into the container
COPY model /app/model

# Install additional dependencies for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Expose the port for FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Run both FastAPI and Streamlit applications
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.enableCORS false"]
