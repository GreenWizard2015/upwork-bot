class CMonitoringTask:
  def __init__(self, links):
    self._links = links
    return
  
  @property
  def links(self):
    return self._links
  
  def update(self, jobs):
    # TODO: Impl. sending jobs to callback & refreshing task last update time
    return