class CJob:
  def __init__(self, data):
    self._data = data
    return
  
  def asShortText(self):
    return ' | '.join(map(str, [self.budget, self.title, self.link]))
  
  @property
  def uuid(self):
    return self._data['ciphertext']
  
  @property
  def link(self):
    return 'https://www.upwork.com/freelance-jobs/apply/%s/' % (self.uuid, )
  
  @property
  def title(self):
    return self._data.get('title', '')
  
  @property
  def budget(self):
    # TODO: Impl. budget extraction
    # Example:
    # "amount": {
    #   "currencyCode": "USD",
    #   "amount": 100
    # },
    return '--$'