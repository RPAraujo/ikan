import requests
import yaml
import glob

def create_deck(deck_name):
    url = "http://localhost:8765"
    payload = {
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": deck_name
        }
    }
    requests.post(url, json=payload)

def add_card(deck_name, front, back, tags):
    create_deck(deck_name)  # Ensure the deck exists or create it
    url = "http://localhost:8765"
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back,
                },
                "tags": tags
            }
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

def find_cards(query):
    url = "http://localhost:8765"
    payload = {
        "action": "findNotes",
        "version": 6,
        "params": {
            "query": query
        }
    }
    response = requests.post(url, json=payload)
    return response.json().get('result', [])

def update_card(note_id, front, back):
    url = "http://localhost:8765"
    payload = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": note_id,
                "fields": {
                    "Front": front,
                    "Back": back
                }
            }
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

def delete_card(note_id):
    url = "http://localhost:8765"
    payload = {
        "action": "deleteNotes",
        "version": 6,
        "params": {
            "notes": note_id
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

# Process all YAML files within the 'decks' directory and its subdirectories
for filename in glob.glob('decks/**/*.yaml', recursive=True):
    with open(filename, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            deck_name = data.get('deck')
            tags = data.get('tags', [])
            for card in data['cards']:
                if card.get('delete', False):
                    # Handle delete
                    query = f"deck:\"{deck_name}\" \"front:{card['front']}\""
                    note_id = find_cards(query)
                    if note_id:
                        print(f"Deleting card with ID {note_id}")
                        delete_result = delete_card(note_id)
                        print(delete_result)
                elif card.get('update', False):
                    # Handle update
                    query = f"deck:\"{deck_name}\" \"front:{card['front']}\""
                    note_id = find_cards(query)
                    if note_id:
                        print(note_id[0])
                        update_result = update_card(note_id[0], card['front'], card['back'])
                        print(f"Updated note {note_id}: {update_result}")
                else:
                    # Otherwise, try to add the card as usual
                    result = add_card(deck_name, card['front'], card['back'], tags)
                    print(f"Added card to {deck_name} deck: {result}")
        except yaml.YAMLError as exc:
            print(exc)
