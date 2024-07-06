# import readline

# def custom_input(prompt):
#     user_input = ""
#     while True:
#         char = readline.getch()  # Get a single character from user input
#         if char == "\n":
#             break  # Exit the loop on Enter key
#         # Modify the character or input here
#         user_input += char
#         modified_input = user_input.upper()  # Example: Convert input to uppercase
#         print(f"\r{prompt}{modified_input}", end="")  # Update the input line in place
#     print()  # Add a newline after Enter is pressed
#     return modified_input

# user_input = custom_input("Type something: ")
# print(f"You typed: {user_input}")


# import keyboard

# def custom_input(prompt):
#     user_input = ""
#     print(prompt, end="", flush=True)
#     while True:
#         event = keyboard.read_event()
#         if event.event_type == keyboard.KEY_DOWN:
#             if event.name == "enter":
#                 break  # Exit the loop on Enter key
#             elif event.name == "backspace":
#                 user_input = user_input[:-1]  # Handle backspace to delete characters
#             elif event.name is not None:
#                 # Modify the character or input here
#                 user_input += event.name.upper()  # Example: Convert input to uppercase
#             # Update the input line in place
#             print("\r" + prompt + user_input + " " * 10, end="", flush=True)
    
#     print()  # Add a newline after Enter is pressed
#     return user_input

# user_input = custom_input("Type something: ")
# print(f"You typed: {user_input}")



import keyboard

def custom_input(prompt):
    user_input = ""
    print(prompt, end="", flush=True)
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == "enter":
                break  # Exit the loop on Enter key
            elif event.name == "backspace":
                user_input = user_input[:-1]  # Handle backspace to delete characters
            elif event.name is not None:
                # Modify the character or input here
                user_input += event.name.upper()  # Example: Convert input to uppercase
            # Clear the line and update it with the prompt and user input
            print("\r" + prompt + user_input, end="", flush=True)
    
    print()  # Add a newline after Enter is pressed
    return user_input

user_input = custom_input("Type something: ")
print(f"You typed: {user_input}")
