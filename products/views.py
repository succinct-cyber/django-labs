from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .models import Wallet
from web3 import Web3
from . import web3_utils
from web3 import Web3
import json
from .web3_utils import get_total_supply, get_token_uri



def home(request):
    total_supply = get_total_supply()
    return render(request, 'products/products.html', {'total_supply': total_supply})



import requests

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def nft_gallery(request):
    return render(request, 'products/products.html', {'title': 'Available NFT Collection'})

# products/views.py

def register_wallet(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        if address:
            wallet, created = Wallet.objects.get_or_create(address=address)
            return JsonResponse({'status': 'ok', 'created': created})
    return JsonResponse({'status': 'error'})

def register_wallet(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        print(f"Wallet connected: {address}")
        # Optionally save to DB here
        return JsonResponse({'status': 'success', 'address': address})
    
    # products/views.py 

def nft_gallery(request):
    total = get_total_supply()
    nfts = []
    for i in range(total):
        token_uri = get_token_uri(i)
        metadata = requests.get(token_uri).json()
        nfts.append(metadata)
    return render(request, 'products/products.html', {'nfts': nfts})

# Connect to your node (e.g. Infura)
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY"))

def get_total_supply(contract_address, abi):
    contract = w3.eth.contract(
        address=Web3.to_checksum_address(contract_address),
        abi=abi
    )
    return contract.functions.totalSupply().call()

def get_token_uri(contract_address, abi, token_id):
    contract = w3.eth.contract(
        address=Web3.to_checksum_address(contract_address),
        abi=abi
    )
    return contract.functions.tokenURI(token_id).call()



