
import time
import os

def clear_screen():
    os.system('clear')

def display_clock():
    try:
        while True:
            clear_screen()
            current_time = time.strftime('%H:%M:%S %p')
            current_date = time.strftime('%A, %B %d, %Y')
            
            print("=" * 40)
            print("           DIGITAL CLOCK")
            print("=" * 40)
            print(f"\n    Time: {current_time}")
            print(f"    Date: {current_date}\n")
            print("=" * 40)
            print("Press Ctrl+C to exit")
            
            time.sleep(1)
    except KeyboardInterrupt:
        clear_screen()
        print("Clock stopped. Goodbye!")

if __name__ == "__main__":
    display_clock()
