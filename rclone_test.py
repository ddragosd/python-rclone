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

# pylint: disable=W0212,C0111

import unittest
import tempfile
import os
import logging
import json
import rclone


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")


class RSyncTest(unittest.TestCase):
    def setUp(self):
        self.cfg = """[local]
        type = local
        nounc = true"""

    def test_execute_with_wrong_command(self):
        result = rclone.with_config(self.cfg)._execute(
            ["command_not_valid", "some", "args"])
        self.assertEqual(result.get('code'), -20)
        self.assertIsInstance(result.get('error'), FileNotFoundError)

    def test_execute_with_correct_command(self):
        result = rclone.with_config(self.cfg)._execute(["echo", "123"])
        self.assertEqual(result.get('code'), 0)
        self.assertIsNotNone(result.get('out'))

    def test_listremoted(self):
        result = rclone.with_config(self.cfg).listremotes()
        self.assertEqual(result.get('code'), 0)
        self.assertEqual(result.get('out'), b'local:\n')

    def test_copy_and_ls(self):
        source = "local:" + os.getcwd() + "/README.md"
        with tempfile.TemporaryDirectory() as dest:
            result = rclone.with_config(self.cfg).copy(
                source, "local:" + dest)
            self.assertEqual(result.get('code'), 0)
            self.assertEqual(result.get('out'), b'')

            result = rclone.with_config(self.cfg).ls("local:"+dest)
            self.assertEqual(result.get('code'), 0)
            self.assertRegex(result.get('out').decode("utf-8"),
                             r'.*\sREADME.md.*', "README.md was not listed.")

    def test_sync_and_lsjson(self):
        source = "local:" + os.getcwd() + "/README.md"
        with tempfile.TemporaryDirectory() as dest:
            result = rclone.with_config(self.cfg).sync(
                source, "local:" + dest)
            self.assertEqual(result.get('code'), 0)
            self.assertEqual(result.get('out'), b'')

            result = rclone.with_config(self.cfg).lsjson("local:"+dest)
            self.assertEqual(result.get('code'), 0)
            result_json = json.loads(result.get('out').decode("utf-8"))
            self.assertGreater(len(result_json), 0)
            self.assertEqual(result_json[0].get('Path'), 'README.md')
            self.assertFalse(result_json[0].get('IsDir'))

    def test_copy_lsjson_and_delete(self):
        source = "local:" + os.getcwd() + "/README.md"
        with tempfile.TemporaryDirectory() as dest:
            # copy
            result = rclone.with_config(self.cfg).copy(
                source, "local:" + dest)
            self.assertEqual(result.get('code'), 0)
            self.assertEqual(result.get('out'), b'')
            # lsjson
            result = rclone.with_config(self.cfg).lsjson("local:"+dest)
            self.assertEqual(result.get('code'), 0)
            result_json = json.loads(result.get('out').decode("utf-8"))
            self.assertGreater(len(result_json), 0)
            self.assertEqual(result_json[0].get('Path'), 'README.md')
            self.assertFalse(result_json[0].get('IsDir'))
            # delete
            result = rclone.with_config(self.cfg).delete(
                "local:" + dest + "/README.md")
            self.assertEqual(result.get('code'), 0)
            # lsjson to check that the file is gone
            result = rclone.with_config(self.cfg).lsjson("local:"+dest)
            self.assertEqual(result.get('code'), 0)
            result_json = json.loads(result.get('out').decode("utf-8"))
            self.assertEqual(len(result_json), 0)


if __name__ == '__main__':
    unittest.main()