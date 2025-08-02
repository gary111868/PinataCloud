# test_pinatacloud.py
"""
Tests for PinataCloud module.
"""

import unittest
from pinatacloud import PinataCloud

class TestPinataCloud(unittest.TestCase):
    """Test cases for PinataCloud class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PinataCloud()
        self.assertIsInstance(instance, PinataCloud)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PinataCloud()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
