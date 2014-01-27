import subprocess
import random

# only tested for osx yet
def set_clipboard_data(data: str):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data.encode())
    p.stdin.close()
    retcode = p.wait()

def gen_pw() -> str:
    return "NoGeneratedPass"

while True:
    print("""This is a simple password generator.
            Just press 'Any Key' as long as you want
            to have a password generated. When you like
            to use the password you saw, press ^C (ctrl-c)
            and the password will be copied to your clipboard.""")
    try:
        last_pw = gen_pw()
        input(last_pw + "\n")
    except KeyboardInterrupt:
        try:
            set_clipboard_data(last_pw)
            print("\nSuccessfully copied.")
            break
        except:
            raise
            print("\nError copying to clipboard.")
            break