# NEEDED IMPORTS
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import ttkbootstrap as ttk
import random


# DEFINE GAME WINDOW
window=ttk.Window(themename='cerculean')
window.title("H4NG M4N")

# DEFINE LISTS
randoms = ["ABBREVIATED","ACCUSES","ALCOHOLICS","ANTHEM", "ANTISENSE", "APARTMENTS", "APPELLANT", "APPROPRIATED", "ARCHAEOLOGICAL","AVENGERS", "BANK", "HEAD","BROUGHT", "BULLET","BUTTON", "BUY","CELEBRATED","CLAPPING","CLIMB","COMMUNITIES","COMPLICATIONS", "COMPRESSING","DEFAMATION","DIRECTIVES", "DRAWER","EXHIBITS", "EYELINER","FLOWCHART","FRUIT","GRADES","HERB","IMPART", "INCOME", "INTEGRATES","JEWELERY", "LEARN", "LEGALLY", "LIPSTICK", "LOAN", "MARKET", "MONITOR","OBSERVATIONAL", "OUTAGE", "OVERRIDE", "PACK","PHANTOM", "PHOTONS","PROBABLY","PROGRAMMING","REDEMPTION", "REPORT", "RESSOURCES", "RETAIL", "REVEALED", "REVERT","SCHEMATIC", "SCREWS","SERIES", "SHIELD", "SHREDDED","SLEEP", "SPEARS", "SPONSORSHIP", "STEREOTYPES"]
countries = ["AFGHANSTAN","ALBANIA","ALGERIA","ARGENTINA","ARMENIA","AUSTRALIA","AUSTRIA","AZERBAIJAN","BAHRAIN","BANGLADESH","BELARUS","BELGIUM","BRAZIL","CAMEROON","CHILE","CHINA","COLOMBIA","CROATIA","DENMARK","EGYPT","FRANCE","Georgia","GERMANY","GREECE","HUNGARY","ICELAND","INDIA","IRAN","IRAQ","ITALY","JAPAN","JORDAN","KAZAKHSTAN","KENYA","KUWAIT","LEBANON","LITHUANIA","MALTA","MEXICO","MOROCCO","NEPAL","NETHERLANDS","NIGERIA","NORWAY","PAKISTAN","PALESTINE","PERU","PHILIPPINES","POLAND","PORTUGAL","QATAR","ROMANIA","RUSSIA","SERBIA","SINGAPORE","SLOVAKIA","SPAIN","SUDAN","SWEDEN","SWITZERLAND","SYRIA","TAIWAN","THAILAND","TUNISIA","TURKEY","UKRAINE","URUGUAY","VIETNAM","ZIMBABWE"]
cities = ["RIYADH", "KINGSTON","LONDON","SKOPJE", "MOSCOW","ZAGREB","BEIRUT","WARSAW","KRAKOW","PRAGUE", "SANTIAGO","BEIJING", "BANGKOK","BELGRADE", "AMMAN", "CAIRO","ATHENS", "JERUSALEM", "BRATISLAVA", "STOCKHOLM", "MADRID", "BARCELONA", "BUDAPEST", "DEBRECEN", "GETAFE", "BRNO", "VENICE", "MILAN", "ROME", "NAPOLI", "ARSENAL", "BRIGHTON", "AQABA", "BUCHAREST", "SZIGED", "ORADEA", "LISBON", "AMSTERDAM"]
companies = ["NVIDIA", "GOOGLE", "LINKEDIN", "VODAFONE", "APPLE", "ORANGE", "INTEL", "MICROSOFT", "HUAWEI", "MASTERCARD", "ADOBE", "CISCO", "PAYPAL", "VISA", "WALMART", "TESCO", "STARBUCKS", "AMAZON", "PEPSI", "NIKE", "ADDIDAS", "PUMA", "SAMSUNG", "VERIZON", "DISNEY", "FACEBOOK", "ALIBABA", "IBM", "ORACLE", "DELL", "NETFLIX", "PHILIPS", "BROWN", "XIAOMI", "EBAY", "TELENOR", "NINTENDO", "SONY", "TELKOM", "NOKIA", "ERICSSON"]

# DEFINE H4NGM4N ART ( PICS )
photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png")]

# METHOD: INTIATING A NEW GAME BY PASSING LIST TYPE PARAMETER TO GENERATE RANDOM WORD AND BLANKS WORDS
def newGame(wordList):
    optionsWindow.destroy()
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(wordList)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

# METHOD: HANDLING USER GUESS
def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<6:                                       # NUMBER OF LIVES
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):                           # CHECKING IF GUESSED LETTER IS CORRECT
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:          # HANDLING CASE WIN
                    messagebox.showinfo("H4NG M4N", "Congratulations, You Are Alive!") 
                    gameList()
        else:
                numberOfGuesses+=1                              # MISTAKES
                imgLabel.config(image=photos[numberOfGuesses])  # MISTAKES LOAD FOLLOWING H4NGM4N ART
                if numberOfGuesses==6:                          # HANDLING CASE LOSE
                 messagebox.showwarning("H4NG M4N", "x_x You Got H4NGED x_x\n            Try Again!")
    
# LABEL TO SHOW H4NGM4N ART
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

# DISPLAYING KEYBOARD OF UPPER_CHARS ON GAME WINDOW
lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

# NEW GAME BUTTON
Button(window, text="NEW\nGAME", command=lambda:gameList(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

# CHECKING WHICH LIST THE USER CHOOSE FROM OPTIONS WINDOW 
def callback(selected):
    if(selected=="Cities"):
        Button(optionsWindow, text="OK", command=lambda:newGame(cities),font=("Helvetica 10 bold")).grid(row=5, column=3 ,columnspan=6, pady=5, sticky="NSWE")
    elif(selected=="Companies"):
        Button(optionsWindow, text="OK", command=lambda:newGame(companies),font=("Helvetica 10 bold")).grid(row=5, column=3 ,columnspan=6, pady=5, sticky="NSWE")
    elif(selected=="Random"):
        Button(optionsWindow, text="OK", command=lambda:newGame(randoms),font=("Helvetica 10 bold")).grid(row=5, column=3 ,columnspan=6, pady=5, sticky="NSWE")
    elif(selected=="Countries"):
        Button(optionsWindow, text="OK", command=lambda:newGame(countries),font=("Helvetica 10 bold")).grid(row=5, column=3 ,columnspan=6, pady=5, sticky="NSWE")

# OPTIONS WINDOW TO MAKE USER CHOOSE FROM THE LISTS AVAILABLE
def gameList():
    global selected
    global optionsWindow
    optionsWindow = ttk.Window()
    optionsWindow.title("Categories")

    #style = ttk.Style(optionsWindow)
    #style.theme_use("breeze-dark")
    
    Label(optionsWindow, text="Choose A Category", font=("Helvetica 18")).grid(row=0, column=3, columnspan=6, padx=10)
    
    global variable
    variable = StringVar(optionsWindow)

    OptionMenu(optionsWindow, variable,"Countries", "Random", "Cities", "Companies", command=callback).grid(row=3, column=3, columnspan=6, padx=5)

    variable.set("Countries")
    optionsWindow.mainloop()
    
# INITILLAIZE H4NGM4N
gameList()
window.mainloop()