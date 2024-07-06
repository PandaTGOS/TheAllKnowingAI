from getkey import getkey, keys

key = getkey()

if key == keys.UP:
  print("r")
#   ...  # Handle the UP key
elif key == keys.DOWN:
  print("s")
#   ...  # Handle the DOWN key
elif key == 'a':
  print("x")
elif key == 'Y':
  print("u")
#   ...  # Handle `shift-y`
else:
  # Handle other text characters
  buffer =''
  buffer += key
  print(buffer)