#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.06.19
@author: felix
"""


from rply import ParserGenerator
from my_own_language.ast import Number, Sum, Sub, Mul, Div, Print


class Parser:

    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            ['NUMBER',
             'PRINT',
             'OPEN_PAREN',
             'CLOSE_PAREN',
             'OPEN_BRACE',
             'CLOSE_BRACE',
             'OPEN_BRAKET',
             'CLOSE_BRAKET',
             'SEMI_COLON',
             'SUM',
             'SUB',
             'MUL',
             'DIV',
             ]
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handler(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
