#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.06.19
@author: felix
"""


from rply import LexerGenerator


class Lexer:

    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Print
        self.lexer.add('PRINT', r'print')
        # Braces
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACE', r'{')
        self.lexer.add('CLOSE_BRACE', r'}')
        self.lexer.add('OPEN_BRAKET', r'\[')
        self.lexer.add('CLOSE_BRAKET', r'\]')
        # Operations
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'/')
        # Datatype
        self.lexer.add('NUMBER', r'\d+')
        # Semicolon
        self.lexer.add('SEMI_COLON', r'\;')
        # ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
