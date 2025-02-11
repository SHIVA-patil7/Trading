from django.urls import path
from .views import FetchNewMemeCoins, FilterProfitableCoins, BuyToken, SellToken, TradingBot

urlpatterns = [
    path("fetch-coins/", FetchNewMemeCoins.as_view(), name="fetch-coins"),
    path("filter-coins/", FilterProfitableCoins.as_view(), name="filter-coins"),
    path("buy/", BuyToken.as_view(), name="buy-token"),
    path("sell/", SellToken.as_view(), name="sell-token"),
    path("trade/", TradingBot.as_view(), name="trading-bot"),
]

