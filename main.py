from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get-location', methods=['POST'])
def get_location():
    # Get the address from the request
    data = request.get_json()
    address = data.get('address')

    if not address:
        return jsonify({"error": "Address is required"}), 400

    # Prepare the payload for the external request
    payload = f'address={address}'

    # Make the POST request to the Ghana Post GPS service
    url = "https://ghanapostgps.sperixlabs.org/get-location"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an error if the request failed
        # Return the response from the external API
        return jsonify(response.json()), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to retrieve location: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
