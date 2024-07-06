import getpass

try:
    p = getpass.getpass(prompt = "Speak: ")
except Exception as error:
    print('ERROR', error)
    
else:
    print('You typed:', p)
