from pynput import keyboard


def init_controller():
    return keyboard.Controller()


def keyListener(hitSpace):
    def on_press(key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        if(k == 'space'):
            hitSpace["space"] = True
        if(k == 'i'):
            print('Init record')
            hitSpace["save"] = True
        if(k == 'e'):
            print('End record')
            hitSpace["save"] = False

    listener = keyboard.Listener(on_press=on_press)
    listener.start()


def pressSpace(handler):
    handler.press(keyboard.Key.space)
    handler.release(keyboard.Key.space)
