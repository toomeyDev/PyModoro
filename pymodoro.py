import time, sys, re
from os import system, name

def countdown(t=1500):
    clear_screen()
    print("Timer:\n")
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = "{:002d}:{:002d}".format(mins, secs)
        print(f"{timer}", end="\r")
        time.sleep(1)
        t -= 1

    print("\nTimer complete, time for a break.")
    time.sleep(3)


def break_time(t=300):
    clear_screen()
    print("Break Time:")
    while t > 0:
        mins, secs = divmod(t, 60)
        break_timer = "{:002d}:{:002d}".format(mins, secs)
        print(f"{break_timer}", end="\r")
        time.sleep(1)
        t -= 1

    print("\nBreak complete, time to get back to work.")
    time.sleep(3)


def exit():
    print("Exiting...")
    print("==================================================================")
    sys.exit(1)


def clear_screen():
    """Clear the terminal/console of any generated text."""
    # make use of 'cls' command to clear screen in Windows
    if name == 'nt':
        system('cls')
    # use 'clear' for all other operating systems (linux, macosx etc)
    else:
        system('clear')


def menu():
    while True:
        print("==================================================================")
        print("[0] - Start a standard timer")
        print("[1] - Start a custom timer")
        print("[2] - Exit the application")

        u_input = input("Selection: ")
        u_input = re.sub("\D", "", u_input)
        if u_input == "0":
            print("Starting a standard timer...")
            countdown()
            break_time()
        elif u_input == "1":
            print("Starting a custom timer...")
            length = int(input("Enter the desired length for the timer in seconds: "))
            break_length = int(input("Enter the desired break length in seconds\n"
            +"(IE 300 seconds for 5 min) : "))
            countdown(length)
            break_time(break_length)
        elif u_input == "2":
            exit()
        else:
            print("Please enter a valid choice (options 0-2)")
            time.sleep(3)
            clear_screen()
        clear_screen()


def main():
    print("*| Welcome to PyModoro, a CLI timer application for managing productivity |*\n")
    menu()

if __name__ =="__main__":
    main()
