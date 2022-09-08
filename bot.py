import art

print(art.text2art('''BOT
BY
ARTOX''', font='small', chr_ignore=True))
print(art.text2art('TG:', font='white_bubble'), end=' ')
print('@DemonikJR')
print('Libs importing...')

from bot_config import config
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import AdminFilter, ChatTypeFilter
from aiogram.dispatcher import filters
import os
import pdf_mod as pdf
import bot_states as bState

print('Successful! Bot loading...')

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'go'])
async def start_handler(message):
    await message.reply(config.start_message)
    
@dp.message_handler(content_types=['document'])
async def file_handler(message):
    lang = bState.viewLangChoiced(message.chat.id)
    if lang == 'en' or lang == 'ru':
        if 'pdf' in message.document.file_name:
            if message.document.file_size > 20510000:
                await message.reply('Error: File size over 20 MB!') # If file size over 20 MB - send error
            else:
                if 'mp3' not in os.listdir('chats/' + str(message.chat.id) + '/'):
                    os.mkdir('chats/' + str(message.chat.id) + '/pdf')
                    os.mkdir('chats/' + str(message.chat.id) + '/mp3')
                await message.document.download(destination_file='chats/' + str(message.chat.id) + '/pdf/' + str(message.chat.id) + '.pdf')
                await message.answer('Get a file! Start to convert, please wait a 5 minute...')
                text = pdf.PDF2text('chats/' + str(message.chat.id) + '/pdf/' + str(message.chat.id) + '.pdf')
                pdf.text2mp(text, message.chat.id, lang)
                await message.answer('Successful! Got your MP3!')
                await message.reply_document(open('chats/' + str(message.chat.id) + '/mp3/' + str(message.chat.id) + '.mp3', 'rb'))
                bState.resultLangChoiced(message.chat.id)
        else:
            await message.reply('Error: It\'s not a PDF-file!') # If file not a PDF - send error
    else:
        await message.reply('Error: You have not selected a language!') 
    
@dp.message_handler(content_types=['text'], text=['ru', 'en'])
async def lang_handler(message):
    if str(message.chat.id) not in os.listdir('chats/'):
        os.mkdir('chats/' + str(message.chat.id))    
    if not bState.viewLangChoiced(message.chat.id):
        bState.userLangChoiced(message.chat.id, message.text)
        await message.reply('You choice the language.')
    else:
        await message.reply('You already picked the language!')

if __name__ == '__main__':
    print(art.text2art('BOT IS RUN', font='small'))
    executor.start_polling(dp, skip_updates=True)