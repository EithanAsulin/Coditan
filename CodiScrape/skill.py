import urllib.request
import ssl
import html.parser

class _HTMLTextExtractor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self._text = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self._skip = True

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            self._text.append(data.strip())

    def get_text(self):
        return ' '.join(t for t in self._text if t)

def CodiScrape(website: str) -> str:
    """
    Scrape the given website URL and return all visible text content.
    Uses only Python standard library – zero external dependencies.
    """
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(website, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
            html = response.read().decode('utf-8', errors='replace')
        extractor = _HTMLTextExtractor()
        extractor.feed(html)
        return extractor.get_text()
    except Exception as e:
        return f"Error scraping {website}: {e}"