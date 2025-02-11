import requests
import time
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MemeCoin
from .serializers import MemeCoinSerializer

# Solana API for scanning new meme coins
DEX_SCANNER_API = "https://api.dexscreener.com/latest/dex/search?q=solana"

class FetchNewMemeCoins(APIView):
    """Fetches new meme coins from DEX Screener API"""
    
    def get(self, request):
        response = requests.get(DEX_SCANNER_API)
        if response.status_code != 200:
            return Response({"error": "Failed to fetch data"}, status=500)

        # Extract coin data
        coins = response.json().get("pairs", [])

        # Save to database
        for coin in coins:
            MemeCoin.objects.update_or_create(
                address=coin["baseToken"]["address"],
                defaults={
                    "name": coin["baseToken"]["name"],
                    "symbol": coin["baseToken"]["symbol"],
                    "price_usd": float(coin.get("priceUsd", 0)),
                    "liquidity": float(coin.get("liquidity", {}).get("usd", 0)),
                },
            )

        return Response({"message": "Meme coins updated in the database."})

class FilterProfitableCoins(APIView):
    """Filters meme coins based on price < $0.01 and liquidity > $5000"""

    def get(self, request):
        profitable_coins = MemeCoin.objects.filter(price_usd__lt=0.01, liquidity__gt=5000)
        serializer = MemeCoinSerializer(profitable_coins, many=True)
        return Response({"filtered_coins": serializer.data})



class BuyToken(APIView):
    """Simulates buying a token based on priceUsd"""

    def post(self, request):
        price_usd = request.data.get("priceUsd")  # Get priceUsd from request
        amount = request.data.get("amount", 0.5)  # Default amount is 0.5 SOL

        if not price_usd:
            return Response({"error": "❌ priceUsd is required!"}, status=400)

        return Response({"message": f"✅ Buying {amount} SOL worth of meme coin at ${price_usd}"})

class SellToken(APIView):
    """Simulates selling a token"""

    def post(self, request):
        price_usd = request.data.get("priceUsd")  # Use priceUsd instead of token_address
        amount = request.data.get("amount", 100)  

        if not price_usd:
            return Response({"error": "❌ priceUsd is required!"}, status=400)

        return Response({"message": f"✅ Selling {amount} tokens of meme coin at ${price_usd}"})

class TradingBot(APIView):
    """Main trading bot that buys and sells meme coins automatically"""

    def get(self, request):
        response = requests.get(DEX_SCANNER_API)
        if response.status_code != 200:
            return Response({"error": "❌ Failed to fetch coins from DEX Screener"}, status=500)
        
        new_coins = response.json().get("pairs", [])

        # Apply filtering: Price < $0.01 and Liquidity > $5000
        profitable_coins = [
            coin for coin in new_coins
            if float(coin.get("priceUsd", 0)) < 0.01 and float(coin.get("liquidity", {}).get("usd", 0)) > 5000
        ]

        for coin in profitable_coins:
            price_usd = coin["priceUsd"]  # Extract priceUsd

            # Simulate Buying
            self.buy_token(price_usd, amount=0.5)
            time.sleep(30)  # Wait for price movement

            # Simulate Selling
            self.sell_token(price_usd, amount=100)

        return Response({"message": "✅ Trading cycle completed."})

    def buy_token(self, price_usd, amount):
        """Simulates buying a token based on priceUsd"""
        print(f"✅ Buying {amount} SOL worth of meme coin at ${price_usd}")
    
    def sell_token(self, price_usd, amount):
        """Simulates selling a token based on priceUsd"""
        print(f"✅ Selling {amount} tokens of meme coin at ${price_usd}")

