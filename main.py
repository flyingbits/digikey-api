import os
import digikey
from digikey.v3.productinformation import KeywordSearchRequest

os.environ['DIGIKEY_CLIENT_ID'] = 'YPhYG9yShwi8CTZ81Gvj9FpJFEh1SHZt'
os.environ['DIGIKEY_CLIENT_SECRET'] = 'z7pVwbcSAW9xL7Fz'
os.environ['DIGIKEY_CLIENT_SANDBOX'] = 'True'
os.environ['DIGIKEY_STORAGE_PATH'] = 'cache_dir'

# Query product number
dkpn = '296-6501-1-ND'
part = digikey.product_details(dkpn)

# Search for parts
search_request = KeywordSearchRequest(keywords='CRCW080510K0FKEA', record_count=10)
result = digikey.keyword_search(body=search_request)

print(result)