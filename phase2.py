import requests # type: ignore
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

class MegaverseAPI:
    base_url = os.getenv('BASE_URL')
    
    def __init__(self, candidate_id):
        self.candidate_id = candidate_id
    
    def fetch_goal_map(self):
        url = f"{self.base_url}/map/{self.candidate_id}/goal"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
    def create_polyanet(self, row, column):
        data = {
            "row": row,
            "column": column,
            "candidateId": self.candidate_id
        }
        response = requests.post(f"{self.base_url}/polyanets", json=data)
        response.raise_for_status()

    def delete_polyanet(self, row, column):
        data = {
            "row": row,
            "column": column,
            "candidateId": self.candidate_id
        }
        response = requests.delete(f"{self.base_url}/polyanets", json=data)
        response.raise_for_status()
    
    def create_soloon(self, row, column, color):
        data = {
            "row": row,
            "column": column,
            "color": color,
            "candidateId": self.candidate_id
        }
        response = requests.post(f"{self.base_url}/soloons", json=data)
        response.raise_for_status()

    def delete_soloon(self, row, column, color):
        data = {
            "row": row,
            "column": column,
            "color": color,
            "candidateId": self.candidate_id
        }
        response = requests.delete(f"{self.base_url}/soloons", json=data)
        response.raise_for_status()
    
    def create_cometh(self, row, column, direction):
        data = {
            "row": row,
            "column": column,
            "direction": direction,
            "candidateId": self.candidate_id
        }
        response = requests.post(f"{self.base_url}/comeths", json=data)
        response.raise_for_status()

    def delete_cometh(self, row, column, direction):
        data = {
            "row": row,
            "column": column,
            "direction": direction,
            "candidateId": self.candidate_id
        }
        response = requests.delete(f"{self.base_url}/comeths", json=data)
        response.raise_for_status()

def parse_and_create_entities(api, goal_map):
    entity_mapping = {
        "POLYANET": api.create_polyanet,
        "BLUE_SOLOON": lambda r, c: api.create_soloon(r, c, "blue"),
        "RED_SOLOON": lambda r, c: api.create_soloon(r, c, "red"),
        "PURPLE_SOLOON": lambda r, c: api.create_soloon(r, c, "purple"),
        "WHITE_SOLOON": lambda r, c: api.create_soloon(r, c, "white"),
        "UP_COMETH": lambda r, c: api.create_cometh(r, c, "up"),
        "DOWN_COMETH": lambda r, c: api.create_cometh(r, c, "down"),
        "RIGHT_COMETH": lambda r, c: api.create_cometh(r, c, "right"),
        "LEFT_COMETH": lambda r, c: api.create_cometh(r, c, "left"),
    }

    for row_idx, row in enumerate(goal_map):
        for col_idx, entity in enumerate(row):
            if entity in entity_mapping:
                entity_mapping[entity](row_idx, col_idx)

if __name__ == "__main__":
    candidate_id = os.getenv('CANDIDATE_ID')  # candidateId
    api_client = MegaverseAPI(candidate_id)
    
    # Step 1: Fetch the goal map
    goal_map = api_client.fetch_goal_map()
    
    # Step 2: Parse the goal map and create entities automatically
    parse_and_create_entities(api_client, goal_map['goal'])