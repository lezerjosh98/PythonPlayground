"""Welcome to my windows funkit script. I hope you have fun."""
from colorama import Fore, init
import sys
import time
init(autoreset=True)#This so we reset style after every line hopefully
def concertlightseffect():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    reset = Fore.RESET
    try:
        while True:
            for color in colors:
                sys.stdout.write(color + "I Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! \nI Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! \nI Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! I Like PARTY LIGHTS!!!!! \n ")
                sys.stdout.flush()
                time.sleep(0.5)
                sys.stdout.write(reset + "     \r")
                sys.stdout.flush()
                time.sleep(0.5)
    except KeyboardInterrupt:
        pass
if __name__ == "__main__":
    concertlightseffect()
