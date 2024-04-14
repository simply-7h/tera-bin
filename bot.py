import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def download(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    file_id = update.message.text.split()[1]
    file_info = context.bot.get_file(file_id)
    file_path = file_info.file_path
    if file_path.endswith('.mp4'):
        download_url = 'https://api.telegram.org/file/bot{}/{}'.format(context.bot.token, file_path)
        response = requests.get(download_url)
        with open('video.mp4', 'wb') as f:
            f.write(response.content)
        update.message.reply_text('Video downloaded successfully!')
    else:
        update.message.reply_text('Invalid file type. Only MP4 files are supported.')

def main() -> None:
    updater = Updater(token='7017046466:AAG7fozqorxqO9wdLKBFRwpFOZUvqafsNl8', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('download', download))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
