from src.Support_Functions import convert
import time
"""Loops until the appropriate input is received
Calls the convert function from the convert module"""

def main():
    while True:
        try:
            Number = input('Please enter the amount you want to convert or ctrl+c to exit\n')
        except(KeyboardInterrupt, SystemExit):
            print("Exiting...")
            time.sleep(3)
            break
        print(convert(Number)+'\n')

if __name__ == "__main__":
    main()
