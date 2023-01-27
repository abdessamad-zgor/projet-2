from os.path import dirname
import re
from utils import enter_date, enter_hour

db = {}


def load_data():
    global db
    with open(dirname(__file__)+"/dbfile.txt") as f:
        lines = [l.strip() for l in f.readlines() if l != ""]
        for l in lines:
            segs = l.split(";")
            taches = [t.strip()
                      for t in segs[len(segs)-1].split("*") if t != ""]
            db[segs[0]] = {
                segs[1]: {
                    "titre": segs[2],
                    "taches": taches
                }
            }


def add_event(date, hour, name, taches):
    global db
    try:
        db[date][hour] = {
            "titre": name,
            "taches": taches
        }
    except KeyError:
        db[date] = {
            hour: {
                "titre": name,
                "taches": taches
            }
        }
    print(f"l'evenement {name} est ajouter au jour {date} a l'heure {hour}")


def modify_event(option):
    global db
    date = re.findall(".*(\d{2}/\d{1,2}/\d{4})", option)[0]
    hour = re.findall(".*(\d{2}:\d{2})", option)[0]
    event_original = db[date][hour]


    new_date = enter_date(f"(laissez vide pour preserver l'originale {date}) ")

    new_hour = enter_hour(f"(laissez vide pour preserver l'originale {hour}) ")

    new_name = input(
        f"Entez le nom de l'evenement : (laissez vide pour preserver l'originale {db[date][hour]['titre']}) ")
    new_taches = []
    taches_orig = event_original['taches']
    while True:
        try:
            orginal_val = "(laissez vide pour preserver l'originale"+taches_orig[len(new_taches)]+")" if len(taches_orig)>len(new_taches) else ''
            tache = input(
                f"entrez une tache {len(new_taches)} (Ctrl+C pour quitez) : {orginal_val}")
            if tache=="":
                if len(taches_orig)<=len(new_taches):
                    continue;
                else :
                    new_taches.append(taches_orig[len(new_taches)+1])
            else:
                new_taches.append(tache)
            
        except KeyboardInterrupt:
            print()
            break
    if (new_date !="" and new_date != date) or (new_hour !="" and new_hour != hour):
        del db[date][hour]
    
    try:
        db[new_date if new_date!="" else date][new_hour if new_date!="" else hour] = {
            "titre": new_name if new_name!="" else event_original["titre"],
            "taches": new_taches
        }
    except KeyError:
        db[new_date if new_date!="" else date] = {
            new_hour if new_date!="" else hour: {
                "titre": new_name  if new_name!="" else event_original["titre"],
                "taches": new_taches
            }
        }
    print(
        f"l'evenement {new_name} au jour {new_date if new_date!='' else date} a l'heure {new_hour if new_date!='' else hour} est modifie")


def delete_event(option):
    global db
    date = re.findall(".*(\d{2}/\d{1,2}/\d{4})", option)[0]
    hour = re.findall(".*(\d{2}:\d{2})", option)[0]
    del db[date][hour]


def list_events():
    global db
    events = []
    for date, h in db.items():
        for hour, ev in h.items():
            events.append("Date : "+date+"; Heure : "+hour +
                          "; Nom d'evenement : "+ev["titre"])
    return events


def commit_db_to_memory():
    global db
    events = []
    for date, h in db.items():
        for hour, ev in h.items():
            events.append(date+";"+hour + ";" +
                          ev["titre"]+";"+"*".join(ev["taches"]))
    with open(dirname(__file__)+"/dbfile.txt", "w") as f:
        f.write("\n".join(events))
