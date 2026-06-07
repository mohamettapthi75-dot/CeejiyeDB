use std::collections::HashMap;
use std::time::{Duration, Instant};
use crate::types::{CeejiyeValue, StoredValue};

pub struct Storage {
    data: HashMap<String, StoredValue>,
}

impl Storage {
    pub fn new() -> Self {
        Self {
            data: HashMap::new(),
        }
    }

    pub fn set(&mut self, key: String, value: CeejiyeValue) {
        self.data.insert(key, StoredValue {
            value,
            expires_at: None,
        });
    }

    pub fn set_with_ttl(&mut self, key: String, value: CeejiyeValue, seconds: u64) {
        let expires_at = Instant::now() + Duration::from_secs(seconds);
        self.data.insert(key, StoredValue {
            value,
            expires_at: Some(expires_at),
        });
    }

    pub fn get(&mut self, key: &str) -> Option<CeejiyeValue> {
        self.purge_expired();
        self.data.get(key).map(|v| v.value.clone())
    }

    pub fn delete(&mut self, key: &str) -> bool {
        self.data.remove(key).is_some()
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
    }

    pub fn get_all_keys(&mut self) -> Vec<String> {
        self.purge_expired();
        self.data.keys().cloned().collect()
    }

    pub fn purge_expired(&mut self) {
        let now = Instant::now();
        self.data.retain(|_, v| {
            match v.expires_at {
                Some(expiry) => expiry > now,
                None => true,
            }
        });
    }

    pub fn increment(&mut self, key: String) -> Result<i64, String> {
        self.purge_expired();
        if let Some(entry) = self.data.get_mut(&key) {
            match &mut entry.value {
                CeejiyeValue::Tiro(n) => {
                    *n += 1;
                    Ok(*n)
                }
                _ => Err("Khalad: Furaha noociisu ma ahan Tiro (i64).".to_string()),
            }
        } else {
            self.set(key, CeejiyeValue::Tiro(1));
            Ok(1)
        }
    }
}
