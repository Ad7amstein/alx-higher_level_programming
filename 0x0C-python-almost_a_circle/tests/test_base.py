#!/usr/bin/python3
"""Defines Unittest for base module."""

import unittest
import pycodestyle
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suits for base module functiosn."""

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quit=True)
        result = style.check_files(['models/base.py'])
