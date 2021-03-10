"""The algorithms test suite.

Re-export individual test sub-packages in order to allow importing them as the whole into another module (`main.py`) and running them all at once.

Exported sub-packages:
  - search
  - sort
"""
import test.search
import test.sort