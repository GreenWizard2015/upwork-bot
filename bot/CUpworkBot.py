from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.ext.dispatcher import run_async
from bot.CEnvironment import CEnvironment

class CUpworkBot:
  def __init__(self, configs):
    self.configs = configs
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
      configs=self.configs,
      update=update,
      context=context
    )
    
    try:
      # TODO: If message contains some upwork's urls, than bind them and begun monitoring
      # TODO: Add /stop command
      # TODO: Add /refresh command
      cmd = env.command
      env.send('Unknown command. See /help')
    except Exception as e:
      env.send('Error: %s' % e)
      raise e
    return
