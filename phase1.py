import requests # type: ignore
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

class MegaverseAPI:
    base_url = os.getenv('BASE_URL')
    
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id
    
    def create_polyanet(self, row, column):
        data = {
            "row": row,
            "column": column,
            "candidateId": self.candidate_id
        }
        try:
            url = f"{self.base_url}/polyanets"
            response = requests.post(url, json=data)
            response.raise_for_status()
            print(f"Polyanet created at ({row}, {column})")
        except requests.RequestException as e:
            print(f"Failed to create Polyanet at ({row}, {column}): {e}")
    
    def delete_polyanet(self, row, column):
        data = {
            "row": row,
            "column": column,
            "candidateId": self.candidate_id
        }
        try:
            url = f"{self.base_url}/polyanets"
            response = requests.delete(url, json=data)
            response.raise_for_status()
            print(f"Polyanet deleted at ({row}, {column})")
        except requests.RequestException as e:
            print(f"Failed to delete Polyanet at ({row}, {column}): {e}")

# Polyanet coordinates for the X-shape
polyanet_coordinates = [
    (2, 2), (2, 8),
    (3, 3), (3, 7),
    (4, 4), (4, 6),
    (5, 5),
    (6, 4), (6, 6),
    (7, 3), (7, 7),
    (8, 2), (8, 8)
]

if __name__ == "__main__":
    candidate_id = os.getenv('CANDIDATE_ID')  # candidateId
    api_client = MegaverseAPI(candidate_id)
    
    for row, column in polyanet_coordinates:
        api_client.create_polyanet(row, column)