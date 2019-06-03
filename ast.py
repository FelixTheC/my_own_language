#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 02.06.19
@author: felix
"""
from llvmlite import ir


class Number:
    def __init__(self, builder, module, val):
        self.val = val
        self.builder = builder
        self.module = module

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.val))
        return i
        # return int(self.val)


class BinaryOp:

    def __init__(self, builder, module, left, right):
        self.left = left
        self.right = right
        self.builder = builder
        self.module = module


class Sum(BinaryOp):

    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinaryOp):

    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Mul(BinaryOp):

    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i
        # return self.left.eval() * self.right.eval()


class Div(BinaryOp):

    def eval(self):
        i = self.builder.sdiv(self.left.eval(), self.right.eval())
        return i
        # return self.left.eval() / self.right.eval()


class Print:

    def __init__(self, builder, module, printf, val):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.val = val

    def eval(self):
        val = self.val.eval()

        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        self.builder.call(self.printf, [fmt_arg, val])
