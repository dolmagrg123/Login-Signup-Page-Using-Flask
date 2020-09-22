import json
import requests
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults





zillow_data = ZillowWrapper("X1-ZWz170bz3q85qj_9bpwi")
deep_search_response = zillow_data.get_deep_search_results('2114 Bigelow Ave', '98109', True)
result = GetDeepSearchResults(deep_search_response)

print(result.bathrooms)



# address = "8815 Vanderveer Street, Queens Village, NY"
# postal_code= "11427"

# api = zillow.ValuationApi()
# data = api.GetSearchResults(key,address,postal_code)
# print(data)