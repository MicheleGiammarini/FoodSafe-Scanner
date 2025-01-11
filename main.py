from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Simulated database of risky ingredients
RISKY_INGREDIENTS = {
    "aspartame": "May cause allergic reactions and has potential brain effects.",
    "BHA": "Potential carcinogen linked to liver and kidney damage.",
    "BHT": "Potential carcinogen that can alter metabolism.",
    "acrylamide": "Classified as a carcinogen, linked to increased cancer risk.",
    "monosodium glutamate": "Can cause headaches and other adverse reactions.",
    "salt": "Excessive consumption of salt can lead to high blood pressure, increased risk of heart disease, stroke, kidney disease, and headaches due to dehydration."

}

# Endpoint to get product information via barcode
@app.route('/scan', methods=['POST'])
def scan_barcode():
    data = request.get_json()
    if not data or 'barcode' not in data:
        return jsonify({"error": "Barcode is required"}), 400

    barcode = data['barcode']
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    # Call Open Food Facts API
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch product data: {str(e)}"}), 500

    product_data = response.json()
    if product_data.get('status') != 1:
        return jsonify({"error": "Product not found"}), 404

    product = product_data['product']
    result = {
        "product_name": product.get("product_name", "Unknown"),
        "ingredients": [i.get('text', '').lower() for i in product.get("ingredients", [])],
        "nutritional_info": product.get("nutriments", {})
    }
    return jsonify(result), 200

# New endpoint to analyze ingredients starting from barcode
@app.route('/analyze', methods=['POST'])
def analyze_ingredients():
    data = request.get_json()
    if not data or 'barcode' not in data:
        return jsonify({"error": "Barcode is required"}), 400

    barcode = data['barcode']
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    # Call Open Food Facts API to get the product data
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for HTTP errors
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to fetch product data: {str(e)}"}), 500

    product_data = response.json()
    if product_data.get('status') != 1:
        return jsonify({"error": "Product not found"}), 404

    product = product_data['product']
    ingredients = [i.get('text', '').lower() for i in product.get("ingredients", [])]

    # Analyze the ingredients against the risky ingredients list
    risks = []
    for ingredient in ingredients:
        if ingredient in RISKY_INGREDIENTS:
            risks.append({
                "ingredient": ingredient,
                "risk": RISKY_INGREDIENTS[ingredient]
            })

    # Return the analysis result
    return jsonify({
        "product_name": product.get("product_name", "Unknown"),
        "ingredients": ingredients,
        "risks": risks
    }), 200

# Start the server on 0.0.0.0 and dynamic port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the dynamic port provided by Replit or default to 5000
    app.run(host='0.0.0.0', port=port, debug=True)
