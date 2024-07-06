import sys
import time

def simulate_typing(predefined_string):
    user_input = ""
    
    for char in predefined_string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)  # Adjust the delay time to control the typing speed
    
    while True:
        char = sys.stdin.read(1)
        
        if char == '\n':
            break
        elif char == '\b':
            user_input = user_input[:-1]  # Remove the last character
        else:
            user_input += char
    
    print("\nYou typed:", user_input)

if __name__ == "__main__":
    predefined_string = "You are an idiot"
    simulate_typing(predefined_string)
