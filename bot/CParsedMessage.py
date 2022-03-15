import re

class CParsedMessage:
  def __init__(self, text):
    self._text = text
    return
  
  @property
  def links(self):
    LINKS_RE = r'(https:\/\/www\.upwork\.com\/[^\s]+)'
    matches = re.findall(LINKS_RE, self._text, re.IGNORECASE)
    return list(set(matches))