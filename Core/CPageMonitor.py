import threading
import time
from Core.CUpworkPage import CUpworkPage
from Core.CMonitoringTask import CMonitoringTask

class CPageMonitor():
  def __init__(self, configs, timeProvider=time.time):
    self._configs = configs
    self._tasks = {
      # UUID: task
    }
    self._time = timeProvider
    self._interval = configs.RefreshIntervalMinutes
    self._lock = threading.RLock()
    self._thread = None
    return
  
  def startMonitoring(self):
    assert(self._thread is None)
    self._thread = threading.Thread(target=self._monitoringLoop)
    self._thread.start()
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
  
  def _monitoringLoop(self):
    while True:
      task = self._takeTask()
      if task:
        jobs = self._fetch(task.links)
        task.update(jobs)
        continue
      
      time.sleep(0.1)
      continue
    return
  
  def _takeTask(self):
    # TODO: Add tests 
    task = False
    with self._lock:
      T = self._time()
      for taskData in self._tasks:
        if taskData['updated'] < T:
          T = taskData['updated']
          task = taskData
        continue
    
    if task:
      task = CMonitoringTask(links=task['links'], consume=self._updateTask(task))
    return task
  
  def _fetch(self, links):
    jobs = []
    for url in links:
      try:
        jobs.extend(
          CUpworkPage(url).jobs()
        )
      except Exception as e:
        # TODO: Use logging module
        print(url, e)
      continue
    return jobs
  
  def _updateTask(self, task):
    def f(jobs):
      task['callback'](jobs)
      task['updated'] = self._time()
      return 
    return f