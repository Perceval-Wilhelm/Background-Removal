# Background Removal

This repository contains a FastAPI application for image segmentation using YOLOv8, as well as a Streamlit frontend for easy interaction. The API takes an image as input and returns a segmented image with the background removed.

## Demo
https://github.com/user-attachments/assets/70c14382-d957-48f7-bc5d-c0653dab0a5a

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [Using Postman for Testing](#using-postman-for-testing)
- [Running the Server in a tmux Session](#running-the-server-in-a-tmux-session)
- [Docker Deployment](#docker-deployment)
- [Project Structure](#project-structure)
- [Additional Information](#additional-information)

## Prerequisites

- Python 3.8.19 or higher
- Conda
- FastAPI
- YOLOv8 Model (`yolov8m-seg.pt`)
- Postman (for testing)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Perceval-Wilhelm/Background-Removal.git
    cd Background-Removal
    ```

2. **Create and activate the Conda environment:**

    ```bash
    conda create --name background-removal python=3.8.19
    conda activate background-removal
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    pip install -r requirements_pytorch.txt
    ```

4. **Download the YOLOv8 model:**

    - Place the `yolov8m-seg.pt` model file in the `model` directory.

5. **Directory structure:**

    Ensure your directory structure looks like this:

    ```plaintext
    Background-Removal/
    ├── input/
    │   ├── bus.png
    │   └── cars.png
    ├── model/
    │   └── yolov8m-seg.pt
    ├── output/
    │   ├── bus_output.png
    │   └── cars_output.png
    ├── postman_collection/
    │   └── Background Removal.postman_collection.json
    ├── tests/
    │   └── test_segmentation.py
    ├── app.py
    ├── main.py
    ├── README.md
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    ├── requirements_pytorch.txt
    └── segmentation.py
    ```

## Running the Server

1. **Activate the Conda environment:**

    ```bash
    conda activate background-removal
    ```

2. **Run the FastAPI server:**

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

3. **Run the Streamlit app:**

    ```bash
    streamlit run app.py
    ```

4. **Access the applications:**

    - **FastAPI documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
    - **Streamlit app:** [http://localhost:8501](http://localhost:8501)

## Using Postman for Testing

1. **Open Postman.**

2. **Import the Postman collection:**
    - Click on `Import` in the top-left corner of Postman.
    - Select the exported JSON file of the Postman collection.
    - Click on `Import`.

3. **Create a new request in Postman:**
    - Go to the `Collections` tab.
    - Expand the `Background Removal` collection.
    - Select `Segment Image` request.

4. **Set up the request:**
    - Set the request type to `POST`.
    - Set the URL to:
      ```
      http://localhost:8000/segment
      ```

5. **Set the headers:**
    - Go to the `Headers` tab.
    - Add a new header:
      ```
      Key: Content-Type
      Value: multipart/form-data
      ```

6. **Set the body:**
    - Go to the `Body` tab.
    - Select `form-data`.
    - Add two fields:
        - **Field 1:**
          ```
          Key: challenge
          Type: Text
          Value: cv3
          ```
        - **Field 2:**
          ```
          Key: file
          Type: File
          Value: [Choose File button] (Select an image file)
          ```

7. **Choose the file to upload:**
    - Click on the `Choose Files` button next to the `file` field.
    - Select an image file from your computer (e.g., `sample_image.png`).

8. **Send the request:**
    - Click the `Send` button.

9. **Verify the response:**
    - If the request is successful, you should see a JSON response like this:
      ```json
      {
          "message": "succeed",
          "segmented_image_path": "/output/sample_image_output.png"
      }
      ```

## Running the Server in a tmux Session

1. **Start a new `tmux` session:**

    ```bash
    tmux new -s background-removal
    ```

2. **Navigate to your project directory:**

    ```bash
    cd /path/to/deployment/
    ```

3. **Activate the Conda environment:**

    ```bash
    conda activate background-removal
    ```

4. **Run the FastAPI server:**

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

5. **Detach from the `tmux` session:**
    - Press `Ctrl + b`, then release both keys and press `d`.

6. **Reattach to your `tmux` session later:**

    ```bash
    tmux attach -t background-removal
    ```

## Docker Deployment

### Building the Docker Image

To build the Docker image, run the following command in the project directory:

```bash
docker build -t background-removal-app .
```

### Pulling the Docker Image

To use the pre-built Docker image from Docker Hub, run the following command:

```bash
docker pull percevalwilhelm/background-removal-app
```

### Running the Docker Container

To run the Docker container, use the following command:

```bash
docker run -p 8000:8000 -p 8501:8501 percevalwilhelm/background-removal-app
```

### Accessing the Applications

- **FastAPI documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Streamlit app:** [http://localhost:8501](http://localhost:8501)

## Project Structure

- **main.py**: Entry point of the FastAPI application.
- **segmentation.py**: Contains the segmentation logic using YOLOv8.
- **model/**: Directory to store the YOLOv8 model.
- **tests/**: Contains test scripts and sample images for testing.
- **requirements.txt**: Contains the list of dependencies.
- **requirements_pytorch.txt**: Contains the list of PyTorch dependencies.
- **README.md**: Project documentation.
- **app.py**: Streamlit app for front-end.
- **postman/**: JSON file for testing on Postman.

## Additional Information

- Ensure the YOLOv8 model (`yolov8m-seg.pt`) is downloaded and placed in the `model` directory.
- For any issues or questions, please open an issue on the repository or contact the maintainer.
