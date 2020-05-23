import os
import subprocess
import sys
import unittest


class CliTests(unittest.TestCase):
    alfaci = os.path.join(os.path.dirname(__file__), '..', 'lib', 'alfaci',
                          'cli.py')

    def test_shell_setup(self):
        actual = subprocess.run(
            [sys.executable, self.alfaci, 'shell-setup'],
            capture_output=True)
        actual.check_returncode()

    def test_version(self):
        actual = subprocess.run(
            [sys.executable, self.alfaci, 'version'],
            capture_output=True).stdout.decode('UTF-8').strip()
        from alfaci.version import pkg_version as expected
        self.assertEqual(actual, expected)
