# Python-Password-Manager
A simple and easy to use password manager that runs out of python

To whom it may concern

This is a password manager type thing
Its simple
Its cool
Its easy

The general idea with this program was to have a simple and sleek solution for password managing. I didn't trust most current platforms since I'm not big on having my password stored on another person's server, so I kept these local (for now..).

Passwords you create will be stored in the password.txt file and randomly encrypted with the key "hidden" in the password. I don't know what kind of encryption you were expecting. If you need to reference your password, simply copy and paste it back into the program and it'll unencrypt. Anyone with half a brain can unencrypt it if they look at this project's code but it ***is*** better than storing it in plaintext.

NOTE: If there are any spaces within the encrypted password, ***do not remove them***. The way the "encryption" works is it chooses a random number between 1-9 and changes
all the characters accordingly. It's possibe that it may get changed into a space, so dont mess up your password.
