import urllib.request
import urllib.parse

values = {'q': 'python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?'+data

headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"


req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)

resp_data = resp.read()