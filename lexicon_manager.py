import json
import os
from datetime import datetime

DICTIONARY_FILE = 'protocols/dictionary.json'

def load_dict():
    if not os.path.exists(DICTIONARY_FILE):
        return {}
    with open(DICTIONARY_FILE, 'r') as f:
        return json.load(f)

def add_term(term, definition, rationale):
    data = load_dict()
    
    if term in data:
        print(f"ERREUR : Le terme '{term}' est immuable. Modification interdite.")
        return

    data[term] = {
        "definition": definition,
        "rationale": rationale,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "author": "MOC-G3C"
    }

    with open(DICTIONARY_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"SUCCÈS : '{term}' a été gravé dans le dictionnaire.")

# Exemple d'utilisation
if __name__ == "__main__":
    print("--- Gestionnaire du Dictionnaire Immuable ---")
    terme = input("Nom du terme : ")
    def_text = input("Définition : ")
    justification = input("Justification (Rationale) : ")
    add_term(terme, def_text, justification)
