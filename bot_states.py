import shelve, os


def viewLangChoiced(chat_id):
    if str(chat_id) in os.listdir(path='chats/'):
        if str(chat_id) + '.dat' in os.listdir(path='chats/' + str(chat_id)):
            with shelve.open('chats/' + str(chat_id) + '/' + str(chat_id)) as db:
                return db['LangChoiced']
        else:
            return False
    else:
        return False

def userLangChoiced(chat_id, lang):
    with shelve.open('chats/' + str(chat_id) + '/' + str(chat_id)) as db:
        db['LangChoiced'] = lang
        
def resultLangChoiced(chat_id):
    with shelve.open('chats/' + str(chat_id) + '/' + str(chat_id)) as db:
        db['LangChoiced'] = ''    