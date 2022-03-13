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
    # TODO: Add help    
    update.message.reply_text('''Commands:
    ''')
    return
  
  @run_async
  def process(self, update, context):
    env = CEnvironment(
      configs=self._configs,
      update=update,
      context=context
    )
    
    try:
      # TODO: If message contains some upwork's urls, than bind them and begun monitoring
      # TODO: Add /stop command
      cmd = env.command
      if 'refresh' == cmd: return self.refresh(env)
      
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