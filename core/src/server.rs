use tokio::net::TcpListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use std::sync::{Arc, Mutex};
use crate::storage::Storage;
use crate::types::CeejiyeValue;

pub async fn run_server(storage: Arc<Mutex<Storage>>, port: u16) -> tokio::io::Result<()> {
    let listener = TcpListener::bind(format!("0.0.0.0:{}", port)).await?;
    println!("CeejiyeDB server listening on port {}", port);

    loop {
        let (mut socket, _) = listener.accept().await?;
        let storage = Arc::clone(&storage);

        tokio::spawn(async move {
            let mut buf = [0; 1024];
            loop {
                let n = match socket.read(&mut buf).await {
                    Ok(n) if n == 0 => return,
                    Ok(n) => n,
                    Err(_) => return,
                };

                let request = String::from_utf8_lossy(&buf[..n]);
                let response = handle_request(&storage, request.trim());

                if socket.write_all(response.as_bytes()).await.is_err() {
                    return;
                }
            }
        });
    }
}

fn handle_request(storage: &Arc<Mutex<Storage>>, request: &str) -> String {
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
        "TIRI" => {
            format!("Wadarta furaha: {}\n", db.count())
        }
        _ => "ERROR: Amarkan lama yaqaan.\n".to_string(),
    }
}
