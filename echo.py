#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Julita, Piero, and demo"

import argparse
import sys

def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")

    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument("-t", "--title", action="store_true", help="convert text to titlecase")
    parser.add_argument("text", help="text to be manipulated")
    
    return parser

def main(args, option=False):
    
    """Implementation of echo"""
    # Short notes:
    # value of flags have to equal true/false, not text directly
    # if you ns.upper = ['hello], you get errors when trying to pass
    # more than one flag. Also, its best to keep reassigning text. 
    # If you try to reassign a result var, it breaks when pass no flags.
    parser = create_parser()
    # pass args to parser.parse_args() function
    ns = parser.parse_args(args)

    # The BIDNESS LOGIC
    result = ns.text
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()
    if ns.title:
        result = result.title()

    return result              


if __name__ == '__main__':
    main(sys.argv[1:], option=False)
