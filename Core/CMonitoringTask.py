class CMonitoringTask:
  def __init__(self, links, consume):
    self._links = links
    self._consumeJobs = consume
    return
  
  @property
  def links(self):
    return self._links
  
  def update(self, jobs):
    return self._consumeJobs(jobs)