import requests

def track_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"ISP: {data['isp']}")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
    else:
        print("Failed to track IP.")

# Example usage
ip_address = input("Enter IP address: ")
track_ip(ip_address)

input("Press Enter to exit...")
