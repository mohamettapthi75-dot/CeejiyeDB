# CeejiyeDB 🇸🇴

CeejiyeDB is a simple, Redis-inspired, in-memory database engine that uses Somali-style syntax called **CeejiyeLang**.

## Project Structure
- `main.py`: Interactive CLI interface.
- `parser.py`: Command tokenizer and parser.
- `storage.py`: In-memory storage with JSON persistence.
- `commands.py`: Command execution logic.
- `data.json`: Local database file.

## Commands (Amarrada)

- **KAYDI**: Saves a key-value pair.
  - Usage: `KAYDI <fure> <qiimo>`
  - Example: `KAYDI magac Ceejiye`

- **SOOQAAD**: Retrieves a value by its key.
  - Usage: `SOOQAAD <fure>`
  - Example: `SOOQAAD magac`

- **TIR**: Deletes a key from the database.
  - Usage: `TIR <fure>`
  - Example: `TIR magac`

- **DHAMAN**: Exits the database terminal.
  - Usage: `DHAMAN`

## How to Run
```bash
python3 ceejiyedb/main.py
```

## Internal Architecture
CeejiyeDB works by maintaining a Python dictionary in memory. Every time a `KAYDI` or `TIR` command is executed, the state is persisted to `data.json` to ensure data durability.
