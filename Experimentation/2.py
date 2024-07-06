import keyboard

def is_typing():
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            return True

if __name__ == "__main__":
    print("Waiting for user to start typing...")
    user_is_typing = is_typing()
    if user_is_typing:
        print("User is typing.")
    else:
        print("User is not typing.")