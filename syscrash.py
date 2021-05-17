from termcolor import colored, cprint

cprint ("The system somehow failed. This might have been because of a bad input or because of a system error\n", 'blue', attrs=['bold'])

cprint ("Restart the OS", 'blue', attrs=['bold'],)


input("Press enter to restart")
import main