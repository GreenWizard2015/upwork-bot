class CPageMonitor(object):
  def __init__(self, configs):
    self._configs = configs
    self._tasks = {
      # UUID: task
    }
    return
  
  def stop(self, UUID):
    return self._tasks.pop(UUID, None)