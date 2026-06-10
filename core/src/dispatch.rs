use std::sync::{Arc, Mutex};
use crate::storage::Storage;
use crate::types::CeejiyeValue;

pub fn dispatch_command(storage: &Arc<Mutex<Storage>>, request: &str) -> String {
    let parts: Vec<&str> = request.split_whitespace().collect();
    if parts.is_empty() {
        return "ERROR: Amarka ma furna.\n".to_string();
    }

    let command = parts[0].to_uppercase();
    let args = &parts[1..];

    let mut db = storage.lock().unwrap();

    match command.as_str() {
        "KAYDI" => {
            if args.len() < 2 {
                "ERROR: KAYDI <fur> <qii>\n".to_string()
            } else {
                let key = args[0].to_string();
                let value = args[1..].join(" ");
                db.set(key.clone(), CeejiyeValue::Qoraal(value));
                format!("SUCCESS: '{key}' waa la kaydiyay.\n")
            }
        }
        "SOOQAAD" => {
            if args.is_empty() {
                "ERROR: SOOQAAD <fur>\n".to_string()
            } else {
                match db.get(args[0]) {
                    Some(CeejiyeValue::Qoraal(s)) => format!("{s}\n"),
                    Some(CeejiyeValue::Tiro(n)) => format!("{n}\n"),
                    Some(CeejiyeValue::Liis(l)) => format!("{:?}\n", l),
                    Some(CeejiyeValue::Set(s)) => format!("{:?}\n", s),
                    Some(CeejiyeValue::Hash(h)) => format!("{:?}\n", h),
                    None => "ERROR: Furaha lama helin.\n".to_string(),
                }
            }
        }
        "TIR" => {
            if args.is_empty() {
                "ERROR: TIR <fur>\n".to_string()
            } else if db.delete(args[0]) {
                format!("SUCCESS: '{}' waa la tiray.\n", args[0])
            } else {
                "ERROR: Furaha lama helin.\n".to_string()
            }
        }
        "LIIS" => {
            let keys = db.get_all_keys();
            if keys.is_empty() {
                "Wax xog ah kuma jirto.\n".to_string()
            } else {
                format!("{}\n", keys.join("\n"))
            }
        }
        "TIJAABO" => {
            if args.is_empty() {
                "ERROR: TIJAABO <fur>\n".to_string()
            } else if db.exists(args[0]) {
                "Haa, waa jirtaa.\n".to_string()
            } else {
                "Maya, kuma jirto.\n".to_string()
            }
        }
        "TIRI" => {
            format!("Wadarta furaha: {}\n", db.count())
        }
        "CUSB" => {
            if args.len() < 2 {
                "ERROR: CUSB <fur> <qii>\n".to_string()
            } else {
                let key = args[0];
                if db.exists(key) {
                    let value = args[1..].join(" ");
                    db.set(key.to_string(), CeejiyeValue::Qoraal(value));
                    format!("SUCCESS: '{}' waa la cusboonaysiiyay.\n", key)
                } else {
                    "ERROR: Furaha kuma jiro xogta.\n".to_string()
                }
            }
        }
        "NADIIFI" => {
            db.clear();
            "SUCCESS: Dhammaan xogta waa la tirtiray.\n".to_string()
        }
        "MUDDAD" => {
            if args.len() < 2 {
                "ERROR: MUDDAD <fur> <ilbiriqsi>\n".to_string()
            } else {
                let key = args[0];
                if let Ok(secs) = args[1].parse::<u64>() {
                    let val = db.get(key).unwrap_or(CeejiyeValue::Qoraal("TTL_VALUE".to_string()));
                    db.set_with_ttl(key.to_string(), val, secs);
                    format!("SUCCESS: '{}' waxaa loo muddeeyay {} ilbiriqsi.\n", key, secs)
                } else {
                    "ERROR: Muddaddu waa inay noqotaa tiro.\n".to_string()
                }
            }
        }
        "KOOB" => {
            if args.is_empty() {
                "ERROR: KOOB <fur>\n".to_string()
            } else {
                match db.increment(args[0].to_string()) {
                    Ok(n) => format!("SUCCESS: '{}' hadda waa {}.\n", args[0], n),
                    Err(e) => format!("{}\n", e),
                }
            }
        }
        "DHIMIS" => {
            if args.is_empty() {
                "ERROR: DHIMIS <fur>\n".to_string()
            } else {
                match db.decrement(args[0].to_string()) {
                    Ok(n) => format!("SUCCESS: '{}' hadda waa {}.\n", args[0], n),
                    Err(e) => format!("{}\n", e),
                }
            }
        }
        "NOOC" => {
            if args.is_empty() {
                "ERROR: NOOC <fur>\n".to_string()
            } else {
                match db.get_type(args[0]) {
                    Some(t) => format!("{}\n", t),
                    None => "ERROR: Furaha lama helin.\n".to_string(),
                }
            }
        }
        "XAALAD" => {
            format!("Status: Active, Keys: {}\n", db.count())
        }
        _ => "ERROR: Amarkan lama yaqaan.\n".to_string(),
    }
}
