# CeejiyeDB 🇸🇴

CeejiyeDB waa keyd xogeed (database) fudud oo loo dhisay si la mid ah Redis, balse isticmaala afka Soomaaliga (**CeejiyeLang syntax**). Mashruucan waxaa loo sameeyay si loogu fududeeyo barashada dhismaha database-yada iyo isticmaalka luuqad barnaamijyadeed oo Soomaali ah.

---

## ✨ Astaamaha (Features)

- **In-memory Storage:** Xogta waxaa lagu hayaa RAM-ka si ay u noqoto mid aad u dhakhso badan.
- **Persistence:** Xogta si toos ah ayaa loogu kaydiyaa faylka `data.json` si aysan u lumin marka barnaamijka la xiro.
- **Somali Commands:** Dhammaan amarrada lagu maamulo database-ka waa af-Soomaali.
- **Colored CLI:** Interface midabo leh oo ku tusaya guusha ama khalaadka dhaca.
- **Modular Design:** Habdhismeed nadiif ah oo loo qaybiyay qaybo kala duwan (Parser, Storage, Commands).

---

## 🚀 Sida loo bilaabo (Getting Started)

### Shuruudaha
Waxaad u baahan tahay oo kaliya **Python 3.x**.

### Sida loo orodka (Run)
Isticmaal amarkan si aad u bilawdo database-ka:
```bash
python3 ceejiyedb/main.py
```

---

## 🛠 Amarrada (Commands)

CeejiyeDB waxay taageertaa amarradan soo socda:

1. **KAYDI**: Waxaa loo isticmaalaa in xog lagu kaydiyo.
   - *Habka:* `KAYDI <fure> <qiimo>`
   - *Tusaale:* `KAYDI magac Ceejiye`

2. **SOOQAAD**: Waxaa loo isticmaalaa in xog horay u kaydsanayd la soo saaro.
   - *Habka:* `SOOQAAD <fure>`
   - *Tusaale:* `SOOQAAD magac`

3. **TIR**: Waxaa loo isticmaalaa in xogta lagu tirtiro.
   - *Habka:* `TIR <fure>`
   - *Tusaale:* `TIR magac`

4. **DHAMAN**: Waxaa loo isticmaalaa in laga baxo (exit) barnaamijka.
   - *Habka:* `DHAMAN`

---

## 📁 Habdhismeedka Mashruuca (Project Structure)

```text
ceejiyedb/
 ├── main.py        # CLI-ga iyo isku xirka barnaamijka
 ├── parser.py      # Kala dhig-dhigga amarrada Soomaaliga ah
 ├── storage.py     # Maamulka xogta ee RAM-ka iyo faylka JSON
 ├── commands.py    # Fulinta amarrada (Logic)
 └── data.json      # Halka xogtu ku kaydsantahay (Persistence)
```

---

## 👨‍💻 Horumarinta Mustaqbalka (Future Roadmap)
- [ ] Taageerada **EXPIRE** (Xogta oo waqti kadib is tirtirta).
- [ ] Isku xirka **TCP Server** (Si database-ka meel fog looga soo galo).
- [ ] Taageerada **Data Types** kale sida Lists iyo Hashes.

---

**CeejiyeDB** waa qayb ka mid ah dadaallada lagu horumarinayo agabka software-ka ee ku baxa Af-Soomaaliga. Ku raaxayso! 🚀
