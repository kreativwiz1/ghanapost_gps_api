# Ghana Post GPS Location Service 📍

A Flask-based REST API service that provides detailed location information by interfacing with the Ghana Post GPS digital addressing system. This service enables easy retrieval of comprehensive location data including coordinates, street names, and administrative regions from digital addresses.

## ✨ Features

- **Location Data Retrieval**
  - Digital address validation
  - Coordinate extraction
  - Street name lookup
  - Administrative region identification

- **Comprehensive Response Data**
  - Latitude and longitude coordinates
  - Street names and descriptions
  - Administrative regions
  - Area and district information
  - Postal codes

- **API Features**
  - RESTful architecture
  - JSON response format
  - Robust error handling
  - Request validation

## 📋 Prerequisites

- Python 3.11 or higher
- Poetry (dependency management)
- Internet connection for API requests

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/kreativwiz1/ghana_post_gps.git
cd ghana_post_gps
```

2. Install dependencies:
```bash
poetry install
```

3. Configure environment variables (if required):
```bash
export GHANA_POST_API_KEY="your-api-key"
```

## 📡 API Reference

### Get Location Details

Retrieves detailed location information from a Ghana Post GPS digital address.

#### Endpoint
```
POST /get-location
Content-Type: application/json
```

#### Request Body
```json
{
  "address": "GW-0007-3916"
}
```

#### Success Response
```json
{
  "data": {
    "Table": [{
      "AddressV1": "GW00073916",
      "Area": "Amasaman",
      "CenterLatitude": 5.701875828062917,
      "CenterLongitude": -0.299161335820203,
      "District": "Ga West",
      "Street": "Nii Ayi Lamptey I Crescent",
      "Region": "Greater Accra",
      "PostCode": "GW0007",
      "Coordinates": {
        "NE": {"lat": 5.702375, "lng": -0.298661},
        "SW": {"lat": 5.701376, "lng": -0.299661}
      }
    }]
  },
  "found": true
}
```

#### Error Response
```json
{
  "error": "Invalid address format",
  "code": "INVALID_ADDRESS",
  "status": 400
}
```

## 💻 Usage Examples

### cURL
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"address":"GW-0007-3916"}' \
  http://localhost:5000/get-location
```

### Python
```python
import requests

response = requests.post(
    'http://localhost:5000/get-location',
    json={'address': 'GW-0007-3916'}
)
location_data = response.json()
```

## 🚀 Deployment

### Development
```bash
python main.py
```

### Production
Using Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 main:app
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|-----------|
| GHANA_POST_API_KEY | API key for Ghana Post GPS | Yes |
| FLASK_ENV | Development/Production mode | No |
| PORT | API port (default: 5000) | No |

### Dependencies
```toml
[tool.poetry.dependencies]
python = "^3.11"
flask = "^2.0.1"
requests = "^2.27.1"
gunicorn = "^20.1.0"
```

## 🔍 Error Handling

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid address format |
| 401 | Unauthorized - Invalid API key |
| 404 | Not Found - Address not found |
| 500 | Internal Server Error - External API failure |

## 📊 Performance Considerations

- **Rate Limiting**
  - External API rate limits apply
  - Consider implementing caching for frequent requests

- **Timeouts**
  - Default request timeout: 30 seconds
  - Configurable through environment variables

## 🛡️ Security

- Input validation for address format
- API key authentication
- HTTPS recommended for production
- Request size limits

## 🧪 Testing

Run the test suite:
```bash
poetry run pytest
```

Example test cases:
```python
def test_valid_address():
    response = client.post('/get-location', json={'address': 'GW-0007-3916'})
    assert response.status_code == 200
    assert response.json['found'] == True
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📮 Support

For support:
- Open an issue in the GitHub repository
- Contact the maintainers
- Check documentation for common issues

## 📚 Additional Resources

- [Ghana Post GPS Documentation](https://ghanapostgps.com/developers)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Requests Library](https://docs.python-requests.org/)