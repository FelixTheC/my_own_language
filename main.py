#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.06.19
@author: felix
"""
from my_own_language.lexer import Lexer
from my_own_language.parser import Parser
from my_own_language.codegen import CodeGen

fname = 'input.ba'
with open(fname, 'r+') as f:
    text_input = f.read()

# text_input = """
# print(4 + 4 * 2);
# """

# for token in tokens:
#     """
#     Token('PRINT', 'print')
#     Token('OPEN_PAREN', '(')
#     Token('NUMBER', '4')
#     Token('SUM', '+')
#     Token('NUMBER', '4')
#     Token('MUL', '*')
#     Token('NUMBER', '2')
#     Token('CLOSE_PAREN', ')')
#     Token('SEMI_COLON', ';')
#     """
#     print(token)

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

pg = Parser(module, builder, printf)
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()

codegen.create_ir()
codegen.save_ir('output.ll')
