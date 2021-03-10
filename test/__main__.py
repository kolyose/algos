"""The algorithms test suite.

Re-export individual test sub-packages in order to allow running them all at once from CLI by `python -m test` command.

Exported sub-packages:
  - search
  - sort
"""
import test.search
import test.sort