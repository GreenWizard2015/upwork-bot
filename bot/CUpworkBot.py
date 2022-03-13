from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.dispatcher import run_async
from bot.CEnvironment import CEnvironment

class CUpworkBot:
  def __init__(self, configs, scraper):
    self._configs = configs
    self._scraper = scraper
    return
  
  def bind(self, dp):
    dp.add_handler(MessageHandler(Filters.update.edited_message, self.ignoreEdit))
    #######################
    dp.add_handler(CommandHandler("start", self.help))
    dp.add_handler(CommandHandler("help", self.help))
    #######################
    dp.add_handler(MessageHandler((Filters.text | Filters.command) & (~Filters.update.edited_message), self.process))
    return True
  
  def ignoreEdit(self, update, context):
    pass
  
  def help(self, update, context):
    update.message.reply_text('''Send me URLs to upwork's search and I'll monitor them for new jobs (every %d minutes)
Commands:
/stop - stop monitoring.
/refresh - force update.
    ''' % (self._configs.RefreshIntervalMinutes, ))
    return
  
  @run_async
  def process(self, update, context):
    env = CEnvironment(
      configs=self._configs,
      update=update,
      context=context
    )
    
    try:
      cmd = env.command
      if 'refresh' == cmd: return self.refresh(env)
      if 'stop' == cmd: return self.stop(env)
      
      if self.startLinksMonitoring(env): return
      
      env.send('Unknown command. See /help')
    except Exception as e:
      env.send('Error: %s' % e)
      raise e
    return

  def refresh(self, env):
    links = env.read('links', [])
    if not links:
      env.send('No links for scraping.')
      return
    # TODO: Trigger update event of scraper for current user
    return

  def stop(self, env):
    self._scraper.stop(env.userUUID)
    env.send('Scraping is stopped! No links for scraping.')
    return
  
  def startLinksMonitoring(self, env):
    message = env.message
    # TODO: Extract links from message
    links = []
    if links:
      self._scraper.start(env.userUUID, links, self._notifyUser(env))
      env.send('Start watching: \n' + '\n'.join(links))
      return True
    return False
  
  def _notifyUser(self, env):
    # TODO: Impl. user notification
    def onJob(jobs):
      return
    return onJob