# TODO: Protect operations with lock
class CPageMonitor(object):
  def __init__(self, configs):
    self._configs = configs
    self._tasks = {
      # UUID: task
    }
    self._interval = configs.RefreshIntervalMinutes
    return
  
  def stop(self, UUID):
    return self._tasks.pop(UUID, None)
  
  def start(self, UUID, links, callback):
    self._tasks[UUID] = {
      'links': links,
      'callback': callback,
      'updated': -1
    }
    return
  
  def refresh(self, UUID):
    if UUID in self._tasks:
      self._tasks[UUID]['updated'] = -1
      return True
    return False