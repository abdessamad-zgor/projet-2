import db
import art
from pick import pick
from utils import enter_hour, enter_date, leave_or_stay, clear

db.load_data()

choix=""

def handle_choice():
    global choix
    if choix=='1':
        clear()
        date = enter_date()
        heure = enter_hour()
        name = input("Entez le nom d'evenement : ")
        taches = []
        while True:
            try:
                tache = input(f"entrez une tache {len(taches)} (Ctrl+C pour quitez) : ")
                taches.append(tache)
            except KeyboardInterrupt:
                print()
                break;
        db.add_event(date, heure, name, taches)
        leave_or_stay()
    elif choix=='2':
        clear()
        option, index = pick(db.list_events(), "selectionez l'evenement a modifier (ENTRE): ", "=>")
        db.modify_event(option)
        leave_or_stay()
    elif choix=='3':
        clear()
        print("\t"+"\n\t".join(db.list_events()))
        leave_or_stay()
    elif choix=='4':
        clear()
        option, index = pick(db.list_events(), "selectionez l'evenement a supprimer (ENTRE):", "=>")
        db.delete_event(option)
        leave_or_stay()
    


def main():
    try:
        clear()
        global choix
        while True:
            clear()
            print(art.text2art("Menu"))
            print("""
            1-ajouter un evenement
            2-modifier un evenement
            3-voir les evenements
            4-supprimer un evenement
            """)
            choix=input("entez votre choix : ")
            handle_choice()
    except KeyboardInterrupt:
        print()
        print("enregister les changement au mémoire ...")
        db.commit_db_to_memory()
        exit(1)

main()