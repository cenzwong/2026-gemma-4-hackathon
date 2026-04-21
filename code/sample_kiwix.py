import requests
import sys
import json
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_kiwix_data(base_url=None):
    if base_url is None:
        base_url = os.getenv("KIWIX_SERVER_URL", "http://192.168.8.152:8080")
    """
    Connects to the kiwix-serve API and fetches basic information.
    """
    print(f"Connecting to kiwix-serve at {base_url}...\n")
    
    try:
        # 1. Verify the server is accessible
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        print(f"✅ Successfully connected! (Status Code: {response.status_code})")
        
        # 2. Access the catalog (Kiwix usually serves OPDS/JSON catalog at specific endpoints)
        # We try a common endpoint. Adjust if you need a specific search or content endpoint.
        catalog_url = f"{base_url}/catalog/v2/entries"
        catalog_response = requests.get(catalog_url, timeout=10)
        
        if catalog_response.ok:
            print(f"✅ Successfully fetched catalog from {catalog_url}")
            content_type = catalog_response.headers.get('Content-Type', '')
            
            if 'application/json' in content_type:
                data = catalog_response.json()
                print(f"JSON data received. Snippet:")
                print(json.dumps(data, indent=2)[:300] + "...")
            else:
                print(f"Response snippet (Non-JSON):")
                print(catalog_response.text[:300] + "...")
        else:
            print(f"⚠️ Could not fetch standard catalog from {catalog_url}. The API might have different endpoints depending on the kiwix-serve version. (Status: {catalog_response.status_code})")
            
    except requests.exceptions.Timeout:
        print("❌ Error: Connection timed out. Make sure the server is running and accessible on your network.")
        sys.exit(1)
    except requests.exceptions.ConnectionError:
        print(f"❌ Error: Failed to connect to {base_url}.")
        print("Please verify that kiwix-serve is running, the IP address is correct, and port 8080 is open.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the request: {e}")
        sys.exit(1)

def search_articles(base_url, book_id, query):
    """
    Searches for articles in a specific book (ZIM file) using the Kiwix suggest API.
    Book ID should be the UUID of the book (e.g., from the catalog, like '5d963c1c-a44b-f83c-68e4-dec4c71374ed').
    """
    print(f"\nSearching for '{query}' in book '{book_id}'...")
    suggest_url = f"{base_url}/suggest"
    params = {
        "content": book_id,
        "term": query
    }
    
    try:
        response = requests.get(suggest_url, params=params, timeout=10)
        response.raise_for_status()
        
        results = response.json()
        print(f"✅ Found {len(results)} results:")
        for res in results[:5]:  # Print top 5
            label = res.get('label', '')
            label = label.replace('<b>', '').replace('</b>', '')
            label = label.replace('&lt;b&gt;', '').replace('&lt;/b&gt;', '')
            
            path = res.get('path', '')
            if path:
                print(f" - {label}: {base_url}/content/{book_id}/{path}")
            else:
                print(f" - {label} (Pattern match)")
                
    except requests.exceptions.RequestException as e:
        print(f"❌ Error searching: {e}")

if __name__ == "__main__":
    base_url = os.getenv("KIWIX_SERVER_URL", "http://192.168.8.152:8080")
    fetch_kiwix_data(base_url)
    
    # Example book ID from the wikipedia_en_medicine catalog entry
    example_book_idx = "5d963c1c-a44b-f83c-68e4-dec4c71374ed" 
    search_articles(base_url, example_book_idx, "fever")
