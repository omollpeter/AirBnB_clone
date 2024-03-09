import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel


class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.my_console = HBNBCommand()
