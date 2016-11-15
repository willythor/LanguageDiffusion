''' google_translate101.py
experimenting with the Google Translate API
Goslate: Free Google Translate API
download goslate.py from ...
https://bitbucket.org/zhuoqiang/goslate/raw/tip/goslate.py
info ...
http://pythonhosted.org/goslate/
some language codes
English = 'en'
German = 'de'
French = 'fr'
Spanish = 'es'
Dutch = 'nl'
Swedish = 'sv'
Finnish = 'fi'
be careful which IDE you use
Spyder, IEP and IDLE are okay
PyScripter will screw up some of the foreign characters
tested with Python33  by  vegaseat  06nov2014
'''
import goslate
gs = goslate.Goslate()
# translate a given string to the language given by the code
print(gs.translate('hello world', 'de'))  # Hallo Welt
print(gs.translate('hello world', 'fr'))  # Bonjour tout le monde
print(gs.translate('hello world', 'es'))  # hola mundo
print(gs.translate('hello world', 'nl'))  # hallo wereld
print(gs.translate('hello world', 'sv'))  # hallÃ¥ vÃ¤rlden
print(gs.translate('hello world', 'fi'))  # Hei maailma
print('-'*40)
text = '''\
Good morning!
I hope you have all slept well.
'''
# translate(text, target_language, source_language=u'')
# english to german
print(gs.translate(text, 'de', 'en'))
'''
Guten Morgen!
Ich hoffe, Sie haben alle gut geschlafen.
'''
print('-'*40)
# english to dutch
print(gs.translate(text, 'nl', 'en'))
'''
Goedemorgen!
Ik hoop dat jullie allemaal goed geslapen.
'''
print('-'*40)
# more stuff ...
# romanized Chinese
gs_roman = goslate.Goslate(goslate.WRITING_ROMAN)
print(gs_roman.translate('hello world', 'zh'))  # NÇ hÇŽo shÃ¬jiÃ¨
# detect the language code of a given string
print(gs.detect('hello world'))  # en