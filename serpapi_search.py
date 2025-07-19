import requests

api_key = 'my api key' 

params = {
    'engine': 'google',
    'q': 'web3 founders',
    'api_key': api_key,
    'num': 10  # number of results to get
}

response = requests.get('https://serpapi.com/search', params=params)

if response.status_code == 200:
    data = response.json()
    results = data.get('organic_results', [])
    for i, result in enumerate(results, 1):
        print(f"{i}. {result.get('title')}")
        print(f"   {result.get('link')}\n")
else:
    print(f"Error: HTTP {response.status_code}")
