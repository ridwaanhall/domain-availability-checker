#
# instagram.com/ridwaanhall
#

import requests
import json
import os
from datetime import datetime
import ridwaanhall

# Define folder name
folder_name_json = f"data/json/{ridwaanhall.domain_name}"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name_json):
    os.makedirs(folder_name_json)
    
# Get current date and time
current_time = datetime.now()

# Format the current date and time
formatted_time = current_time.strftime("%Y%m%d%H%M%S")

# Define file paths inside the folder
results_smo_path = os.path.join(folder_name_json, f"{formatted_time}SMO.json")
results_sds_path = os.path.join(folder_name_json, f"{formatted_time}SDS.json")

# Perform Search More Options request
response_smo = requests.post(ridwaanhall.smo_url, json=ridwaanhall.payload_smo, headers=ridwaanhall.headers_global)

if response_smo.status_code == 200:
    data_smo = response_smo.json()

    with open(results_smo_path, "w") as file:
        json.dump(data_smo, file, indent=4)

    print("Search More Options results saved to", results_smo_path)
else:
    status_code_smo = response_smo.status_code
    print(response_smo.text)
    print("Search More Options request failed with status code:", status_code_smo)

# Perform Single Domain Search request
response_sds = requests.post(ridwaanhall.sds_url, json=ridwaanhall.payload_sds, headers=ridwaanhall.headers_global)

if response_sds.status_code == 200:
    data_sds = response_sds.json()

    with open(results_sds_path, "a") as file:
        json.dump(data_sds, file, indent=4)

    print("Single Domain Search results appended to", results_sds_path)
else:
    status_code_sds = response_sds.status_code
    print("Single Domain Search request failed with status code:", status_code_sds)
