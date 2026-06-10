# CeejiyeDB 🇸🇴 v1.2.0

CeejiyeDB waa keyd xogeed (database) fudud oo loo dhisay si la mid ah Redis, balse isticmaala afka Soomaaliga (**CeejiyeLang syntax**).

---

## ✨ Astaamaha Cusub (v1.2.0)

- ⏳ **MUDDAD (TTL):** Xogta hadda waxaa loo samayn karaa waqti ay ku dhacayso.
- 🔢 **Atomic Ops:** Amarrada `KOOB` iyo `DHIMIS` ee loogu talagalay tiriye-yaasha (counters).
- 📊 **XAALAD:** Tusmooyinka database-ka sida tirada furayaasha iyo xajmiga RAM-ka.
- 🧹 **Auto-Purge:** Database-ka si toos ah ayuu isaga nadiifiyaa xogta dhacday.

---

## 🛠 Amarrada (Commands)

| Amar | Isticmaalka | Macnaha |
| :--- | :--- | :--- |
| **KAYDI** | `KAYDI <fure> <qiimo>` | Keydi xog cusub |
| **SOOQAAD** | `SOOQAAD <fure>` | Soo saar xog kaydsan |
| **TIR** | `TIR <fure>` | Tirtir xogta |
| **MUDDAD** | `MUDDAD <fure> <ilb>` | Set TTL (Time To Live) |
| **KOOB** | `KOOB <fure>` | Kordhi tiro (Increment) |
| **DHIMIS** | `DHIMIS <fure>` | Dhim tiro (Decrement) |
| **XAALAD** | `XAALAD` | Tus xaaladda database-ka |
| **CAAWI** | `CAAWI` | Tus amarrada oo dhan |
| **DHAMAN** | `DHAMAN` | Ka bax barnaamijka |

---

## 🚀 Sida loo bilaabo (Getting Started)

### Sida loo orodka (Run)
```bash
python3 ceejiyedb/main.py
```

### Orodka Tijaabada (Tests)
```bash
python3 tests/test_v1_2.py
```

---

## 🗺️ Roadmap (Mustaqbalka)
- [ ] v2.0: Rust Core Engine (Performance)
- [ ] v2.0: TCP Server Support
- [ ] v2.0: Python SDK & REST API
- [ ] v2.0: Web Dashboard

---

**CeejiyeDB** — Af-Soomaali, Fudud, iyo Xooggan. 🚀
