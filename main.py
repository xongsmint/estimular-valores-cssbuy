import requests
from src.config import exchange_rate_api_url
from src.fetcher import simulate_cost
import asyncio

# exchange rate
response = requests.get(exchange_rate_api_url)
response = response.json()
yuan_per_brl = response["yuan_per_brl"]
brl_per_yuan = response["brl_per_yuan"]

# na china
shp_country = "Brazil"
products = [
    {
        "total_y": 17,
        "weight_g": 32,
        "attributes": ["Brand"],
        "valor_declarado_dol": 2.3
    },
    {
        "total_y": 14.5,
        "weight_g": 208,
        "attributes": ["Brand"],
        "valor_declarado_dol": 2
    },
    {
        "total_y": 11,
        "weight_g": 220,
        "attributes": ["Brand"],
        "valor_declarado_dol": 2
    }
]

# importando
package_weight_g = 100 # 100g = margin of error
for p in products:
    package_weight_g += p["weight_g"]

asyncio.run(simulate_cost())
