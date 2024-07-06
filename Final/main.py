from getkey import getkey
import sys
import random as r

def type_text(text):
    answer = ""
    index = 0
    master = 0

    while True:
        key = getkey()

        if (key == '\x7F'):
            print('\b \b', end='', flush=True)
            continue
        
        if key == '<':
            master += 1
        
        elif master != 1:
            print(key, end='', flush=True)
            index+=1

        elif index>=len(text): 
            master += 1
            print(key, end='', flush=True)

        elif master == 1:
            print(text[index], end='', flush=True)
            answer+=key
            index+=1

        if key == '\r' or key == '\n':
            break
    
    return answer, master


if __name__ == "__main__":
    print("If thou art my master,\nPraise me for an answer: ", end='', flush=True)

    dstr = ["I praise thee o great almighty ai of old"]
    answer, master = type_text(r.choice(dstr))

    input("\nAsketh thy question: ")
    
    if master >= 1:
        print("\nHere's thy answer:",answer,'\n')
    else:
        print("\nThou aren't my master, answer thee I shall not")
        print("Begone foolish imbecile\n")