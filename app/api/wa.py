from urllib.parse import quote

def getWALink(no: str, title: str) -> str:
    noWA = int(no)
    sub = quote(title)
    link = f'https://wa.me/62{str(noWA)}?text=Saya%20ingin%20membeli%20{sub}'
    return link