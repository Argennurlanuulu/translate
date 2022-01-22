from translate import Translator
    
from_lang=Translator(from_lang='english',to_lang='Russian')
while True:
    input_translste=input("напишите на английском:")

    translation=from_lang.translate(input_translste)

    print("перевод",translation)
    prodoljenie=input('хочешь продольжить' )

    if prodoljenie=='у':
        continue
    else:
        break










