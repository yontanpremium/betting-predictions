import os
import json
import requests
from datetime import datetime

def fetch_predictions():
    # Use the API key from your GitHub Secrets
    api_key = os.getenv('FOOTBALL_API_KEY')
    headers = { 'X-Auth-Token': api_key }
    url = "https://api.football-data.org/v4/matches"
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        predictions = []
        
        # Pulling the top 10 matches for today
        for match in data.get('matches', [])[:10]:
            predictions.append({
                "match": f"{match['homeTeam']['shortName']} vs {match['awayTeam']['shortName']}",
                "prediction": "Home Win" if match['homeTeam']['name'] == "Arsenal" else "Over 1.5 Goals",
                "confidence": "91%", 
                "date": datetime.now().strftime("%Y-%m-%d")
            })
        
        if not predictions:
            predictions.append({"match": "No games today", "prediction": "N/A", "confidence": "0%", "date": "N/A"})

        with open('predictions.json', 'w') as f:
            json.dump(predictions, f, indent=4)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_predictions()
  
