#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from telegram.ext import Updater
from python_json_config import ConfigBuilder
from bot.CUpworkBot import CUpworkBot

logging.basicConfig(
  format='%(asctime)s - %(levelname)s - %(message)s',
  level=logging.INFO
)
logger = logging.getLogger(__name__)

def error(update, context):
  """Log Errors caused by Updates."""
  logger.warning('Update "%s" caused error "%s"', update, context.error)
  return

def main():
  configs = ConfigBuilder().parse_config('configs.json')

  updater = Updater(configs.TelegramToken, use_context=True)
  bot = CUpworkBot(configs=configs)
  bot.bind(updater.dispatcher)
  updater.dispatcher.add_error_handler(error)

  updater.start_polling()
  updater.idle()
  return

if __name__ == '__main__': main()
