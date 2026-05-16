import os
from kiwix import Kiwix
base_url = "http://192.168.8.152:8080"
k = Kiwix(base_url)
books = k.get_kiwix_book()
print(f"Found {len(books)} books")
for b in books:
    print(b.name, b.title, b.id)
