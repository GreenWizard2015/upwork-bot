import requests
import json
from Core.CJob import CJob

def defaultHttp(url):
  return requests.get(
    url, headers={
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'cache-control': 'no-cache',
      'x-requested-with': 'XMLHttpRequest'
    }
  ).content

# TODO: Rename to more suitable name i.e. CSearchResults
class CUpworkPage:
  def __init__(self, url, http=defaultHttp):
    self._url = url
    self._http = http
    return
  
  def jobs(self):
    resp = self._http(self._url)
    data = json.loads(resp)
    # TODO: Dump response on error
    return [CJob(x) for x in data['searchResults']['jobs']]