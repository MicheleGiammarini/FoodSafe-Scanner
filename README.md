FoodSafe Scanner
FoodSafe Scanner is a Flask-based web application that helps users analyze food products for risky ingredients by scanning their barcodes. The app connects to the Open Food Facts API to retrieve product data and checks it against a pre-defined list of risky ingredients to alert users about potential health risks.

Features
Scan Products: Retrieve product information via barcode.
Analyze Ingredients: Check ingredients for potential risks (e.g., allergens, carcinogens).
Nutrition Info: View nutritional data for products.
Installation
Clone the repository:
bash
Copia codice
git clone https://github.com/MicheleGiammarini/FoodSafe-Scanner.git
Install dependencies:
Copia codice
pip install -r requirements.txt
Run the app:
css
Copia codice
python main.py
API Endpoints
POST /scan: Scans a product barcode and returns basic product information.
POST /analyze: Analyzes product ingredients for potential risks.
Risky Ingredients Database
The following ingredients are flagged for potential health risks:

Aspartame
BHA
BHT
Acrylamide
Monosodium glutamate
Salt
License
This project is licensed under the MIT License - see the LICENSE file for details.
