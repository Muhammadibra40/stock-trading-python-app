# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# POLYGON_API_KEY = os.getenv('POLYGON_API_KEY')
# LIMIT = 1000

# url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'


# # response = requests.get(url)


# # print(response.json())
# # next_url = response.json()['next_url']
# # data = response.json()['results']    

# tickers = []
# # params = {"limit": 100, "next_url": None}



# while True:
#     print("Batch being extracted ....")
#     response = requests.get(url).json()
#     try:
#         data = response["results"]
#         tickers.extend(data)

#         # for ticker in data:
#         #     tickers.append(ticker)
    
#         if "next_url" not in response or not response["next_url"]:
#             break
        
#         url = response["next_url"] + f"&apiKey={POLYGON_API_KEY}"
#         print("Batch extraction finished.")

#     except KeyError:
#         print("Data extraction completed.")
#         break



# print(len(tickers))


import requests
import os
import time
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

tickers = []
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit=1000&sort=ticker&apiKey={POLYGON_API_KEY}"

while url:
    print("Batch being extracted ....")
    response = requests.get(url).json()

    data = response["results"]
    if "results" in response:
        tickers.extend(data)


    url = response.get("next_url")
    if url:
        url += f"&apiKey={POLYGON_API_KEY}"
        time.sleep(12)  #prevent hitting Polygon free-tier rate limits
        print("Batch extraction finished.")
    else:
        break

print(f"Total tickers extracted: {len(tickers)}")
df = pd.DataFrame(tickers)

script_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(script_dir)      
output_dir = os.path.join(parent_dir, "Data")  

os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "polygon_tickers.csv")


df.to_csv(output_path, index=False)

print("Data written to polygon_tickers.csv")

