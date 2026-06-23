import random
import json
with open("database/verses_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

def get_first_arabic_letter(text):
    for char in text:
        if '\u0600' <= char <= '\u06FF' and char not in {
            '\u0640', '\u0650', '\u064E', '\u064F', '\u0651', '\u0652'}:
            return char
    return None  


def encrypt(message, category = "general"):
    encrypted = []
    for letter in message.strip():
        if letter not in db:
            continue
        verses = [verse for verse in db[letter] if category == "general"
                   or verse['category']==category]
        if not verses:
            continue
        chosen_verse = random.choice(verses)['verse'].strip()
        encrypted.append(chosen_verse)

    return '\n'.join(encrypted)

def format_as_poem(verses, verses_per_line=2):
    
    if isinstance(verses, str):
        verses = [v.strip() for v in verses.split('\n') if v.strip()]
    else:
        verses = [v.strip() for v in verses if v.strip()]
    poem_lines = []
    for i in range(0, len(verses), verses_per_line):
        current_verses = verses[i:i+verses_per_line]
        # Join pairs with double space
        if len(current_verses) == verses_per_line:
            line = "    ".join(current_verses)
        
        else:
            line = "\t\t"+ current_verses[0]
        poem_lines.append(line)

    return '\n'.join(poem_lines)

def encryption(message, category = "general", verses_per_line = 2):
    verses = encrypt(message, category)
    peom = format_as_poem(verses, verses_per_line)
    return peom

def decryption(poem):
    decrypted = []
    for line in poem.split('\n'):
        verses = line.split('    ') if '    ' in line else [line.strip()]
        for verse in verses:
            if not verse:
                continue
            
            for char in verse:
                if '\u0600' <= char <= '\u06FF' and char not in {
                    '\u0640', '\u0650', '\u064E', '\u064F', '\u0651', '\u0652'  # حركات
                }:
                    decrypted.append(char)
                    break
    return ''.join(decrypted)

MSG = "مرحبا"
ENCRYPTED = encryption(MSG)
DECTRYPTED = decryption(ENCRYPTED)

print(f"Original: {MSG}")
print(ENCRYPTED)
print(DECTRYPTED)
