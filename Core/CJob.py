class CJob:
  def __init__(self, uuid):
    self._uuid = uuid
    return
  
  def asShortText(self):
    # TODO: Impl. short job description
    return ''
  
  @property
  def uuid(self):
    return self._uuid