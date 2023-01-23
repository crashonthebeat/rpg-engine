import unittest
import src.cmdparse as cmd

class singleVerbTest(unittest.TestCase):
    def test(self):
        self.assertEqual(cmd.parse("rest"), ("rest", False, False, False))
        self.assertEqual(cmd.parse("Rest"), ("rest", False, False, False))
        self.assertEqual(cmd.parse("I rest"), ("rest", False, False, False))

class singleObjectTest(unittest.TestCase):
    def test(self):
        self.assertEqual(cmd.parse("take sword"), ("take", "sword", False, False))
        self.assertEqual(cmd.parse("take the sword"), ("take", "sword", False, False))
        self.assertEqual(cmd.parse("I take the sword"), ("take", "sword", False, False))
        self.assertEqual(cmd.parse("I take the shining sword"), ("take", "shining sword", False, False))
        self.assertEqual(cmd.parse("I take the benevolent sword"), ("take", "benevolent sword", False, False))

class indirectObjectTest(unittest.TestCase):
    def test(self):
        self.assertEqual(cmd.parse("take sword from stone"), ("take", "sword", "stone", "from"))
        self.assertEqual(cmd.parse("give the shining sword to the suspicious merchant"), ("give", "shining sword", "suspicious merchant", "to"))


unittest.main()