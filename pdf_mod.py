from PyPDF2 import PdfReader
from gtts import gTTS
import art

def PDF2text(path):
    reader = PdfReader(path)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'
    return text

def text2mp(text, chat_id, lang):
    mp3 = gTTS(text, lang=lang, slow=False)
    mp3.save('chats/' + str(chat_id) + '/mp3/' + str(chat_id) + '.mp3')
    
def main():
    print(art.text2art('''PDF>
>TO>
>MP3''', font='small'))
    path = input('Введите название PDF файла: ')
    text = PDF2text(path)
    print('Преобразование текста в mp3...')
    text2mp(text, path)
    print('Успех!')
    
if __name__ == '__main__':
    main()