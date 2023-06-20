# # CryptoFusePy

CryptoFusePy is a Python library for interacting with the [CryptoFuse API](https://www.cryptofuse.net/api_docs). It enables developers to easily integrate CryptoFuse's cryptocurrency swapping functionality into their Python applications.


# ## Installation

Alternatively, if the package is available on PyPI, you can install it using `pip`:


```sh
git clone https://github.com/your_username_here/cryptofusepy.git
cd cryptofusepy
pip install .
```
## Usage

You can use the `CryptoFuseClient` class from the `cryptofusepy` package to interact with the CryptoFuse API.

Here's a quick example on how you can instantiate the client and fetch the available cryptocurrencies:

```python
from cryptofusepy import CryptoFuseClient

# Instantiate the client
client = CryptoFuseClient()

# Fetch available cryptos
available_cryptos = client.fetch_available_cryptos()
print(available_cryptos)
```

For a more detailed example that shows how to use all the endpoints, please see the [example.py](example.py) file in this repository.

## Available Methods

Here is a list of available methods in the `CryptoFuseClient` class:

- `fetch_available_cryptos(): Fetches the available cryptocurrencies.`
- `fetch_exchange_rate(from_crypto, to_crypto): Fetches the exchange rate between two cryptocurrencies.`
- `generate_address(from_crypto, to_crypto, user_address, referral=None): Generates an address for swapping.`
- `register_referral(to_crypto, user_address, referral): Registers a referral.`
- `get_address_by_uuid(uuid): Retrieves address information by UUID.`
- `get_latest_transaction(uuid, latest_known_transaction_id=None, latest_known_transaction_status=None): Retrieves the latest transaction for the provided UUID.`
- `get_crypto_swap_status(): Retrieves the Crypto Swap status.`

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue if you find a bug or have a feature request.