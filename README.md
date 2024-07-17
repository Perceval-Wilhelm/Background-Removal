# Image Segmentation API (week1_test2)

This repository contains a FastAPI application for image segmentation using YOLOv8. The API takes an image as input and returns a segmented image with the background removed.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [Using Postman for Testing](#using-postman-for-testing)
- [Running the Server in a tmux Session](#running-the-server-in-a-tmux-session)
- [Project Structure](#project-structure)

## Prerequisites

- Python 3.8.19 or higher
- Conda
- FastAPI
- YOLOv8 Model (`yolov8m-seg.pt`)
- Postman (for testing)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://gitlab.com/sirrtt/week1_test2.git
    cd week1_test2
    ```

2. **Create and activate the Conda environment:**

    ```bash
    conda create --name image-segmentation-api python=3.8.19
    conda activate image-segmentation-api
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
    image_segmentation_api/
    ├── input/
    |   ├── bus.png
    │   └── cars.png
    ├── model/
    │   └── yolov8m-seg.pt
    ├── output/
    |   ├── bus_output.png
    │   └── cars_output.png
    ├── postman_collection
    │   └── Image Segmentation API.postman_collection.json
    ├── tests/
    │   └── test_segmentation.py
    ├── app.py
    ├── main.py
    ├── README.md
    ├── requirements.txt
    ├── requirements_pytorch.txt
    └── segmentation.py
    ```

## Running the Server

1. **Activate the Conda environment:**

    ```bash
    conda activate image-segmentation-api
    ```

2. **Run the FastAPI server:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

3. **Access the FastAPI documentation:**

    Open your web browser and navigate to:

    ```
    http://localhost:8000/docs
    ```

## Using Postman for Testing

1. **Open Postman.**

2. **Import the Postman collection:**
    - Click on `Import` in the top-left corner of Postman.
    - Select the exported JSON file of the Postman collection.
    - Click on `Import`.

3. **Create a new request in Postman:**
    - Go to the `Collections` tab.
    - Expand the `Image Segmentation API` collection.
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
    tmux new -s image-segmentation
    ```

2. **Navigate to your project directory:**

    ```bash
    cd /path/to/deployment/
    ```

3. **Activate the Conda environment:**

    ```bash
    conda activate image-segmentation-api
    ```

4. **Run the FastAPI server:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

5. **Detach from the `tmux` session:**
    - Press `Ctrl + b`, then release both keys and press `d`.

6. **Reattach to your `tmux` session later:**

    ```bash
    tmux attach -t image-segmentation
    ```

## Project Structure

- **main.py**: Entry point of the FastAPI application.
- **segmentation.py**: Contains the segmentation logic using YOLOv8.
- **model/**: Directory to store the YOLOv8 model.
- **tests/**: Contains test scripts and sample images for testing.
- **requirements.txt**: Contains the list of dependencies.
- **requirements_pytorch.txt**: Contains the list of PyTorch dependencies.
- **README.md**: Project documentation.
- **app.py**: Streamlit app for front-end (if applicable).
- **postman/**: JSON file for testing on Postman

## Additional Information

- Ensure the YOLOv8 model (`yolov8m-seg.pt`) is downloaded and placed in the `model` directory.
- For any issues or questions, please open an issue on the repository or contact the maintainer.
