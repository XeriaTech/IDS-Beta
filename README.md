# IlluminateOS
This is a rudimentary os-type thing. It has preinstalled apps created by me. Most of them are privacy-security related, as that's what I'm into and what I have the most experience coding, but I will totally add other apps that other people write. 

Until I create a file and permission system, I won't be adding an official option to add apps. Enjoy! 

## Features

1. Fully functioning Firefox

2. PGP generation, encryption, and decryption

3. Verified boot on start of OS (Attestation)

4. Encrypted (AES-256) and unencrypted notes

5. Google Search

6. Simple Calculator

7. Hashing machine

8. File checksum machine

9. Simple AES-256 text encryption

10. Lock screen with options to change the password

11. Open-source

12. No tracking

13. A developer ready to listen to ideas and add others' programs into the OS

14. Simple single-letter commands

## Todo

#### Overall Todo

1. Sandboxing

2. Apps permissions

3. Gui?

4. ~~Add wikipedia page/information on different tools (such as pgp)~~

5. Encrypt OS

6. WebView (https://pypi.org/project/pywebview/)

7. Move some encryption apps to a 'communication' folder

8. ~~Clear terminal using os.system('clear') after choices~~

9. ~~Add different color text for different threat levels of current options~~

10. Add different settings page for different users

11. Switch from cryptocode to cryptodome chacha20

12. ~~Add clock at the home screen~~

13. After leaving an app, go to main menu, not lock screen

14. Add an option to have a single command that can be used amytime a choice is given to go back to the main menu (add settings to choose?)

16. ~~Add a library of online privacy infographics and guides (Surveillence Self Defense, Hitchhiker's guide to anonymity, )~~

17. Change text to colors with attributes

#### Small Todo

1. ~~Add option for choosing pgp keys~~

2. Add encryption options with different ciphers

4. ~~Make firefox work~~

5. Make it pip install ~~pycryptodome~~ and cryptocode automaticaly

6. ~~Add lock screen~~
  
  a. When a predetermined code is put in, wipe os

  b. When os is booted, have programs authenticate that lock screen is unlocked

7. ~~Add different algorithms to the file checksum~~

8. ~~Add 'saved as... (file)' after encrypting text in pgp~~

9. Add option to go back to app list after choosing 'encryption apps'

10. ~~Add different size keys for pgp~~


12. Move the 'back to main menu' option to the end of the options in app list

 
14. Add option to hash or not hash the title of encrypted notes

15. Warning when generating  new pgp key will overwrite an already name pgp key woth the same name

16. Add animation when loading (generating pgp keys)

17. When terminating process in when two generated pgp keys ahve the same name, make it so you can go back to pgp without it dying

19. Read all notes available in notes app

20. Create ability to edit notes

21. Add in settings an option to choose a different message in response to a wrong inputted password

22. ~~Add a message to the lock screen~~

23. Add option to disable lock screen

24. Add text color options in the settings

25. Add option to chnage/disable loading animation

26. Make clock accurate

27. Seperate lock screen from home screen so when exiting apps, go to home screen instead

28. Make home screen more graphical


#### Apps to add

1. Stenography

2. Keepass

3. Chat

4. 


#### Need help with

1. Reading files in folders 

## Methodology
The main.py file is just the home screen. It boots, shows a lockscreen, and gives a directory to other py files. The apps are ran as different py files. This makes it simpler to read the main.py file, and allows more flexibility on variables and naming in the code

Lots of other semi-OSs on replit have a loading screen, but it loads for a predetermined time and in the end wastes time. I've improved on the design and made it so when the packages are loaded, 'done' is set to true, and the loading animation stops



## Changelog


1.0.7- Added the option to change heading text color, made system error page colorful

1.0.6- Added an error screen (blue screen of death) whenever an unrecognized input is given and restarts

1.0.5- Added Dark Castle text game (Thanks TechTimmyD!)

1.0.4- Added option to change message to failed password attempt, clears terminal after opening an app

1.0.3- If os is modified, exit and erase lock screen password, main.py, private.pem, and codes.txt

1.0.2- Added option to change lock screen message, screen now clears after booting (erasing 'Booting up IlluminateOS...' and if edited, 'Os shutting down...'), added loading animation

1.0.1- Added privacy guides 

1.0.0- Initial release

