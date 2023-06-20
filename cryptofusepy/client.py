import requests

BASE_URL = 'https://www.cryptofuse.net/crypto_swap/api/'

class CryptoFuseClient:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

    def fetch_available_cryptos(self):
        endpoint = 'available_cryptos/'
        url = BASE_URL + endpoint
        response = self.session.post(url)
        return response.json()

    def fetch_exchange_rate(self, from_crypto, to_crypto):
        endpoint = 'get_exchange_rate/'
        url = BASE_URL + endpoint
        data = {'from_crypto': from_crypto, 'to_crypto': to_crypto}
        response = self.session.post(url, json=data)
        return response.json()

    def generate_address(self, from_crypto, to_crypto, user_address, referral=None):
        endpoint = 'generate_address/'
        url = BASE_URL + endpoint
        data = {'from_crypto': from_crypto, 'to_crypto': to_crypto, 'user_address': user_address, 'referral': referral}
        response = self.session.post(url, json=data)
        return response.json()

    def register_referral(self, to_crypto, user_address, referral):
        endpoint = 'register_referral/'
        url = BASE_URL + endpoint
        data = {'to_crypto': to_crypto, 'user_address': user_address, 'referral': referral}
        response = self.session.post(url, json=data)
        return response.json()

    def get_address_by_uuid(self, uuid):
        endpoint = f'get_address_by_uuid/{uuid}/'
        url = BASE_URL + endpoint
        response = self.session.get(url)
        return response.json()

    def get_latest_transaction(self, uuid, latest_known_transaction_id=None, latest_known_transaction_status=None):
        endpoint = 'get_latest_transaction/'
        url = BASE_URL + endpoint
        data = {
            'uuid': uuid,
            'latest_known_transaction_id': latest_known_transaction_id,
            'latest_known_transaction_status': latest_known_transaction_status
        }
        response = self.session.post(url, json=data)
        return response.json()

    def get_crypto_swap_status(self):
        endpoint = 'crypto_swap_status/'
        url = BASE_URL + endpoint
        response = self.session.post(url)
        return response.json()
