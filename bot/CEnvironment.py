import re
import functools
import hashlib

class CEnvironment:
  def __init__(self, configs, update, context):
    self.configs = configs
    self._update = update
    self._context = context
    
  def send(self, message, disable_web_page_preview=True, disable_notification=True):
    return self._update.message.reply_text(
      message,
      disable_web_page_preview=disable_web_page_preview,
      disable_notification=disable_notification
    )
  
  @property
  def message(self):
    return self._update.message.text
  
  @property
  def username(self):
    chat = self._update.message.chat
    return chat.username
  
  @property
  def userUUID(self):
    chat = self._update.message.chat
    data = [chat.id, chat.username]
    data = '|'.join([str(x) for x in data])
    return hashlib.sha256(data.encode('utf8')).hexdigest()
  
  @property
  @functools.lru_cache(1)
  def command(self):
    match = re.compile(r'^\/(\S+)').search(self.message)
    if match:
      return match.group(1).lower()
    return ''
  
  @property
  @functools.lru_cache(1)
  def args(self):
    args = re.split(r'\s+', self.message)
    if (0 < len(args)) and args[0].startswith('/'):
      args = args[1:]
    return args

  def arg(self, n, default=''):
    args = self.args
    return args[n] if n < len(args) else default

  def store(self, values):
    for k, v in values.items():
      self._context.user_data[k] = v
    return

  def read(self, name, default=None):
    return self._context.user_data.get(name, default)
  
  def filterJobs(self, jobs):
    oldJobs = self.read('jobs', set())
    newJobs = [x for x in jobs if not(x.uuid in oldJobs)]
    oldJobs.update([x.uuid for x in newJobs])
    self.store({'jobs': oldJobs})
    return newJobs