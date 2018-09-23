#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import base64
import sys
from rclone import rclone
import tempfile
import os
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

class RSyncTest(unittest.TestCase):
    def test_execute_with_wrong_command(self):
        result = rclone.with_config(None)._execute(
            ["command_not_valid", "some", "args"])
        self.assertEqual(result.get('code'), -20)
        self.assertIsInstance(result.get('error'), FileNotFoundError)

    def test_execute_with_correct_command(self):
        result = rclone.with_config(None)._execute(["echo", "123"])
        self.assertEqual(result.get('code'), 0)
        self.assertIsNotNone(result.get('out'))

    def test_listremoted(self):
        # TODO
        cfg = """[local]
        type = local
        nounc = true"""
        result = rclone.with_config(cfg).listremotes()
        self.assertEqual(result.get('code'), 0)
        self.assertEqual(result.get('out'), b'local:\n')
        pass