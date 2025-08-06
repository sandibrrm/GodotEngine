# test_godotengine.py
"""
Tests for GodotEngine module.
"""

import unittest
from godotengine import GodotEngine

class TestGodotEngine(unittest.TestCase):
    """Test cases for GodotEngine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GodotEngine()
        self.assertIsInstance(instance, GodotEngine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GodotEngine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
