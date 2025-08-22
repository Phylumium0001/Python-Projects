import unittest
from utils.normalize import normalize_url
from utils.hash_url import generate_hash_value
from utils.generate_short_url import generate_url
from utils.user_id import generate_user_id


class Test_Url(unittest.TestCase):
    # test method names begin with 'test'

    def testNormalizeFunc(self):
        self.assertEqual(
            normalize_url("http://www.google.com/jde"),
            "google.com/jde")

        self.assertEqual(
            normalize_url("www.google.com/jde"),
            "google.com/jde")

    def testHashFunc(self):
        self.assertEqual(
            generate_hash_value("google.com"),
            "d4c9d9027326271a89ce51fcaf328ed673f17be33469ff979e8ab8dd501e664f"
        )

    def test_gen_usr_id(self):
        self.assertIsNotNone(generate_user_id())

    def test_generate_url(self):
        normalized_url = normalize_url("google.com")
        hash = generate_hash_value(normalized_url)
        self.assertEqual(generate_url(hash, "1234"),
                         "shlk.com/1d4c-29d9-3027")


class Test_Db(unittest.TestCase):
    def TestInput(self):
        pass


if __name__ == '__main__':
    unittest.main()
