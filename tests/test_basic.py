import unittest

from data_models import build_profiles, UserProfile
from legacy_utils import LegacyCache


class TestBasics(unittest.TestCase):
    def test_profiles(self):
        profiles = build_profiles("Ada", 2)
        self.assertEqual(len(profiles), 2)
        self.assertIsInstance(profiles[0], UserProfile)

    def test_legacy_cache(self):
        cache = LegacyCache()
        cache["key"] = "value"
        self.assertEqual(cache["key"], "value")


if __name__ == "__main__":
    unittest.main()
