import socket

class CeejiyeClient:
    """
    Python SDK for CeejiyeDB TCP server.
    """
    def __init__(self, host="localhost", port=7379):
        self.host = host
        self.port = port

    def _send_command(self, cmd_string):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(cmd_string.encode())
            data = s.recv(1024)
            return data.decode().strip()

    def kaydi(self, key, value):
        return self._send_command(f"KAYDI {key} {value}")

    def sooqaad(self, key):
        return self._send_command(f"SOOQAAD {key}")

    def tir(self, key):
        return self._send_command(f"TIR {key}")

    def tiri(self):
        return self._send_command("TIRI")
