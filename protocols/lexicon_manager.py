import json
import os
from datetime import datetime

# Chemin vers ton dictionnaire sur ton dépôt MOC-G3C
DICTIONARY_FILE = 'protocols/dictionary.json'

def load_dict():
    """Charge le dictionnaire existant ou en crée un nouveau."""
    if not os.path.exists(DICTIONARY_FILE):
        return {}
    with open(DICTIONARY_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_term(term, definition, rationale):
    """Ajoute un terme s'il n'existe pas déjà (Immuabilité)."""
    data = load_dict()
    
    if term in data:
        print(f"\n[ERREUR] : Le terme '{term}' est immuable. Modification interdite par le protocole.")
        return

    data[term] = {
        "definition": definition,
        "rationale": rationale,
        "date_added": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "author": "MOC-G3C"
    }

    # Sauvegarde avec indentation pour la lisibilité sur GitHub
    with open(DICTIONARY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"\n[SUCCÈS] : '{term}' a été gravé avec succès dans l'Axe Hybride.")

if __name__ == "__main__":
    print("=== GESTIONNAIRE DU DICTIONNAIRE IMMUABLE (v1.0) ===")
    t = input("Terme à graver : ")
    d = input("Définition formelle : ")
    r = input("Justification (Rationale) : ")
    add_term(t, d, r)
