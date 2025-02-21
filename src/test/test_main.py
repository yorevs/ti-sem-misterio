#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
   @project: %PROJECT_NAME%
   @package: test
      @file: test_main.py
   @created: %DDD, DD Mon YYYY%
    @author: AUTHOR
      @site: SITE_URL
   @license: MIT - Please refer to <https://opensource.org/licenses/MIT>

   Copyright (c) COPYRIGHT
"""

from hspylib.core.config.app_config import AppConfigs
from hspylib.core.tools.commons import dirname

import logging as log
import os
import sys
import unittest

TEST_DIR = dirname(__file__)


class TestMain(unittest.TestCase):
    # Setup tests
    def setUp(self):
        resource_dir = f"{TEST_DIR}/resources"
        os.environ["ACTIVE_PROFILE"] = "test"
        self.configs = AppConfigs(resource_dir=resource_dir)
        self.assertIsNotNone(self.configs)
        self.assertEqual(self.configs.get_int('any.property'), 12345)
        log.info(self.configs)

    # Teardown tests
    def tearDown(self):
        pass

    # TEST CASES ----------

    def test_should_test_something(self):
        pass


# Program entry point.
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMain)
    unittest.TextTestRunner(verbosity=2, failfast=True, stream=sys.stdout).run(suite)
