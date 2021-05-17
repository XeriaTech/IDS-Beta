print ("Booting up IlluminateOS...")

import itertools
import threading
import time
import sys

#Loading screen animation
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

from termcolor import colored, cprint
from Cryptodome.Hash import SHA3_512
import os
import threading

done = True


def timee():
  print (time.asctime( time.localtime(time.time()) ))


def clear():
  #Clear the terminal
  os.system('clear')


#The attestation station hashes the main.py file and checks that with the hash of the true file. If they don't match, it means that the os was edited and it shuts down. The process doesen't do anything right now, because when you develop the os it will change
import osapps.attestation
clear()

 
def calculator():
  import apps.calculator
          
def changecolors():
  print("You have a chance to change the heading color, your options are")#cprint these to the color that it is
  cprint ("Red", 'red')
  cprint ("Green", 'green')
  cprint ("Yellow", 'yellow')
  cprint ("Blue", 'blue')
  cprint ("White", 'white')
  print ("Note: The changes will only take place after you stop and start the repl\n")
  heading = input("What do you want the heading color to be?   ")
  if heading == 'red':
    f = open("colors.txt", 'w')
    f.write(heading)
    f.close() 
  elif heading == 'yellow':
    f = open("colors.txt", 'w')
    f.write(heading)
    f.close() 
  elif heading == 'green':
    f = open("colors.txt", 'w')
    f.write(heading)
    f.close() 
  elif heading == 'blue':
    f = open("colors.txt", 'w')
    f.write(heading)
    f.close() 
  elif heading == 'white':
    f = open("colors.txt", 'w')
    f.write(heading)   
    f.close() 
  
  else:
    import syscrash

  f = open("colors.txt", 'r')
  print ("Text color chnaged to", f.read())
  f.close()
  input("Press enter to continue   ")
  mainmenu()







def encryptos():
  print ("Encrypt the OS")
  cprint ("This action will render the entire OS unuseable if you forget the password. Do not use it lightly", 'red')
  print ("This feature is still a work in progress")
  mainmenu()



def unencryptednotes():
  import apps.unencryptednotes

def encryptednotes():
  import apps.encryptednotes

def changelockscreenpassword():
  #Lock screen settings
  cprint ("Lock screen settings", 'green')
  ytyvg = input("Do you want to \na) Change the password\nb) Change lock screen message\nc) Change the message to a failed password attampt\n")
  if ytyvg == 'a':
    qaqaqa = input("What's the current password?   ")
    
    h_obj = SHA3_512.new()
    h_obj.update(bytes(qaqaqa, 'utf-8'))
    kutck = (h_obj.hexdigest())

    g = open('codes.txt', 'r')
    gg = g.read()
    if gg != kutck:
      print ('Wrong password')
      g.close()
      exit()

    if gg == kutck:
      newpassword = input("What do you want the new password to be?   ")
      newpassword2 = input("Please type the new password again         ")
      h_obj = SHA3_512.new()
      h_obj.update(bytes(newpassword, 'utf-8'))
      nphash = (h_obj.hexdigest())

      h_obj = SHA3_512.new()
      h_obj.update(bytes(newpassword2, 'utf-8'))
      np2hash = (h_obj.hexdigest())
      
      if nphash != np2hash:
        print ("The two passwords are not the same")
        changelockscreenpassword()

      if nphash == np2hash:
        print ("The two passwords are the same")
        g = open('codes.txt', 'w')
        g.write(nphash)
        g.close()
        mainmenu()
      else:
        import syscrash
      g.close()    
      mainmenu()
    else:
      import syscrash

  if ytyvg == 'b':
    p = open('lockscreen.txt', 'r')
    print ('The current lock screen message is', p.read())
    p.close()
    wewewe = input("What do you want the new message to be?   ")

    p = open('lockscreen.txt', 'w')
    p.write(wewewe)
    p.close()
  if ytyvg == 'c':
    d = open("FailedLockScreenMessage.txt", 'w')
    ghvcew = input("What do you want the new message to be?   ")
    d.write(ghvcew)
    d.close()
    mainmenu()
  else:
    import syscrash

  
#A possible settings addition to chnage the color of printed text ,The text will be sperated into group sof 'body text', 'subtitle text', and 'title text'. Right now, I'm working on changing the text color when you ener a dangerous area such as settings. Dangerous areas will be red or orange, and non-dangerous areas will have a different color

f = open("colors.txt", 'r')
headcolor = (f.read())
f.close()

def settings():
  clear()
  cprint ("Settings", 'red', attrs=['bold'])
  choosesettings = input("a) Main Menu\nb) Lock Screen Settings\nc) Text Color\nd) Encrypt OS\n")
  if choosesettings == 'a':
    mainmenu()
  if choosesettings == 'd':
    encryptos()
  if choosesettings == 'b':
    changelockscreenpassword()
  if choosesettings == 'c':
    changecolors()

  else:
    import syscrash



def information():
  clear()
  cprint ("Information", (headcolor))
  print ("This is a rudementary os-type thing. It has preinstalled apps created by me. Most of them are privacy-security related, as that's what I'm into and what I have the most experience coding, but I will totally add other apps that other people write. Until I create a file and permission system, I won't be adding an official option to add apps. Enjoy! ")
  cwd = os.getcwd() 
  print("Current working directory:", cwd) 
  print(os.name)
  tyesxc = input("\nDo you want information about the different apps included in the os?  (y/n)   ")

  if tyesxc == 'y':
    print ("\npgp - https://en.wikipedia.org/wiki/Pretty_Good_Privacy\n")
    print ("AES- https://en.wikipedia.org/wiki/Aes256")
    print ("\nencryption - https://en.wikipedia.org/wiki/Encryption")
    print ("\npython - https://en.wikipedia.org/wiki/Python_(programming_language)")
    print ("\nhashing - https://en.wikipedia.org/wiki/Cryptographic_hash_function")
    print ("\nverified boot - https://source.android.com/security/verifiedboot")
    print ("\nos - https://en.wikipedia.org/wiki/Operating_system\n")
    input("Press enter when ready to proceed   ")
    mainmenu()


  if tyesxc == 'n':
    mainmenu()

  else:
    import syscrash

def firefox():
  import apps.firefox
 

cprint ("Welcome to IlluminateOS", 'green', attrs=['bold'])

def mainmenu():
  clear()
  timee()
  cprint ("Menu", (headcolor))
  menu = input("\na) Apps\nb) Information\nc) Settings\n")
  if menu == 'a':
    appmenu()
  if menu == 'b':
    information()
  if menu == 'c':
    settings()
  else:
    import syscrash


def appmenu():
  clear()
  cprint ("\nApps", (headcolor))
  chooseapp = input("a) Encryption Apps\nb) Games\nc) notes\nd) Encrypted Notes\ne) Files *Not working*\nf) Back to main menu\ng) Calculator\nh) Validate apps and os\ni) Google Search\nj) Firefox\n")
  if chooseapp == ('j'):
    firefox()
  if chooseapp == ("g"):
    calculator()
  if chooseapp == ('f'):
    mainmenu()
  if chooseapp == ('d'):
    encryptednotes()
  if chooseapp == ('c'):
    unencryptednotes()
  if chooseapp == ('e'):
    import fileacess
  if chooseapp == ('a'):
    chenap = input("\na) Hashing\nb) File Checksum\nc) PGP\nd) Text Encryption\n")
    if chenap == ('a'):
      import apps.encryptionapps.hashing
    if chenap == ('b'):
      import apps.encryptionapps.filecheck
    if chenap == ('c'):
      import apps.encryptionapps.pgp
    if chenap == ('d'):
      import apps.encryptionapps.textenc
    if chenap == ('e'):
      import apps.encryptionapps.steganography
    else:
      import syscrash
  if chooseapp == ('h'):
    import osapps.attest
  if chooseapp == ('i'):
    import apps.search
  if chooseapp == ('b'):
    yyeeet = input("\na) The Dark Castle\n")
    if yyeeet == 'a':
      import apps.games.darkcastle
    else:
      import syscrash
  else:
    import syscrash





#cprint("Hello", 'red')
#print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')

#for i in range(10):
#    cprint(i, 'magenta', end=' ')

#cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)


def lockscreen():
  #Lock screen
  timee()
  cprint ("Lock Screen", 'red')
  w = open('lockscreen.txt', 'r')
  print (w.read())
  w.close()
  
  ewvwv = input("What's the password?   ")

  h_obj = SHA3_512.new()
  h_obj.update(bytes(ewvwv, 'utf-8'))
  kutck = (h_obj.hexdigest())

  g = open('codes.txt', 'r')
  gg = g.read()
  if gg != kutck:
    w = open('FailedLockScreenMessage.txt', 'r')
    print (w.read())
    w.close()
    g.close()
    exit()

  if gg == kutck:
    print ("Password correct")
    g.close()
    os.system('clear') 
    mainmenu()


lockscreen()