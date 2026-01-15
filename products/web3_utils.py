from web3 import Web3

# Connect to blockchain (you can swap in your actual endpoint)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Replace with your NFT contract details
NFT_CONTRACT_ADDRESS = w3.to_checksum_address("0x1234567890abcdef1234567890abcdef12345678")


NFT_ABI = [
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function",
    },
    {
        "constant": True,
        "inputs": [{"name": "_tokenId", "type": "uint256"}],
        "name": "tokenURI",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function",
    },
]

# Create contract instance
contract = w3.eth.contract(address=NFT_CONTRACT_ADDRESS, abi=NFT_ABI)

def get_total_supply():
    """
    Returns the total supply of NFTs from the contract.
    """
    try:
        supply = contract.functions.totalSupply().call()
        return supply
    except Exception as e:
        print("Error getting total supply:", e)
        return None

def get_token_uri(token_id):
    """
    Returns the metadata URI for a given NFT token ID.
    """
    try:
        token_uri = contract.functions.tokenURI(token_id).call()
        return token_uri
    except Exception as e:
        print(f"Error getting token URI for token {token_id}:", e)
        return None
