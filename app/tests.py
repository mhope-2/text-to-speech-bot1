import subprocess
import sys

from django.test import SimpleTestCase


class SoupSieveSecurityTests(SimpleTestCase):
    """Regression coverage for Soup Sieve selector-parser ReDoS (#55)."""

    def test_unterminated_attribute_selector_does_not_hang(self):
        selector_test = """
import soupsieve

selector = '[a="' + ('x' * 300)
try:
    soupsieve.compile(selector)
except Exception:
    pass
"""

        result = subprocess.run(
            [sys.executable, "-c", selector_test],
            capture_output=True,
            text=True,
            timeout=2,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
