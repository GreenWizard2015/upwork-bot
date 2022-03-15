class CJob:
  def __init__(self, uuid, link):
    self._uuid = uuid
    self._link = link
    return
  
  def asShortText(self):
    return ' | '.join(map(str, [self.budget, self.title, self._link]))
  
  @property
  def uuid(self):
    return self._uuid
  
  @property
  def title(self):
    # TODO @1: Impl. title extraction
    return 'Title'
  
  @property
  def budget(self):
    # TODO @1: Impl. budget extraction
    return '--$'