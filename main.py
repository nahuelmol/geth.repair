from web3 import Web3 

infura_url = 'https://mainnet.infura.io/v3/008192f0ecd445f2bd16825205da6f89'

web3 = Web3(Web3.HTTPProvider(infura_url))
result = web3.isConnected()

print(result)
