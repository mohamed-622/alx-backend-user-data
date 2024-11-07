#!/usr/bin/env python3
""" Redacting Formatter class """

import re
""" Redacting Formatter class """


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join([rf'{field}=[^ {separator}]*' for field in fields])
    return re.sub(pattern, lambda m: f'{m.group().split("=")[0]}={redaction}', message)
