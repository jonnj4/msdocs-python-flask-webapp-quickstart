from urllib.parse import urlparse, parse_qs

URL = 'http://netloc/path;parameters?query=argument#fragment'
parsed_url = urlparse(URL)
print(parsed_url.scheme)

       