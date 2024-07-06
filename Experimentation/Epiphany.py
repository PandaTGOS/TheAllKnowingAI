from getkey import getkey, keys

answer = ""
text = "You are the best ai in the whole world"
count = 0

print("Type Something: ", end='', flush=True)
while True:
    key = getkey()
    print(key, end='', flush=True)
    print(text[count], end='', flush=True)
    count+=1;

    if key =='\n':
        break