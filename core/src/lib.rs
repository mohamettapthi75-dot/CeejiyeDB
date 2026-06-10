use pyo3::prelude::*;
use std::sync::{Arc, Mutex};
use std::thread;

mod types;
mod storage;
mod server;
mod dispatch;

use storage::Storage;
use dispatch::dispatch_command;

#[pyclass]
struct CeejiyeStore {
    inner: Arc<Mutex<Storage>>,
}

#[pymethods]
impl CeejiyeStore {
    #[new]
    fn new(db_path: Option<String>) -> Self {
        let path = db_path.unwrap_or_else(|| "data.json".to_string());
        Self {
            inner: Arc::new(Mutex::new(Storage::new(path))),
        }
    }

    fn execute(&mut self, request: String) -> String {
        dispatch_command(&self.inner, request.trim())
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
