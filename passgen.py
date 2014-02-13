#!/usr/bin/env python3

# imports
from subprocess import Popen, PIPE
from random import choice

# global variables and constants
pw_length = 8
charset_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset_lower = "abcdefghijklmnopqrstuvwxyz"
charset_num = "1234567890"
pw_charset = charset_upper + charset_lower + charset_num

# only tested for osx yet
def set_clipboard_data(data: str):
    p = Popen(['pbcopy'], stdin=PIPE)
    p.stdin.write(data.encode())
    p.stdin.close()
    retcode = p.wait()

def gen_pw() -> str:
    pw = ""
    for i in range(pw_length):
        pw += choice(pw_charset)
    return pw

while True:
    print("This is a simple password generator.", \
            "Just press 'Enter' as long as you want", \
            "to have a password generated. When you like", \
            "to use the password you saw, press ^C (ctrl-c)", \
            "and the password will be copied to your clipboard.", \
            "Press ^D (ctrl-d) to exit without copying.", sep="\n")
    try:
        last_pw = gen_pw()
        input("\n" + last_pw + "\n")
    except KeyboardInterrupt:
        try:
            set_clipboard_data(last_pw)
            print("\nSuccessfully copied.")
            break
        except:
            print("\nError copying to clipboard.")
            break
    except EOFError:
        print("Exited without copying.")
        break