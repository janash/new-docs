"""
Unit and regression test for the projectname package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import projectname


def test_projectname_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "projectname" in sys.modules
