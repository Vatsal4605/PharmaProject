import requests
import json

def test_pricing_api():
    try:
        # Test the pricing API
        response = requests.get('http://localhost:5000/api/pricing')
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Number of packages: {len(data)}")
            print("Packages:")
            for i, package in enumerate(data):
                print(f"  {i+1}. {package['name']} - {package['price']}")
                print(f"     Description: {package['description']}")
                print(f"     Benefits: {package['benefits']}")
                print()
        else:
            print(f"Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the Flask server is running on http://localhost:5000")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_pricing_api() 