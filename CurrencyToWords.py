from src.Support_Functions import convert

"""Loops until the appropriate input is received
Calls the convert function from the convert module"""

def __main__():
    while True:
        try:
            Number = input('Please enter the amount you want to convert or ctrl+c to exit\n')
        except(KeyboardInterrupt, SystemExit):
            print("Exiting...")
            break
        try:
            float(Number)
            if Number != "0":
                print(convert(Number))
                break
            print("Zero")
            break
        except ValueError:
            print("Enter a number.")

if __name__ == "__main__":
    __main__()
