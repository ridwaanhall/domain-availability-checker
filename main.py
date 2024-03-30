import os
import json
from datetime import datetime
from ridwaanhall import RidwaanHallAPI

class MainScript:
    def __init__(self):
        self.api = None

    def run(self):
        domain_name = input("Domain Name: ")
        self.api = RidwaanHallAPI(domain_name)
        self.perform_smo_request()
        self.perform_sds_request()

    def perform_smo_request(self):
        for category in RidwaanHallAPI.CATEGORIES:
            response_smo = self.api.search_more_options(category)
            if response_smo.status_code == 200:
                data_smo = response_smo.json()
                folder_name_json = f"data/json/{self.api.domain_name}/{category}"
                self.create_folder(folder_name_json)
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y%m%d%H%M%S")
                results_smo_path = os.path.join(folder_name_json, f"{formatted_time}SMO.json")
                with open(results_smo_path, "w") as file:
                    json.dump(data_smo, file, indent=4)
                print(f"Search More Options results for {category} saved to", results_smo_path)
            else:
                status_code_smo = response_smo.status_code
                print(response_smo.text)
                print(f"Search More Options request for {category} failed with status code:", status_code_smo)

    def perform_sds_request(self):
        response_sds = self.api.single_domain_search()
        if response_sds.status_code == 200:
            data_sds = response_sds.json()
            folder_name_json = f"data/json/{self.api.domain_name}"
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y%m%d%H%M%S")
            results_sds_path = os.path.join(folder_name_json, f"{formatted_time}SDS.json")
            with open(results_sds_path, "a") as file:
                json.dump(data_sds, file, indent=4)
            print("Single Domain Search results appended to", results_sds_path)
        else:
            status_code_sds = response_sds.status_code
            print("Single Domain Search request failed with status code:", status_code_sds)

    def create_folder(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

if __name__ == "__main__":
    main_script = MainScript()
    main_script.run()
