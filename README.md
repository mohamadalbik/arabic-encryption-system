# Arabic Poetic Encryption System

A creative encryption and decryption system built with Python that transforms a regular Arabic message into a poem. Each letter of the original message is converted into a poetic line, and the final output is a complete poem based on a chosen category. The system also works in reverse — it can decrypt the poem back into the original message.

## Features

- Encrypt any Arabic message into a poem
- Decrypt the poem back to the original message
- Choose from multiple poem categories
- Poetic lines are intelligently mapped to letters
- Simple and clean GUI

## Screenshots

<img src = "https://github.com/mohamadalbik/arabic-encryption-system/blob/main/.screenshots/photo_1_2026-06-23_19-10-52.jpg" height = "300" width = "300">

<img src = "https://github.com/mohamadalbik/arabic-encryption-system/blob/main/.screenshots/photo_2_2026-06-23_19-10-52.jpg" height = "300" width = "300">

<img src = "https://github.com/mohamadalbik/arabic-encryption-system/blob/main/.screenshots/photo_3_2026-06-23_19-10-52.jpg" height = "300" width = "300">

## Technologies

- Python
- JSON (poem database)
- Web scraping for data collection
- AI-assisted data cleaning

## How to Run

### Prerequisites

- Python 3.7 or higher

### Run the Application

1. **Clone this repository:**
   ```
   git clone https://github.com/your-username/arabic-poetic-encryption.git
   cd arabic-poetic-encryption
   ```

2. **Run the application:**
   ```
   python main.py
   ```

## How It Works

### Encryption
1. Enter your message in the input field
2. Choose a poem category
3. The system maps each letter of your message to a poetic line from the database
4. The result is a complete poem that hides your original message

### Decryption
1. Paste the encrypted poem into the input field
2. The system reverses the mapping process
3. The original message is revealed

## Poem Database

The poem database was built using the following process:

1. **Data Collection** — Poems were gathered from Arabic poetry websites using a custom Python web scraping script
2. **Data Cleaning** — The collected poems were processed and cleaned using AI tools to make them usable by the system
3. **Data Organization** — The cleaned poems were structured into a JSON database, categorized and mapped to letters

## Project Structure

```
arabic-poetic-encryption/
├── main.py              # Main application with GUI
├── encrypt.py           # Encryption logic
├── decrypt.py           # Decryption logic
├── database/
│   └── poems.json       # Poem database
├── scraper/
│   └── poem_scraper.py  # Web scraping script
└── screenshots/         # Application screenshots
```

## Notes

- The system only supports Arabic text
- The quality of the generated poem depends on the richness of the database for the chosen category
- The poem database can be expanded by running the scraper script on additional sources

## About This Project

Built as a creative exploration of combining Arabic literature with encryption concepts. The project demonstrates skills in Python programming, data processing, web scraping, and creative problem-solving.
