from cryptofusepy import CryptoFuseClient

# Instantiate the client
client = CryptoFuseClient()

# Fetch available cryptos
print("\nFetching available cryptos...")
response = client.fetch_available_cryptos()
available_cryptos = response.get('available_cryptos', [])
print(available_cryptos)

# Check if there are at least two cryptos available for the example
if not available_cryptos or len(available_cryptos) < 2:
    print("Not enough cryptos available for the example.")
    exit()

# Fetch exchange rate
from_crypto = "NANO"  # Extract the first element of the first crypto
to_crypto = "BAN"    # Extract the first element of the second crypto
print(f"\nFetching exchange rate from {from_crypto} to {to_crypto}...")
exchange_rate = client.fetch_exchange_rate(from_crypto, to_crypto)
print(exchange_rate)

# Generate address
user_address = "ban_1em9ej7jdcmuhwhwydwohb63xf5bjajzob5hp4x9fzzyhants5jckn684e3f"  # Replace with a real user address
print(f"\nGenerating address for swapping {from_crypto} to {to_crypto}...")
generated_address = client.generate_address(from_crypto, to_crypto, user_address)

print(generated_address)

# Register referral
referral = "yourreferral"  # Replace with a real referral code
print(f"\nRegistering referral for {to_crypto}...")
referral_registration = client.register_referral(to_crypto, user_address, referral)
print(referral_registration)


# Get address by UUID if available from generate_address response
if 'id' in generated_address:
    uuid = generated_address['id']
    
    print(f"\nGetting address by UUID {uuid}...")
    address_by_uuid = client.get_address_by_uuid(uuid)
    print(address_by_uuid)


    print(f"\nGetting latest transaction for UUID {uuid}...")
    latest_transaction = client.get_latest_transaction(uuid)
    print(latest_transaction)


    

else:
    print("\nUUID not available in the response from generate_address endpoint.")


# Get Crypto Swap status
print("\nGetting Crypto Swap status...")
crypto_swap_status = client.get_crypto_swap_status()
print(crypto_swap_status)
