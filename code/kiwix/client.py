import requests
import xml.etree.ElementTree as ET
from typing import List, Optional, Dict, Any
from .book import Book

class Kiwix:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_kiwix_book(
        self,
        start: Optional[int] = None,
        count: Optional[int] = None,
        lang: Optional[str] = None,
        category: Optional[str] = None,
        tag: Optional[str] = None,
        notag: Optional[str] = None,
        maxsize: Optional[int] = None,
        q: Optional[str] = None,
        name: Optional[str] = None
    ) -> List[Book]:
        """
        Fetches the catalog from kiwix-serve and returns a list of Book objects.
        
        Args:
            start: Starting entry index.
            count: Number of entries. Defaults to 10. -1 for unbounded.
            lang: Comma-separated 3-letter language codes.
            category: Comma-separated categories.
            tag: Semicolon-separated tags.
            notag: Semicolon-separated tags to exclude.
            maxsize: Maximum size in bytes.
            q: Title or description query text.
            name: Matching book name.
        """
        catalog_url: str = f"{self.base_url}/catalog/v2/entries"
        
        params: Dict[str, Any] = {}
        if start is not None: params['start'] = start
        if count is not None: params['count'] = count
        if lang is not None: params['lang'] = lang
        if category is not None: params['category'] = category
        if tag is not None: params['tag'] = tag
        if notag is not None: params['notag'] = notag
        if maxsize is not None: params['maxsize'] = maxsize
        if q is not None: params['q'] = q
        if name is not None: params['name'] = name
        
        try:
            response = requests.get(catalog_url, params=params, timeout=10)
            response.raise_for_status()
            
            # Try parsing it as XML first (Native Kiwix-serve response)
            try:
                root = ET.fromstring(response.content)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)
                
                books: List[Book] = []
                for entry in entries:
                    def get_text(tag: str) -> Optional[str]:
                        el = entry.find(f"atom:{tag}", ns)
                        return el.text if el is not None else None
                        
                    raw_id: str = get_text('id') or ''
                    book_id: str = raw_id.replace('urn:uuid:', '')
                    
                    book = Book(
                        client=self,
                        id=book_id,
                        name=get_text('name'),
                        title=get_text('title'),
                        language=get_text('language'),
                        description=get_text('summary'),
                        date=get_text('updated'),
                        article_count=get_text('articleCount'),
                        media_count=get_text('mediaCount')
                    )
                    books.append(book)
                return books
            except ET.ParseError as e:
                # Fallback to JSON if the server actually returned JSON
                try:
                    data = response.json()
                    feed = data.get('feed', {})
                    json_entries = feed.get('entry', [])
                    if isinstance(json_entries, dict):
                        json_entries = [json_entries]
                        
                    books = []
                    for item in json_entries:
                        raw_id = item.get('id', '')
                        book_id = raw_id.replace('urn:uuid:', '')
                        book = Book(
                            client=self,
                            id=book_id,
                            name=item.get('name'),
                            title=item.get('title'),
                            language=item.get('language'),
                            description=item.get('summary'),
                            date=item.get('updated'),
                            article_count=item.get('articleCount'),
                            media_count=item.get('mediaCount')
                        )
                        books.append(book)
                    return books
                except ValueError:
                    print(f"Error parsing response from Kiwix: {e}")
                    return []

        except requests.exceptions.RequestException as e:
            print(f"Error fetching kiwix catalog: {e}")
            return []
