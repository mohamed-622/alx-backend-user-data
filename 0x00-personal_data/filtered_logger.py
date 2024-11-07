#!/usr/bin/python3

""" Module for implementing a Filter class that inherits from"""

import re


def filter_datum(fields: str, redaction: str, message: str, separator: str) -> str:
    """ returns the log message obfuscated """
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
