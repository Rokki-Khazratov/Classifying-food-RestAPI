# AI Image Classification API

This Django REST API allows you to perform image classification using a pre-trained AI model and provides a user-friendly endpoint to upload and classify images. The AI model is based on a Fastai deep learning framework, and it is capable of classifying various fruits, vegetables, and fast food items.

## AI Model Source : https://github.com/Meliyev




## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Rokki-Khazratov/classifyingfood-RestAPI.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip/pip3 install -r requirements.txt
    ```

## Usage

### Running the Django Server

1. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

2. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

The server will be accessible at `http://127.0.0.1:8000/`.

### API Endpoints

#### 1. Image List and Create

- **Endpoint:** `/images/`
- **Methods:** GET, POST
- **Description:** Retrieve a list of images or create a new image entry.

#### 2. Image Retrieve, Update, and Destroy

- **Endpoint:** `/images/<int:pk>`
- **Methods:** GET, PUT, PATCH, DELETE
- **Description:** Retrieve, update, or delete a specific image by its primary key.

#### 3. Image Classification API

- **Endpoint:** `/send/`
- **Method:** POST
- **Description:** Upload an image for classification.

    ##### Example Request:

    - **Method:** POST
    - **URL:** `http://127.0.0.1:8000/api/send/`
    - **Body:** Form-data or any other method to send the image as binary data.

    ##### Example Response:

    ```json
    {
        "id": 35,
        "name": "Strawberry",
        "image": "http://127.0.0.1:8000/storage/images/Screenshot_2024-03-05_at_7.33.05PM_jyl0APi.png",
        "probability": "99.06%"
    }
    ```

## Model Information

The AI model is based on Fastai and has been trained to classify various fruits, vegetables, and fast food items. It provides predictions with associated probabilities.

## Troubleshooting

If you encounter any issues or errors, please check the following:

- Ensure that all dependencies are installed using `requirements.txt`.
- Make sure the server is running and accessible at the specified address.
- Verify that the AI model file (`food_class.pkl`) is located in the `materials/` directory.

For further assistance, feel free to contact the repository owner.

## Contributing

If you'd like to contribute to the project, please follow the standard GitHub fork and pull request workflow. Contributions are welcome!

## License

This project is licensed under the [MIT License](LICENSE).
