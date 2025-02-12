import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def search_query(query, count=5):
    """
    Perform a search query using the Serper API.
    Returns a list of results with title, URL, and snippet.
    """
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise Exception("SERPER_API_KEY not set in environment variables. Check your .env file.")

    # Correct API URL (POST request is required)
    endpoint = "https://google.serper.dev/search"

    # Headers required for authentication
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }

    # Proper request payload for a POST request
    payload = {
        "q": query,
        "num": count
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    
    # Check if request was successful
    if response.status_code != 200:
        raise Exception(f"Serper API returned an error: {response.status_code} - {response.text}")

    data = response.json()

    results = []
    # Extract results from "organic" search results
    if "organic" in data:
        for item in data["organic"]:
            results.append({
                "name": item.get("title"),
                "url": item.get("link"),
                "snippet": item.get("snippet")
            })
    return results

# Test script
if __name__ == "__main__":
    test_query = "Role of residual connections in deep neural networks"
    search_results = search_query(test_query)
    for idx, result in enumerate(search_results, start=1):
        print(f"Result {idx}: {result['name']}\nURL: {result['url']}\nSnippet: {result['snippet']}\n")
