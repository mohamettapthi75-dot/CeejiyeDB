use std::time::Instant;
use serde::{Serialize, Deserialize};

#[derive(Clone, Debug, Serialize, Deserialize)]
pub enum CeejiyeValue {
    Qoraal(String),
    Tiro(i64),
    Liis(Vec<String>),
    Set(Vec<String>), // Stored as Vec for simplicity in JSON, unique on insertion
    Hash(std::collections::HashMap<String, String>),
}

#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct StoredValue {
    pub value: CeejiyeValue,
    pub expires_at_unix: Option<u64>, // Use unix timestamp for easy serialization
}
