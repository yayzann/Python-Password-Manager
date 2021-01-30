##this is a password generator and encrypter
##also unencrypts passwords for reasons uknown
from time import sleep
from random import randint

print("""
 /$$     /$$                                    /$$                    /$$$$$$                                    /$$
|  $$   /$$/                                   | $/                   /$$__  $$                                  |__/
 \  $$ /$$/$$$$$$  /$$$$$$$$  /$$$$$$  /$$$$$$$|_//$$$$$$$           | $$  \ $$ /$$$$$$/$$$$   /$$$$$$  /$$$$$$$$ /$$ /$$$$$$$   /$$$$$$
  \  $$$$/____  $$|____ /$$/ |____  $$| $$__  $$ /$$_____/           | $$$$$$$$| $$_  $$_  $$ |____  $$|____ /$$/| $$| $$__  $$ /$$__  $$
   \  $$/ /$$$$$$$   /$$$$/   /$$$$$$$| $$  \ $$|  $$$$$$            | $$__  $$| $$ \ $$ \ $$  /$$$$$$$   /$$$$/ | $$| $$  \ $$| $$  \ $$
    | $$ /$$__  $$  /$$__/   /$$__  $$| $$  | $$ \____  $$           | $$  | $$| $$ | $$ | $$ /$$__  $$  /$$__/  | $$| $$  | $$| $$  | $$
    | $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$| $$  | $$ /$$$$$$$/           | $$  | $$| $$ | $$ | $$|  $$$$$$$ /$$$$$$$$| $$| $$  | $$|  $$$$$$$
    |__/ \_______/|________/ \_______/|__/  |__/|_______/            |__/  |__/|__/ |__/ |__/ \_______/|________/|__/|__/  |__/ \____  $$
 /$$$$$$$                                                                    /$$                                                /$$  \ $$
| $$__  $$                                                                  | $$                                               |  $$$$$$/
| $$  \ $$/$$$$$$   /$$$$$$$ /$$$$$$$ /$$  /$$  /$$  /$$$$$$   /$$$$$$  /$$$$$$$                                                \______/
| $$$$$$$/____  $$ /$$_____//$$_____/| $$ | $$ | $$ /$$__  $$ /$$__  $$/$$__  $$
| $$____/ /$$$$$$$|  $$$$$$|  $$$$$$ | $$ | $$ | $$| $$  \ $$| $$  \__/ $$  | $$
| $$     /$$__  $$ \____  $$\____  $$| $$ | $$ | $$| $$  | $$| $$     | $$  | $$
| $$    |  $$$$$$$ /$$$$$$$//$$$$$$$/|  $$$$$/$$$$/|  $$$$$$/| $$     |  $$$$$$$
|__/     \_______/|_______/|_______/  \_____/\___/  \______/ |__/      \_______/
  /$$$$$$                                                     /$$
 /$$__  $$                                                   | $$
| $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$
| $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$  | $$ /$$| $$  | $$| $$
|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$
 \______/  \_______/|__/  |__/ \_______/|__/      \_______/   \___/   \______/ |__/
                            """)

print("Initializing...")
sleep(.2)
print("...")
print("Loading Word-Lists...")
sleep(.2)
print("...")
##wordlist
words = ["elias", "john", "doe", "mr", "mustache", "jordan", "measure", "phone", "demon", "state", "irregular", "mouse",
         "gaming", "headset", "beats"
    , "hockey", "peepee", "siege", "certitude", "lamp", "light", "dark", "lightsaber", "starwars", "apple", "pen",
         "razor", "haze", "burial", "amazing", "penultimate",
         "incredible", "mongoose", "measurement", "computer", "linux", "debian", "manjaro", "overwatch", "hippopotamus",
         "hipocratic", "hypervigilant", "powercord", "notebook",
         "foldingchair", "operation", "superman", "dragon", "bermuda", "arbutus", "selkirk", "lawnmower", "eminem", "molly", "yeet"
         "stronk", "underground", "rubber", "candle", "laptop", "desktop", "water", "airpods", "lamp", "lottery", "mula", "cash", "henny",
         "smoke", "spot", "semi", "podracing", "homie", "ball", "astute", "wartime" ]

print("The wordlist currently has", (len(words)), "words and counting!")
print("Loading Password Maker...")
sleep(.2)
print("...")


##passwodgenerating
def capsSwitch(word, n):
    return word[:n].capitalize() + word[n:].capitalize()


pWord = 'n'


def wordScramble():
    pOne = words[randint(0, 52)]
    pOne = capsSwitch(pOne, 0)
    pTwo = words[randint(0, 52)]
    pTwo = capsSwitch(pTwo, 0)
    pWord = (pOne + pTwo)
    return pWord


pWord = wordScramble()


def extraChars():
    pNumber = (str(randint(0, 99))) + (str(randint(0, 99)))
    pC = randint(35, 38)
    pChar = chr(pC)
    eChars = pNumber + pChar
    return eChars


eChars = extraChars()
print("Loaded!")
pPhrase = str(pWord + eChars)
##print(type(pPhrase))
##encrypting
# lowerchar used in lowerString
xp = int(randint(0, 8))


# xz = randint(0,90)
def changeChar(char):
    return chr(ord(char) + xp)


# basically repeats lowerchar over the whole string
result = ""


def changeString(string):
    result = ""
    for i in range(0, len(string)):
        result = result + changeChar(string[i])
    return result


# def pEncrypt():
# changeString(pPhrase)
# print(result)
# print("You're encryption keys are:",xp)
# unencryption
def reverseChar(rChar):
    return chr(ord(rChar) + userKey)


resu = ""


def reverseString(string):
    resu = ""
    for i in range(0, len(string)):
        resu = resu + reverseChar(string[i])
    return resu


nu = input('Would you like to create a new password(n) or unencrypt a previous one(u)? ')

if nu.casefold() == 'n'.casefold():
    while True:
        passName = input("What is this password for?")
        print('Your\'re new password is:')
        print(pPhrase)
        print('encrypting...')
        sleep(.2)
        print('...')
        print('...')
        encryptedPP = changeString(pPhrase)
        print(encryptedPP)
        print("You're encryption key is:", xp,", and your password is for:",passName)
        continueN = input("Is this correct?(y/n): ")
        if continueN.casefold() == 'y'.casefold():
            break

    print("Converting to ASCII")
    encryptedPP.encode('utf-8')

    # yn = input('Do you have an existing password on file?(y/n): ')
    # if yn.casefold() == ('y'):
    # storedP = open("passlist.txt","a")
    # storedP.write(encryptedPP, xp)
    # elif yn.casefold() == ('n'):
    # storedP = open("passlist.txt","w")
    # storedP.write(encryptedPP)
    # storedP.write(xp)
    print('Writing to file...')
    storedP = open("password.txt", "a")
    xpString = str(xp)
    storedP.write("\n")
    storedP.write(passName+" = "+encryptedPP+xpString)
    sleep(.3)
    print('...')
    sleep(.2)
    print('....')
    print('.....')
    print('......')
    print('Done!')

elif nu.casefold() == 'u'.casefold():
    ##prePass = input("What is your encrypted password?: ")
    ##userKey = int(input("And what is your encryption key?: "))
    #prePass = input("What is your full encrypted password? (copy the line from password file): ")
    fetchPass = input("What's the name of your saved password?: ")
    search = open("password.txt")
    for line in search:
        if fetchPass in line:
            search = line
    passNum = len(fetchPass)
    passNum = int(passNum+3)
    ##test
    ##print(passNum)
    print("Checking Local Database...")
    sleep(.3)
    print("...")
    print("Done!")
    prePass = search[passNum:]
    prePass = str(prePass)
    userKey = prePass[len(prePass)-2]
    userKey = int(userKey)
    userKey = userKey * (-1)
    # uses previous functions but reversed to enencrypt
    unencryptedPP = reverseString(prePass)
    print('Your password is:',unencryptedPP)
