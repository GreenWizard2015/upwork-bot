import requests

class CUpworkPage:
  def __init__(self, url, http=requests):
    self._url = url
    self._http = http
    return
  
  def jobs(self):
    # TODO: Impl. fetching jobs from url
    return []
