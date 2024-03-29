#
# instagram.com/ridwaanhall
#

import requests
import ridwaanhall

smo_url:str = ridwaanhall.BASE_API + "api/domain/search-more-options"
sds_url:str = ridwaanhall.BASE_API + "api/domain/single-domain-search"

response_smo:requests.Response = requests.post(smo_url, json=ridwaanhall.payload_smo, headers=ridwaanhall.headers_global)

if response_smo.status_code == 200:
    data_smo:dict = response_smo.json()
    print(data_smo)
else:
    status_code_smo:int = response_smo.status_code
    print(status_code_smo)
