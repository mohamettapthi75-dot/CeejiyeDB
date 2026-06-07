use std::time::Instant;

#[derive(Clone, Debug)]
pub enum CeejiyeValue {
    Qoraal(String),
    Tiro(i64),
    Liis(Vec<String>),
}

#[derive(Clone, Debug)]
pub struct StoredValue {
    pub value: CeejiyeValue,
    pub expires_at: Option<Instant>,
}
