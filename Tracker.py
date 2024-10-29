#Dave.py

##########################################
# Background Color = \x1b[38:5:86m       #
# Text Color = \x1b[38:5:91m             #
# Number Text Color = \x1b[38:5:120m     #
# Quit Txt Color = \x1b[38:5:196m        #
# Typing Color = \x1b[38:5:231m          #
##########################################

import calendar
import os
import time

def clear():
    if os.name == 'nt':  
        os.system('cls')
    else:
        os.system('clear')

def allcalendar():
    print(f"""
    \x1b[38:5:86m╔═════════════════════════════════════╗
    \x1b[38:5:86m║     \x1b[38:5:91mSmart Calendar \x1b[38:5:120m& \x1b[38:5:91mAge Tracker    \x1b[38:5:86m║  
    \x1b[38:5:86m╚═════════════════════════════════════╝""")
    year = int(input("     \x1b[38:5:120mEnter year calendar:\x1b[38:5:231m "))
    time.sleep(1.5)
    clear()
    print(f"""
\x1b[38:5:86m═════════════════╦═════════════════════════════════════╦════════════════════════════════
                 \x1b[38:5:86m║           \x1b[38:5:91mCALENDAR RESULT           \x1b[38:5:86m║   
\x1b[38:5:86m═════════════════╩═════════════════════════════════════╩════════════════════════════════\x1b[38:5:231m""")
    print(calendar.TextCalendar().formatyear(year))
    print("\x1b[38:5:86m════════════════════════════════════════════════════════════════════════════════════════")
    choice = input("\x1b[38:5:196mPress Enter to Go Back:\x1b[38:5:231m ")
    time.sleep(1.5)
    clear()
    main()

def monthcalendar():
    print(f"""
    \x1b[38:5:86m╔═════════════════════════════════════╗
    \x1b[38:5:86m║     \x1b[38:5:91mSmart Calendar \x1b[38:5:120m& \x1b[38:5:91mAge Tracker    \x1b[38:5:86m║ 
    \x1b[38:5:86m╚═════════════════════════════════════╝""")
    year1 = int(input("     \x1b[38:5:120mEnter year calendar:\x1b[38:5:231m "))
    month1 = int(input("     \x1b[38:5:120mEnter No. month calendar:\x1b[38:5:231m "))
    time.sleep(1.5)
    clear()
    print(f"""
\x1b[38:5:86m═══════════════════════════╗
\x1b[38:5:91m   CALENDAR MONTH RESULT   \x1b[38:5:86m║   
\x1b[38:5:86m═══════════════════════════╝\x1b[38:5:231m""")
    print(calendar.month(year1, month1))
    print("\x1b[38:5:86m════════════════════════════\x1b[38:5:231m")
    choice = input("\x1b[38:5:196mPress Enter to Go Back:\x1b[38:5:231m ")
    time.sleep(1.5)
    clear()
    main()

def age():
    global year, birth, result
    print(f"""
    \x1b[38:5:86m╔═════════════════════════════════════╗
    \x1b[38;5;86m║        \x1b[38:5:91mWelcome to Age Tracker       \x1b[38;5;86m║ 
    \x1b[38:5:86m╚═════════════════════════════════════╝""")
    year = int(input("     \x1b[38:5:120mEnter Year of Today:\x1b[38:5:231m "))
    birth = int(input("     \x1b[38:5:120mEnter your Birthyear:\x1b[38:5:231m "))
    result = year - birth
    time.sleep(1.5)
    clear()
    age_result()

def age_result():
    print(f"""
    \x1b[38:5:86m╔═════════════════════════════════════╗
    \x1b[38;5;86m║          \x1b[38:5:91mAge Tracker Result         \x1b[38;5;86m║ 
    \x1b[38:5:86m╚═════╦═════════════════════════╦═════╝
    \x1b[38:5:86m   ╔══╩═════════════════════════╩══╗
    \x1b[38:5:86m   ║                               ║
    \x1b[38:5:86m   ║     \x1b[38:5:120mYour Birthyear: \x1b[38:5:231m{birth:<10}\x1b[38;5;86m║
    \x1b[38:5:86m   ║                               ║
    \x1b[38:5:86m   ║     \x1b[38:5:120mYour age: \x1b[38:5:231m{result:<10}      \x1b[38;5;86m║
    \x1b[38:5:86m   ║                               ║
    \x1b[38:5:86m   ╚═══════════════════════════════╝""")
    choice = input("        \x1b[38:5:196mPress Enter to Go Back:\x1b[38:5:231m ")
    time.sleep(1.5)
    clear()
    main()

def main():
    clear()
    print(f""" 
    \x1b[38:5:86m╔══════════════════════════════════╗
    \x1b[38:5:86m║   \x1b[38:5:91mSmart Calendar \x1b[38:5:120m& \x1b[38:5:91mAge Tracker   \x1b[38:5:86m║   
    \x1b[38:5:86m╠══════════════════════════════════╣
    \x1b[38:5:86m║                                  \x1b[38:5:86m║          
    \x1b[38:5:86m║      \x1b[38:5:120m1. Calendar                 \x1b[38:5:86m║
    \x1b[38:5:86m║                                  \x1b[38:5:86m║
    \x1b[38:5:86m║      \x1b[38:5:120m2. Month Calendar           \x1b[38:5:86m║
    \x1b[38:5:86m║                                  \x1b[38:5:86m║   
    \x1b[38:5:86m║      \x1b[38:5:120m3. Age Tracker              \x1b[38:5:86m║
    \x1b[38:5:86m║                                  \x1b[38:5:86m║
    \x1b[38:5:86m║      \x1b[38:5:120m0. \x1b[38:5:196mExit                     \x1b[38:5:86m║
    \x1b[38:5:86m║                                  \x1b[38:5:86m║  
    \x1b[38:5:86m╠══════════════════════════════════╝""")
    choice = int(input("    ╚═> \x1b[38:5:120mChoice:\x1b[38:5:231m "))
    clear()

    if choice == 1:
        allcalendar()
    elif choice == 2:
        monthcalendar()
    elif choice == 3:
        age()
    elif choice == 0:
        clear()
        print(""" 
        \x1b[38:5:86m╔═══════════════════════════════════╗
        \x1b[38:5:86m║     \x1b[38:5:91mThank you visitors \x1b[38:5:196m<3\x1b[38:5:91m...      \x1b[38:5:86m║
        \x1b[38:5:86m╚═══════════════════════════════════╝""")
        time.sleep(1)
        quit()

main()
