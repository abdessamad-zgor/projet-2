import re
from os import system, name


def enter_hour(original=""):

    heure = input("Enter l'heure d'evenement (HH:MM) : "+original)
    if original != "" and heure == "":
        return ""
    while len(re.findall("\d{2}:\d{2}", heure)) == 0:
        print("Date invalide")
        heure = input("Enter l'heure d'evenement (HH:MM) : "+original)
    return heure


def leave_or_stay():
    ch = input('routornez au menu principale (y/n) :')
    if ch == 'y':
        print()
    else:
        raise KeyboardInterrupt


def enter_date(original=""):
    date = input("Enter la date d'evenement (JJ/MM/YYYY) : "+original)
    if original != "" and date == "":
        return ""
    while len(re.findall("\d{2}/\d{1,2}/\d{4}", date)) == 0:
        print("Date invalide")
        date = input("Enter la date d'evenement (JJ/MM/YYYY) : "+original)
    return date


def clear():
    system('clear' if name != "nt" else "cls")
