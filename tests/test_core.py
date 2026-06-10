import unittest
import os
import time
import ceejiye_core

class TestCeejiyeDB(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_db.json"
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db = ceejiye_core.CeejiyeStore(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_basic_ops(self):
        self.db.execute("KAYDI magac Jules")
        res = self.db.execute("SOOQAAD magac")
        self.assertEqual(res.strip(), "Jules")

        self.db.execute("TIR magac")
        res = self.db.execute("SOOQAAD magac")
        self.assertTrue("ERROR" in res)

    def test_increment_decrement(self):
        self.db.execute("KOOB tiriye") # Starts at 1
        self.db.execute("KOOB tiriye") # 2
        res = self.db.execute("SOOQAAD tiriye")
        self.assertEqual(res.strip(), "2")

        self.db.execute("DHIMIS tiriye") # 1
        res = self.db.execute("SOOQAAD tiriye")
        self.assertEqual(res.strip(), "1")

    def test_ttl(self):
        self.db.execute("KAYDI x saacad")
        self.db.execute("MUDDAD x 1")
        time.sleep(1.2)
        res = self.db.execute("SOOQAAD x")
        self.assertTrue("ERROR" in res)

    def test_persistence(self):
        self.db.execute("KAYDI fure1 qiime1")
        # Simulate restart
        del self.db
        db2 = ceejiye_core.CeejiyeStore(self.db_path)
        res = db2.execute("SOOQAAD fure1")
        self.assertEqual(res.strip(), "qiime1")

    def test_list_and_count(self):
        self.db.execute("KAYDI a 1")
        self.db.execute("KAYDI b 2")
        res = self.db.execute("TIRI")
        self.assertTrue("2" in res)
        res = self.db.execute("LIIS")
        self.assertTrue("a" in res)
        self.assertTrue("b" in res)

if __name__ == "__main__":
    unittest.main()
