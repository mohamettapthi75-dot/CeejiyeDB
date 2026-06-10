import json
import os
import time
import sys

class Storage:
    """
    v1.2.0: In-memory storage with JSON persistence, TTL, and Atomic Ops.
    """
    def __init__(self, filepath=None):
        if filepath is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.filepath = os.path.join(base_dir, "data.json")
        else:
            self.filepath = filepath

        self.data = {}  # {key: {"value": val, "expires_at": timestamp or None}}
        self.load()

    def load(self):
        """Loads data from the JSON file into memory."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    content = f.read()
                    if content:
                        raw_data = json.loads(content)
                        # Migration: support old {key: value} format and new format
                        for k, v in raw_data.items():
                            if isinstance(v, dict) and "value" in v:
                                self.data[k] = v
                            else:
                                self.data[k] = {"value": v, "expires_at": None}
                    else:
                        self.data = {}
            except (json.JSONDecodeError, IOError):
                self.data = {}
        else:
            self.data = {}
        self.purge_expired()

    def save(self):
        """Saves memory data to the JSON file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Khalad kaydinta: {e}")

    def purge_expired(self):
        """Removes expired keys from storage."""
        now = time.time()
        expired_keys = [k for k, v in self.data.items()
                        if v.get("expires_at") and v["expires_at"] < now]
        for k in expired_keys:
            del self.data[k]
        if expired_keys:
            self.save()

    def set(self, key, value, ttl=None):
        """Sets a key-value pair in storage with optional TTL."""
        expires_at = time.time() + ttl if ttl else None
        self.data[key] = {"value": value, "expires_at": expires_at}
        self.save()
        return True

    def get(self, key):
        """Retrieves a value by its key if not expired."""
        self.purge_expired()
        entry = self.data.get(key)
        if entry:
            return entry["value"]
        return None

    def delete(self, key):
        """Deletes a key from storage."""
        if key in self.data:
            del self.data[key]
            self.save()
            return True
        return False

    def increment(self, key):
        """Increments integer value of a key."""
        self.purge_expired()
        entry = self.data.get(key)
        try:
            val = int(entry["value"]) if entry else 0
            new_val = val + 1
            self.set(key, str(new_val))
            return new_val
        except (ValueError, TypeError):
            raise ValueError("ERROR: Furaha noociisu ma ahan Tiro.")

    def decrement(self, key):
        """Decrements integer value of a key."""
        self.purge_expired()
        entry = self.data.get(key)
        try:
            val = int(entry["value"]) if entry else 0
            new_val = val - 1
            self.set(key, str(new_val))
            return new_val
        except (ValueError, TypeError):
            raise ValueError("ERROR: Furaha noociisu ma ahan Tiro.")

    def set_ttl(self, key, seconds):
        """Updates TTL for an existing key."""
        self.purge_expired()
        if key in self.data:
            self.data[key]["expires_at"] = time.time() + seconds
            self.save()
            return True
        return False

    def get_stats(self):
        """Returns database statistics."""
        self.purge_expired()
        key_count = len(self.data)
        mem_usage = sys.getsizeof(self.data) + sum(sys.getsizeof(v) for v in self.data.values())
        file_size = os.path.getsize(self.filepath) if os.path.exists(self.filepath) else 0
        return {
            "keys": key_count,
            "memory": mem_usage,
            "file_size": file_size
        }
