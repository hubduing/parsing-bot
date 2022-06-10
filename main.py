from urllib import response
import requests
from fake_useragent import UserAgent
import json

ua = UserAgent()

def collect_data():
    offset = 0
    size_off = 60
    arr = []
    count = 0
    min_price = 2000

    while True:
        for item in range(offset, offset + size_off, 60):
            
            url= f"https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=35&isStore=true&limit=60&maxPrice=10000&minPrice=2000&offset={offset}&sort=botFirst&type=2&withStack=true"
            response = requests.get(
                url=url, 
                headers={"user-agent": f"{ua.random}"}
            )

            offset += size_off

            data = response.json()
            items = data.get("items")

            for i in items:
                if i.get("overprice") is not None and i.get("overprice") < -10:
                    item_full_name = i.get("fullName")
                    item_3d = i.get("3d")
                    item_price = i.get("price")
                    item_over_price = i.get("overprice")

                    arr.append({
                        "full_name": item_full_name,
                        "3d": item_3d,
                        "item_price": item_price,
                        "overprice": item_over_price
                    })
        count += 1       

        if len(items) < 60:
            break

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(arr, file, indent=4, ensure_ascii=False)
    print(len(arr))

def main():
    collect_data()

if __name__ == "__main__":
    main()