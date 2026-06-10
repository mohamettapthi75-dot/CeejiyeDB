<div align="center">

# 🗄️ CeejiyeDB (Rust + Python Hybrid)

### *Xogta Soomaalida — The Somali Database Engine*

![Rust](https://img.shields.io/badge/Rust-1.70+-orange?style=for-the-badge&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

**CeejiyeDB** waa engine database oo isku darsaday awoodda **Rust** (core engine) iyo dabacsanaanta **Python** (CLI, SDK, & API).

</div>

---

## 🏗️ Architecture
```text
┌────────────────┐      ┌─────────────────────┐      ┌──────────────┐
│  Python CLI    │ ───► │   PyO3 Bindings     │ ───► │  Rust Core   │
│  (ceejiyedb)   │      │   (ceejiye_core)    │      │  (storage)   │
└────────────────┘      └─────────────────────┘      └──────────────┘
                                  │                          │
                                  ▼                          ▼
                        ┌─────────────────────┐      ┌──────────────┐
                        │  Async TCP Server   │      │  Persistence │
                        │  (Tokio - 7379)     │      │  (JSON/WAL)  │
                        └─────────────────────┘      └──────────────┘
                                  │
                                  ▼
                        ┌─────────────────────┐
                        │  FastAPI REST API   │ (Port 8000)
                        │  (ceejiyedb/api.py) │
                        └─────────────────────┘
```

---

## ⚡ Build & Install

```bash
# Install maturin
pip install maturin

# Build and install locally
maturin build --release
pip install core/target/wheels/*.whl
```

---

## 🚀 Sida Loo Isticmaalo

### CLI Terminal
```bash
python3 ceejiyedb/main.py
```

### REST API
```bash
uvicorn ceejiyedb.api:app --reload
```

---

## 📖 Amarrada CeejiyeLang

| Amar | Isticmaalka | Macnaha |
| :--- | :--- | :--- |
| **KAYDI** | `KAYDI fure qiime` | Keydi xogta |
| **SOOQAAD** | `SOOQAAD fure` | Soo qaad xogta |
| **TIR** | `TIR fure` | Tirtir xogta |
| **MUDDAD** | `MUDDAD fure 60` | TTL - Waqti kadib tirtir |
| **KOOB** | `KOOB tiriye` | Kordhi tiro |
| **DHIMIS** | `DHIMIS tiriye` | Ka dhim tiro |
| **XAALAD** | `XAALAD` | Xaaladda database-ka |

---

## ⚙️ Requirements
- Rust 1.70+
- Python 3.12+
- Maturin
- FastAPI & Uvicorn

---

**CeejiyeDB — Af-Soomaali, Awood Rust 🦀**
