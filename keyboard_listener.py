from pynput import keyboard

controller = keyboard.Controller()

def on_press(key):
    try:
        if key.char == '[':
            controller.press(keyboard.Key.backspace)
            controller.release(keyboard.Key.backspace)
            controller.press('「')
            controller.release('「')
        if key.char == ']':
            controller.press(keyboard.Key.backspace)
            controller.release(keyboard.Key.backspace)
            controller.press('」')
            controller.release('」')
    except AttributeError:
        pass
    

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
