import os
from dotenv import load_dotenv
from kiwix import Kiwix

load_dotenv()

def main():
    base_url = os.getenv("KIWIX_SERVER_URL", "http://192.168.8.152:8080")
    print(f"Connecting to kiwix-serve at {base_url}...\n")
    
    kiwix_client = Kiwix(base_url)
    
    print("Fetching books...")
    books = kiwix_client.get_kiwix_book()
    print(f"✅ Found {len(books)} books.\n")
    
    if not books:
        print("No books found. Exiting.")
        return
        
    # Pick a specific book or fallback to the first one available
    example_book = next((b for b in books if "medicine" in (b.name or "").lower()), books[0])
    
    query = "fever"
    print(f"Searching for '{query}' in book: {example_book.title} (ID: {example_book.id})...")
    
    articles = example_book.search_article(query)
    print(f"✅ Found {len(articles)} results for '{query}':")
    
    for article in articles[:5]:
        if article.path:
            print(f" - {article.title}: {article.url}")
            if article.snippet:
                print(f"   Snippet: {article.snippet[:100]}...")
            if article.word_count:
                print(f"   Word Count: {article.word_count} words")
        else:
            print(f" - {article.title} (Pattern match)")
            
    if articles:
        first_article = articles[0]
        print(f"\nFetching content for '{first_article.title}'...")
        try:
            html, headers = first_article.get_article()
            print(f"✅ Retrieved article with {len(headers)} sections.")
            
            # Example: Filter out "References" and "External links"
            exclude_headers = ["References", "External links", "Further reading", "Notes"]
            filtered_headers = [h for h in headers if h.name not in exclude_headers]
            
            print(f"\nFiltered Sections ({len(filtered_headers)} remaining):")
            for h in filtered_headers[:3]:  # Print first 3 to avoid spamming the console
                print(f"\n--- {h.name} ---")
                text_snippet = h.text[:150] + "..." if len(h.text) > 150 else h.text
                print(text_snippet)
                
            if len(filtered_headers) > 3:
                print(f"\n... and {len(filtered_headers) - 3} more sections.")
                
        except Exception as e:
            print(f"Failed to fetch article content: {e}")

if __name__ == "__main__":
    main()
