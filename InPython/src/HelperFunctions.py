import requests
import json

class HelperFunctions:

    @staticmethod
    # Simple GET example using REST API.
    def methodGetExample():
        print(f"{__name__}")
        url = 'https://api.example.com/data'
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return f'Error: {response.status_code}'


    @staticmethod
    # Simple POST example using REST API.
    def methodPostExample():
        print(f"{__name__}")
        url = 'https://api.example.com/data'
        payload = {'key1': 'value1', 'key2': 'value2'}
        response = requests.post(url, data = payload)

        if response.status_code == 200:
            return response.json()
        else:
            return f'Error: {response.status_code}'


    @staticmethod
    # Configure a network device using REST API.
    def update_hostname(device_ip, new_hostname, auth_token):
        url = f'http://{device_ip}/api/v1/configuration'

        print(f"{__name__}")
        print(f"Device IP    : {device_ip}")
        print(f"New hostname : {new_hostname}")
        print(f"Auth Tpken   : {auth_token}")
        print(f"URL          : {url}")

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        }
        payload = {
            'hostname': new_hostname
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            print("Successfully updated the hostname.")
        else:
            print(f"Failed to update hostname. Status Code: {response.status_code}")


    @staticmethod
    # Fetch user data for passed ID using REST API.
    def fetch_user_data(user_id):
        url = f'https://api.example.com/users/{user_id}'

        print(f"{__name__}")
        print(f"User ID : {user_data}")
        print(f"URL     : {url}")

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return f'Error: {response.status_code}'

    
    @staticmethod
    # Call all methods.
    def Check():
        json_data = HelperFunctions.methodGetExample()
        print(f"Json Data = {json_data}")

        json_data = HelperFunctions.methodPostExample()
        print(f"Json Data = {json_data}")

        user_id = 123
        user_data = HelperFunctions.fetch_user_data(user_id)
        print(f"User Data for User ID {user_id} = {user_data}")

        device_ip = '192.168.1.100'
        new_hostname = 'NewRouterName'
        auth_token = '<YOUR_AUTH_TOKEN>'
        HelperFunctions.update_hostname(device_ip, new_hostname, auth_token)