#!/usr/bin/env python
#
# Python-bindings des3_context type test script
#
# Copyright (C) 2017-2023, Joachim Metz <joachim.metz@gmail.com>
#
# Refer to AUTHORS for acknowledgements.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import os
import sys
import unittest

import pyfcrypto


class Des3ContextTypeTests(unittest.TestCase):
  """Tests the des3_context type."""

  def test_initialize(self):
    """Tests the __init__ function."""
    des3_context = pyfcrypto.des3_context()
    self.assertIsNotNone(des3_context)


if __name__ == "__main__":
  argument_parser = argparse.ArgumentParser()

  options, unknown_options = argument_parser.parse_known_args()
  unknown_options.insert(0, sys.argv[0])

  unittest.main(argv=unknown_options, verbosity=2)
