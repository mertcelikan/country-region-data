import requests

headers = {
    "X-RapidAPI-Key": "1b91e0eb8amsh9ca8daf5c5fd9fcp11c574jsn2d9a783954a5",
    "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

def country_details(country):
    try:
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country
        response = requests.request("GET", url, headers=headers)
        data = response.json()["data"]
    except Exception as e:
        print("Error while gettin country details: ", e)
    return data

def country_regions(country):
    try:
        url = "https://wft-geo-db.p.rapidapi.com/v1/geo/countries/" + country + "/regions"
        response = requests.request("GET", url, headers=headers)
        data = response.json()
    except Exception as e:
        print("Error while gettin country regions: ", e)
    return data["data"]
