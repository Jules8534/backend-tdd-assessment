#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# """# Your test case class goes here"""
class TestEcho(unittest.TestCase):

    def setUp(self):
        """This function is called only once for all tests"""
        self.parser = echo.create_parser()

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("./USAGE", "r") as f:
            usage = f.read()

        self.assertEquals(stdout, usage)

    def test_all_options(self):
        args = ["-tul", "HeLlo woRlD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_short(self):
        args = ["-u", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        # assert means; "Make sure that..."
        self.assertEqual(actual, expected)
    
    def test_lower_short(self):
        args = ["-l", "HELLO WORLD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_short(self):
        args = ["-t", "HeLlo woRlD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_upper_long(self):
        args = ["--u", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def test_lower_long(self):
        args = ["-l", "HELLO WORLD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_title_long(self):
        args = ["-t", "HeLlo woRlD"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    # """Running the program without arguments should show usage.
    # Run the command 'python ./echo.py -h' in a separate process, 
    # then connect it's output"""
    # process = subprocess.Popen(
    #     ["python", "./echo.py", "-h"],
    #     stdout=subprocess.PIPE)
    # stdout, _ = process.communicate()
    # usage = open("./USAGE", "r").read()
    # self.assertEquals(stdout, usage)

    # def test_upper(self):
    #     # test if --upper flag returns suppercase and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "--upper", "hello"],
    #         universal_newlines=True).strip('\n')
    #     namespace = echo.main(["--upper", "hello"], option=True)
    #     self.assertEqual(output, 'HELLO')
    #     self.assertTrue(namespace.upper)
        
    # def test_upper_short(self):
    #     # test if -u flag returns uppercase and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "-u", "hello"],
    #         universal_newlines=True.strip.('\n')
    #     namespace = echo.main(["-u", "hello"], option=True)
    #     self.assertEqual(output, 'HELLO')
    #     self.assertTrue(namespace.upper)

    # def test_lower(self):
    #     # test if -- lower flag returns lowercase and stores its val in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "--lower", "Hello"],
    #         universal_newlines=True).strip('\n')
    #     namespace = echo.main(["--lower", "Hello"], option=True)
    #     self.assertEqual(output, 'hello')
    #     self.assertTrue(namespace.lower)


    # def test_lower_short(self):
    #     # test if -l flag returns lowercase and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "--lower", "Hello"],
    #         universal_newlines=True).strip('\n')
    #     namespace = echo.main(["--lower", "Hello"], option=True)
    #     self.assertEqual(output, 'hello')
    #     self.assertTrue(namespace.lower)

    
    # def test_title(self):
    #     # test if --title flag capializes first word in string
    #     # and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "--title", "hello"],
    #         universal_newlines=True).strip('\n')
    #     namespace = echo.main(["--lower", "Hello"], option=True)
    #     self.assertEqual(output, 'hello')
    #     self.assertTrue(namespace.lower)


    # def test_title_short(self):
    #     # test if --t flag capializes first word in string
    #     # and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "-t", "hello"],
    #         universal_newlines=True).strip('\n')
    #     namespace = echo.main(["-t", "hello"], option=True)
    #     self.assertEqual(output, 'Hello')
    #     self.assertTrue(namespace.title)      


    # def test_all(self):
    #     # test if --title flag capializes first word in string
    #     # and stores its value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "--tul", "heLLo!"],
    #         universal_newlines=True).strip('\n')
    #     output2 = subprocess.check_output(
    #         ["python", "./echo.py" "-ul", "heLLo!"],
    #         universal_newlines=True).strip('\n')
    #     self.assertEqual(output, 'Hello!')
    #     self.assertEqual(ouput2, 'hello!')


    # def test_no_flags(self):
    #     # test if passing no optional arg returns positional arg
    #     # and stores value in NS
    #     output = subprocess.check_output(
    #         ["python", "./echo.py", "hello!"],
    #         universal_newlines=True.strip('\n')
    #     self.assertEqual(output, 'hello!')
    
if __name__ == '__main__':
    unittest.main()
