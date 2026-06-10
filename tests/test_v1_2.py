import unittest
import os
import time
import sys
import json

# Add project root to path
sys.path.append(os.path.join(os.getcwd(), 'ceejiyedb'))

from storage import Storage
from parser import Parser
from commands import CommandHandler

class TestCeejiyeDB_v1_2(unittest.TestCase):
    def setUp(self):
        self.test_file = "tests/test_data.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.storage = Storage(filepath=self.test_file)
        self.parser = Parser()
        self.handler = CommandHandler(self.storage)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_basic_ops(self):
        # KAYDI / SOOQAAD
        self.handler.execute(*self.parser.parse("KAYDI magac Ceejiye"))
        res = self.handler.execute(*self.parser.parse("SOOQAAD magac"))
        self.assertEqual(res, "Ceejiye")

    def test_ttl(self):
        # KAYDI with MUDDAD
        self.handler.execute(*self.parser.parse("KAYDI x value"))
        self.handler.execute(*self.parser.parse("MUDDAD x 1"))

        # Check it exists
        res = self.handler.execute(*self.parser.parse("SOOQAAD x"))
        self.assertEqual(res, "value")

        # Wait for expiration
        time.sleep(1.2)
        res = self.handler.execute(*self.parser.parse("SOOQAAD x"))
        self.assertTrue("ERROR" in res)

    def test_inc_dec(self):
        # KOOB (initially sets to 1 if not exists)
        res = self.handler.execute(*self.parser.parse("KOOB tiriye"))
        self.assertTrue("1" in res)

        # KOOB again
        res = self.handler.execute(*self.parser.parse("KOOB tiriye"))
        self.assertTrue("2" in res)

        # DHIMIS
        res = self.handler.execute(*self.parser.parse("DHIMIS tiriye"))
        self.assertTrue("1" in res)

    def test_stats(self):
        self.handler.execute(*self.parser.parse("KAYDI a 1"))
        self.handler.execute(*self.parser.parse("KAYDI b 2"))
        res = self.handler.execute(*self.parser.parse("XAALAD"))
        self.assertTrue("Wadarta Furayaasha: 2" in res)

    def test_persistence_migration(self):
        # Create a legacy style file (simulated by Storage.load logic)
        with open(self.test_file, "w") as f:
            json.dump({"old_key": "old_value"}, f)

        # Reload storage
        new_storage = Storage(filepath=self.test_file)
        self.assertEqual(new_storage.get("old_key"), "old_value")

        # Check structure is upgraded on save
        new_storage.save()
        with open(self.test_file, "r") as f:
            data = json.load(f)
            self.assertIsInstance(data["old_key"], dict)
            self.assertEqual(data["old_key"]["value"], "old_value")

if __name__ == "__main__":
    unittest.main()
