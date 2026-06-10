use std::collections::HashMap;
use std::time::{Duration, SystemTime, UNIX_EPOCH};
use std::fs::File;
use std::io::{Read, Write};
use crate::types::{CeejiyeValue, StoredValue};

pub struct Storage {
    data: HashMap<String, StoredValue>,
    db_path: String,
}

impl Storage {
    pub fn new(db_path: String) -> Self {
        let mut storage = Self {
            data: HashMap::new(),
            db_path,
        };
        storage.load();
        storage
    }

    fn now_unix() -> u64 {
        SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs()
    }

    pub fn save(&self) {
        if let Ok(json) = serde_json::to_string_pretty(&self.data) {
            if let Ok(mut file) = File::create(&self.db_path) {
                let _ = file.write_all(json.as_bytes());
            }
        }
    }

    pub fn load(&mut self) {
        if let Ok(mut file) = File::open(&self.db_path) {
            let mut content = String::new();
            if file.read_to_string(&mut content).is_ok() {
                if let Ok(loaded_data) = serde_json::from_str(&content) {
                    self.data = loaded_data;
                }
            }
        }
    }

    pub fn set(&mut self, key: String, value: CeejiyeValue) {
        self.data.insert(key, StoredValue {
            value,
            expires_at_unix: None,
        });
        self.save();
    }

    pub fn set_with_ttl(&mut self, key: String, value: CeejiyeValue, seconds: u64) {
        let expiry = Self::now_unix() + seconds;
        self.data.insert(key, StoredValue {
            value,
            expires_at_unix: Some(expiry),
        });
        self.save();
    }

    pub fn get(&mut self, key: &str) -> Option<CeejiyeValue> {
        self.purge_expired();
        self.data.get(key).map(|v| v.value.clone())
    }

    pub fn delete(&mut self, key: &str) -> bool {
        let removed = self.data.remove(key).is_some();
        if removed { self.save(); }
        removed
    }

    pub fn exists(&mut self, key: &str) -> bool {
        self.purge_expired();
        self.data.contains_key(key)
    }

    pub fn count(&mut self) -> usize {
        self.purge_expired();
        self.data.len()
    }

    pub fn clear(&mut self) {
        self.data.clear();
        self.save();
    }

    pub fn get_all_keys(&mut self) -> Vec<String> {
        self.purge_expired();
        self.data.keys().cloned().collect()
    }

    pub fn purge_expired(&mut self) {
        let now = Self::now_unix();
        let mut changed = false;
        self.data.retain(|_, v| {
            let keep = match v.expires_at_unix {
                Some(expiry) => expiry > now,
                None => true,
            };
            if !keep { changed = true; }
            keep
        });
        if changed { self.save(); }
    }

    pub fn increment(&mut self, key: String) -> Result<i64, String> {
        self.purge_expired();
        let val = if let Some(entry) = self.data.get_mut(&key) {
            match &mut entry.value {
                CeejiyeValue::Tiro(n) => {
                    *n += 1;
                    *n
                }
                _ => return Err("ERROR: Furaha noociisu ma ahan Tiro.".to_string()),
            }
        } else {
            self.data.insert(key.clone(), StoredValue {
                value: CeejiyeValue::Tiro(1),
                expires_at_unix: None,
            });
            1
        };
        self.save();
        Ok(val)
    }

    pub fn decrement(&mut self, key: String) -> Result<i64, String> {
        self.purge_expired();
        let val = if let Some(entry) = self.data.get_mut(&key) {
            match &mut entry.value {
                CeejiyeValue::Tiro(n) => {
                    *n -= 1;
                    *n
                }
                _ => return Err("ERROR: Furaha noociisu ma ahan Tiro.".to_string()),
            }
        } else {
            self.data.insert(key.clone(), StoredValue {
                value: CeejiyeValue::Tiro(-1),
                expires_at_unix: None,
            });
            -1
        };
        self.save();
        Ok(val)
    }

    pub fn get_type(&mut self, key: &str) -> Option<String> {
        self.purge_expired();
        self.data.get(key).map(|v| match v.value {
            CeejiyeValue::Qoraal(_) => "Qoraal".to_string(),
            CeejiyeValue::Tiro(_) => "Tiro".to_string(),
            CeejiyeValue::Liis(_) => "Liis".to_string(),
            CeejiyeValue::Set(_) => "Set".to_string(),
            CeejiyeValue::Hash(_) => "Hash".to_string(),
        })
    }
}
