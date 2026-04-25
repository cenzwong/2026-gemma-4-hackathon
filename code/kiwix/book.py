from dataclasses import dataclass
from typing import List, Optional, TYPE_CHECKING
import requests
from .article import Article

if TYPE_CHECKING:
    from .client import Kiwix

@dataclass
class Book:
    client: 'Kiwix'
    id: str
    name: Optional[str] = None
    title: Optional[str] = None
    language: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    article_count: Optional[str] = None
    media_count: Optional[str] = None

    # def __repr__(self) -> str:
    #     title_str = f" title='{self.title}'" if self.title else ""
    #     lang_str = f" language='{self.language}'" if self.language else ""
    #     return f"<Book id='{self.id}'{title_str}{lang_str}>"

    def search_article(
        self,
        pattern: str = "",
        page_length: int = 25,
        start: int = 0,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        distance: Optional[float] = None,
        format_type: str = "xml",
    ) -> List[Article]:
        """
        Performs a full text search on this book and returns matching articles.

        Args:
            pattern: Text to search for (default: empty string).
            page_length: Maximum number of search results in the response. Capped at 140. (default: 25)
            start: Pagination offset for results. Returns results starting with this index. (default: 0)
            latitude: Geospatial query latitude. (optional)
            longitude: Geospatial query longitude. (optional)
            distance: Geospatial query distance in metres. (optional)
            format_type: Format of the search results, e.g. "html" or "xml". (default: "xml")

        Returns:
            A list of Article objects matching the search criteria.

        Examples:
            >>> book.search_article(pattern="fever", page_length=10, start=0)
            >>> book.search_article(pattern="napoli", format_type="xml")
            >>> book.search_article(pattern="hospital", latitude=48.8566, longitude=2.3522, distance=5000)
        """
        search_url = f"{self.client.base_url}/search"
        params = {
            "books.id": self.id,
            "pattern": pattern,
            "pageLength": page_length,
            "start": start,
            "format": format_type,
        }
        
        if latitude is not None:
            params["latitude"] = latitude
        if longitude is not None:
            params["longitude"] = longitude
        if distance is not None:
            params["distance"] = distance

        try:
            response = requests.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            
            if format_type not in ("html", "xml"):
                print(f"Warning: parsing for format '{format_type}' is not implemented. Returning empty list.")
                return []
            
            results = []
            if format_type == "xml":
                import xml.etree.ElementTree as ET
                try:
                    root = ET.fromstring(response.text)
                    channel = root.find('channel')
                    if channel is not None:
                        for item in channel.findall('item'):
                            title = item.findtext('title') or ""
                            href = item.findtext('link') or ""
                            
                            if href.startswith('/'):
                                url = f"{self.client.base_url}{href}"
                                path = href.split('/')[-1] if '/' in href else href
                            else:
                                url = href
                                path = href.split('/')[-1] if '/' in href else href
                                
                            desc_elem = item.find('description')
                            snippet = "".join(desc_elem.itertext()) if desc_elem is not None else None
                            
                            book_elem = item.find('book')
                            book_title = book_elem.findtext('title') if book_elem is not None else None
                            
                            word_count = item.findtext('wordCount')
                            
                            results.append(Article(
                                title=title,
                                path=path,
                                url=url,
                                snippet=snippet,
                                book_title=book_title,
                                word_count=word_count
                            ))
                except ET.ParseError as e:
                    print(f"Error parsing XML response: {e}")
            else:
                from bs4 import BeautifulSoup
                
                soup = BeautifulSoup(response.text, 'html.parser')
                results_container = soup.find('div', class_='results')
                
                if results_container:
                    for li in results_container.find_all('li'):
                        a_tag = li.find('a')
                        if not a_tag:
                            continue
                            
                        title = a_tag.get_text(strip=True)
                        href = a_tag.get('href', '')
                        
                        if href.startswith('/'):
                            url = f"{self.client.base_url}{href}"
                            path = href.split('/')[-1] if '/' in href else href
                        else:
                            url = href
                            path = href.split('/')[-1] if '/' in href else href

                        cite_tag = li.find('cite')
                        snippet = cite_tag.get_text(strip=True) if cite_tag else None
                        
                        book_title_tag = li.find('div', class_='book-title')
                        book_title = book_title_tag.get_text(strip=True) if book_title_tag else None
                        
                        informations_tag = li.find('div', class_='informations')
                        word_count = informations_tag.get_text(strip=True) if informations_tag else None
                        
                        results.append(Article(
                            title=title,
                            path=path,
                            url=url,
                            snippet=snippet,
                            book_title=book_title,
                            word_count=word_count
                        ))
            return results
        except requests.exceptions.RequestException as e:
            print(f"Error searching articles in book {self.id}: {e}")
            return []
