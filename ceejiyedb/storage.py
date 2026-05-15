import json
import os

class Storage:
    """
    In-memory storage with JSON persistence for CeejiyeDB.
    """
    def __init__(self, filepath=None):
        if filepath is None:
            # Set path relative to the script's directory
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.filepath = os.path.join(base_dir, "data.json")
        else:
            self.filepath = filepath

        self.data = {}
        self.load()

    def load(self):
        """Loads data from the JSON file into memory."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    content = f.read()
                    if content:
                        self.data = json.loads(content)
                    else:
                        self.data = {}
            except (json.JSONDecodeError, IOError):
                self.data = {}
        else:
            self.data = {}

    def save(self):
        """Saves memory data to the JSON file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.data, f, indent=4)
        except IOError as e:
            print(f"Khalad kaydinta: {e}")

    def set(self, key, value):
        """Sets a key-value pair in storage."""
        self.data[key] = value
        self.save()
        return True

    def get(self, key):
        """Retrieves a value by its key."""
        return self.data.get(key)

    def delete(self, key):
        """Deletes a key from storage."""
        if key in self.data:
            del self.data[key]
            self.save()
            return True
        return False
