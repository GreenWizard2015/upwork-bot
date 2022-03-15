import threading

# TODO #1: Impl. data fetching
class CPageMonitor(object):
  def __init__(self, configs):
    self._configs = configs
    self._tasks = {
      # UUID: task
    }
    self._interval = configs.RefreshIntervalMinutes
    self._lock = threading.RLock()
    return
  
  def stop(self, UUID):
    with self._lock:
      task = self._tasks.pop(UUID, None)
    return task
  
  def start(self, UUID, links, callback):
    with self._lock:
      self._tasks[UUID] = {
        'links': links,
        'callback': callback,
        'updated': -1
      }
    return
  
  def refresh(self, UUID):
    with self._lock:
      if UUID in self._tasks:
        self._tasks[UUID]['updated'] = -1
        return True
    return False