use pyo3::prelude::*;
use std::sync::{Arc, Mutex};
use std::thread;

mod types;
mod storage;
mod server;

use types::CeejiyeValue;
use storage::Storage;

#[pyclass]
struct CeejiyeStore {
    inner: Arc<Mutex<Storage>>,
}

#[pymethods]
impl CeejiyeStore {
    #[new]
    fn new() -> Self {
        Self {
            inner: Arc::new(Mutex::new(Storage::new())),
        }
    }

    fn set(&mut self, key: String, value: String) {
        let mut db = self.inner.lock().unwrap();
        db.set(key, CeejiyeValue::Qoraal(value));
    }

    fn set_with_ttl(&mut self, key: String, value: String, seconds: u64) {
        let mut db = self.inner.lock().unwrap();
        db.set_with_ttl(key, CeejiyeValue::Qoraal(value), seconds);
    }

    fn get(&mut self, key: String) -> PyResult<Option<String>> {
        let mut db = self.inner.lock().unwrap();
        match db.get(&key) {
            Some(CeejiyeValue::Qoraal(s)) => Ok(Some(s)),
            Some(CeejiyeValue::Tiro(n)) => Ok(Some(n.to_string())),
            Some(CeejiyeValue::Liis(l)) => Ok(Some(format!("{:?}", l))),
            None => Ok(None),
        }
    }

    fn delete(&mut self, key: String) -> bool {
        let mut db = self.inner.lock().unwrap();
        db.delete(&key)
    }

    fn exists(&mut self, key: String) -> bool {
        let mut db = self.inner.lock().unwrap();
        db.exists(&key)
    }

    fn count(&mut self) -> usize {
        let mut db = self.inner.lock().unwrap();
        db.count()
    }

    fn clear(&mut self) {
        let mut db = self.inner.lock().unwrap();
        db.clear();
    }

    fn keys(&mut self) -> Vec<String> {
        let mut db = self.inner.lock().unwrap();
        db.get_all_keys()
    }

    fn increment(&mut self, key: String) -> PyResult<i64> {
        let mut db = self.inner.lock().unwrap();
        db.increment(key).map_err(|e| PyErr::new::<pyo3::exceptions::PyTypeError, _>(e))
    }

    fn get_type(&mut self, key: String) -> Option<String> {
        let mut db = self.inner.lock().unwrap();
        db.get(&key).map(|v| match v {
            CeejiyeValue::Qoraal(_) => "Qoraal".to_string(),
            CeejiyeValue::Tiro(_) => "Tiro".to_string(),
            CeejiyeValue::Liis(_) => "Liis".to_string(),
        })
    }

    fn start_server(&self, port: u16) {
        let storage = Arc::clone(&self.inner);
        thread::spawn(move || {
            let rt = tokio::runtime::Runtime::new().unwrap();
            rt.block_on(async {
                let _ = server::run_server(storage, port).await;
            });
        });
    }
}

#[pymodule]
fn ceejiye_core(_py: Python, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<CeejiyeStore>()?;
    Ok(())
}
