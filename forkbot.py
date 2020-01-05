#!/usr/bin/env python
from telegram.ext import Updater
import telegram
import requests
import json
import os
TOKEN = os.environ['TELEGRAM_TOKEN']
updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

def query(update, context):
    repos = json.loads(requests.get('https://api.github.com/orgs/fedora-infra/repos').content)
    repos_printed = []
    for repo in repos:
        if repo['name'] in context.args or len(context.args)==0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="`" + repo['name'] + "` has " + str(repo["forks"]) + " forks!", parse_mode=telegram.ParseMode.MARKDOWN)
            repos_printed.append(repo["name"])
    for repo in context.args:
        if repo not in repos_printed:
            context.bot.send_message(chat_id=update.effective_chat.id, text='`' + repo + "` was not found as a repo of fedora-infra!", parse_mode=telegram.ParseMode.MARKDOWN)
            
from telegram.ext import CommandHandler
start_handler = CommandHandler('q', query)
dispatcher.add_handler(start_handler)
updater.start_polling()
