# Object Detection System

This project demonstrates an object detection system using a pre-trained Faster R-CNN model with PyTorch, deployed via a Streamlit web application. The project dependencies are managed using Poetry, and the application is containerized using Docker.

![Application Screenshot](screenshots/screenshot.png)

## Requirements

- Python 3.9
- Poetry
- Docker

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/confused-pandas/object-detection-system.git
    cd object-detection-system
    ```

2. **Install Poetry:**

    Follow the instructions at [Poetry Installation](https://python-poetry.org/docs/#installation) to install Poetry.

3. **Install dependencies:**

    ```sh
    poetry install
    ```

## Running the Application

### Using Poetry

1. **Activate the virtual environment:**

    ```sh
    poetry shell
    ```

2. **Run the Streamlit app:**

    ```sh
    streamlit run src/app/app.py
    ```

    Open a web browser and go to `http://localhost:8501` to access the application.

### Using Docker

1. **Build the Docker image:**

    ```sh
    docker build -t object-detection-system .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -p 8501:8501 object-detection-system
    ```

    Open a web browser and go to `http://localhost:8501` to access the application.

## Usage

1. **Upload an image:**

    Click on "Choose an image..." and upload a JPG image.

2. **View the results:**

    The uploaded image will be displayed with detected objects highlighted by bounding boxes.

## Project Details

- The object detection models used are `fasterrcnn_resnet50_fpn` and `fasterrcnn_mobilenet_v3_large_fpn` from `torchvision`.
- The detection threshold can be adjusted.
- Detected objects are highlighted with bounding boxes in the output image.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyTorch](https://pytorch.org/)
- [Streamlit](https://streamlit.io/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)