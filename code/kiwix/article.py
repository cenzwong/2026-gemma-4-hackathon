from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class Header:
    name: str
    text: str

@dataclass
class Article:
    title: str
    path: str
    url: str
    snippet: Optional[str] = None
    book_title: Optional[str] = None
    word_count: Optional[str] = None

    def get_article(self) -> Tuple[str, List[Header]]:
        """
        Fetches the article's HTML content and parses it into a list of headers.
        Returns a tuple containing the raw HTML and a list of Header objects.
        """
        import requests
        from bs4 import BeautifulSoup
        
        response = requests.get(self.url, timeout=10)
        response.raise_for_status()
        html = response.text
        
        soup = BeautifulSoup(html, 'html.parser')
        mw_parser = soup.find('div', class_='mw-parser-output')
        
        headers = []
        current_name = "Introduction"
        current_text = []
        
        if mw_parser:
            for element in mw_parser.find_all(recursive=False):
                is_heading = False
                heading_text = ""
                
                if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    is_heading = True
                    heading_text = element.get_text(strip=True)
                elif element.name == 'div' and element.get('class') and any(c.startswith('mw-heading') for c in element.get('class')):
                    is_heading = True
                    heading_text = element.get_text(strip=True)
                    
                if is_heading:
                    if current_text or current_name == "Introduction":
                        headers.append(Header(name=current_name, text=" ".join(current_text).strip()))
                    current_name = heading_text
                    current_text = []
                else:
                    text = element.get_text(separator=' ', strip=True)
                    if text:
                        current_text.append(text)
                        
            if current_text:
                headers.append(Header(name=current_name, text=" ".join(current_text).strip()))
        else:
            # Fallback if there is no mw-parser-output
            headers.append(Header(name="Content", text=soup.get_text(separator=' ', strip=True)))
            
        return html, headers
