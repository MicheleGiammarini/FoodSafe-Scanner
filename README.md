# FoodSafe Scanner

FoodSafe Scanner is a Flask-based web application that allows users to scan food product barcodes and receive detailed information about the product, including a list of ingredients and their potential health risks. It uses the Open Food Facts API to fetch product data and compares ingredients against a predefined list of risky ingredients.

## Features

- **Scan Barcode**: Scan a product's barcode to retrieve basic information about the product.
- **Analyze Ingredients**: Analyze the ingredients of the product against a predefined list of risky ingredients and receive detailed health risk information.
- **Risk Assessment**: The application identifies ingredients that could pose health risks (e.g., carcinogens, allergens, and other harmful substances).

## Prerequisites

- Python 3.x
- `pip` (Python package manager)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MicheleGiammarini/FoodSafe-Scanner.git
    cd FoodSafe-Scanner
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python main.py
    ```

    The server will start and listen on `http://0.0.0.0:5000`.

## Endpoints

### 1. **Scan Product by Barcode**

- **URL**: `/scan`
- **Method**: `POST`
- **Request**:
    - `barcode`: A string representing the product barcode.
  
    Example request body:
    ```json
    {
        "barcode": "1234567890123"
    }
    ```

- **Response**:
    Returns basic product details including product name, ingredients, and nutritional information.

    Example response:
    ```json
    {
        "product_name": "Example Product",
        "ingredients": ["ingredient1", "ingredient2"],
        "nutritional_info": {
            "energy": "100kcal",
            "fat": "5g",
            "sugar": "2g"
        }
    }
    ```

### 2. **Analyze Product Ingredients for Risks**

- **URL**: `/analyze`
- **Method**: `POST`
- **Request**:
    - `barcode`: A string representing the product barcode.

    Example request body:
    ```json
    {
    "barcode": "737628064502"
    }
    ```

- **Response**:
    Returns product details along with a list of ingredients and any identified health risks.

    Example response:
    ```json
    {
        "product_name": "Example Product",
        "ingredients": ["ingredient1", "ingredient2"],
        "risks": [
            {
                "ingredient": "ingredient1",
                "risk": "Potential carcinogen linked to liver and kidney damage."
            }
        ]
    }
    ```

## Risky Ingredients List

This application includes a predefined list of risky ingredients and their associated health risks:

- **Aspartame**: May cause allergic reactions and has potential brain effects.
- **BHA**: Potential carcinogen linked to liver and kidney damage.
- **BHT**: Potential carcinogen that can alter metabolism.
- **Acrylamide**: Classified as a carcinogen, linked to increased cancer risk.
- **Monosodium Glutamate**: Can cause headaches and other adverse reactions.
- **Salt**: Excessive consumption can lead to high blood pressure, heart disease, stroke, and kidney disease.

## License

This project is licensed under the MIT License.
