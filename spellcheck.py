import urllib.request
import enchant

def clean(word):
    word = word.strip()
    word = word.lower()
    return word

# def browsercontent(url):
#     try:
#         fp = urllib.request.urlopen(url)
#         mybytes = fp.read()
#         mystr = mybytes.decode("utf8")
#         fp.close()    
#     except:
#         print ("ERROR: COULD NOT RECEIVE WEB DATA")
#         return "ERROR"
#     return mystr

def priblink(word):
    #return "https://www.dictionary.com/browse/"+clean(word)
    d = enchant.Dict("en_US")
    if (d.check(word) == True):
        return True
    else:
        url = "https://raw.githubusercontent.com/gracinev/BoggleBot/main/Legal_Words.txt"
        file = urllib. request.urlopen(url)
        if (word.upper() in str(file.read(), 'utf-8')):
            return True
    return False

def check(word):
    # web = browsercontent(priblink(word))
    web = priblink(word)
    return web
    # if (web == "ERROR"):
    #     return False
    #return not (("No results found for") in web) 

# PORTUGUESE VERSION
#
#def priblink(word):
#    return "https://dicionario.priberam.org/"+clean(word)
#
#def check(word):
#    web = browsercontent(priblink(word))
#    return not (("Palavra n"+chr(227)+"o encontrada.") in web) 