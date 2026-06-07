<div align="center">

# 🗄️ CeejiyeDB

### *Xogta Soomaalida — The Somali Database Engine*



![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)




![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)




![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)




![Language](https://img.shields.io/badge/Language-Somali-blue?style=for-the-badge)



**CeejiyeDB** waa engine database oo Python ku dhisan, Redis u eg, laakiin amarrada **Af-Soomaali** ku hadla — CeejiyeLang.

[🚀 Bilow Hadda](#-sida-loo-isticmaalo) · [📖 Amarrada](#-amarrada-ceejiiyelang) · [🏗️ Qaab-dhismeedka](#%EF%B8%8F-qaab-dhismeedka)

</div>

---

## ✨ Maxay CeejiyeDB Gaara Tahay?

- 🇸🇴 **Af-Soomaali** — Amarrada oo dhan Soomaali
- ⚡ **Xawli sarreeya** — In-memory storage, Redis u eg
- 💾 **Xog la badbaadin karo** — JSON persistence toos ah
- 🛡️ **Ammaan** — Error handling buuxa
- 🧩 **Fudud** — Akhrin, baranba fudud

---

## 🚀 Sida Loo Isticmaalo

### 1. Ku keen mashiinkaaga
```bash
git clone https://github.com/mohamettapthi75-dot/CeejiyeDB.git
cd CeejiyeDB
```

### 2. Bilow
```bash
python3 ceejiyedb/main.py
```

### 3. Bilaabis
```text
╔══════════════════════════════╗
║     CeejiyeDB v1.1.0  🇸🇴   ║
║  Xogta Soomaalida, Xoogga   ║
╚══════════════════════════════╝
Ku soo dhawoow CeejiyeDB. Qor CAAWI si aad amarrada u aragto.
```

## 📖 Amarrada CeejiyeLang

| Amar | Isticmaalka | Tusaale | Macnaha |
| :--- | :--- | :--- | :--- |
| **KAYDI** | `KAYDI <fur> <qii>` | `KAYDI magac Ceejiye` | Keydi qiime |
| **SOOQAAD** | `SOOQAAD <fur>` | `SOOQAAD magac` | Soo qaad qiime |
| **TIR** | `TIR <fur>` | `TIR magac` | Tir fur |
| **CUSB** | `CUSB <fur> <qii>` | `CUSB magac Fadumo` | Cusboonaysii qiime |
| **TIJAABO** | `TIJAABO <fur>` | `TIJAABO magac` | Hubi in fur jiro |
| **LIIS** | `LIIS` | `LIIS` | Tus dhammaan furahaaga |
| **TIRI** | `TIRI` | `TIRI` | Tiri furaha |
| **NADIIFI** | `NADIIFI` | `NADIIFI` | Nadiifi xog oo dhan |
| **CAAWI** | `CAAWI` | `CAAWI` | Tus amarrada oo dhan |
| **DHAMAN** | `DHAMAN` | `DHAMAN` | Ka bax |

---

## 🏗️ Qaab-dhismeedka
```text
CeejiyeDB/
├── ceejiyedb/
│   ├── main.py        # CLI interface + banner + CAAWI
│   ├── parser.py      # Command tokenizer iyo parser
│   ├── storage.py     # In-memory store + JSON persistence
│   └── commands.py    # Fulinta amarrada oo dhan
├── data.json          # Database file (auto-created)
├── .gitignore
└── README.md
```

## ⚙️ Sida Gudaha u Shaqeyso
Isticmaalaha → **main.py** → **parser.py** → **commands.py** → **storage.py** → **data.json**

- **parser.py** — Amarku wuu kala gooyo token-ka
- **commands.py** — Amarka wuu fuliyo
- **storage.py** — Xogta wuu keydiyo (memory + JSON)

---

## 🗺️ Mustaqbalka (Roadmap)
- [ ] **MUDDAD** — TTL / key expiry
- [ ] **KOOB** — Integer increment
- [ ] **CeejiyeLang SDK** (Python package)
- [ ] **TCP server** (run as daemon)
- [ ] **Web dashboard**

## 📄 Ruqsadda
MIT License © 2025 mohamettapthi75-dot

---

**CeejiyeDB — Af-Soomaali, Xoog Buuxa 🇸🇴**
CeejiyeDB 🇸🇴
CeejiyeDB is a simple, Redis-inspired, in-memory database engine that uses Somali-style syntax called CeejiyeLang.

Project Structure
main.py: Interactive CLI interface.
parser.py: Command tokenizer and parser.
storage.py: In-memory storage with JSON persistence.
commands.py: Command execution logic.
data.json: Local database file.
Commands (Amarrada)
KAYDI: Saves a key-value pair.

Usage: KAYDI <fure> <qiimo>
Example: KAYDI magac Ceejiye
SOOQAAD: Retrieves a value by its key.

Usage: SOOQAAD <fure>
Example: SOOQAAD magac
TIR: Deletes a key from the database.

Usage: TIR <fure>
Example: TIR magac
DHAMAN: Exits the database terminal.

Usage: DHAMAN
How to Run
python3 ceejiyedb/main.py
Internal Architecture
CeejiyeDB works by maintaining a Python dictionary in memory. Every time a KAYDI or TIR command is executed, the state is persisted to data.json to ensure data durability.
