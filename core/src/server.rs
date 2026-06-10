use tokio::net::TcpListener;
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use std::sync::{Arc, Mutex};
use crate::storage::Storage;
use crate::dispatch::dispatch_command;

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
                let response = dispatch_command(&storage, request.trim());

                if socket.write_all(response.as_bytes()).await.is_err() {
                    return;
                }
            }
        });
    }
}
