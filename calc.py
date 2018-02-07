#!/usr/bin/env python
# coding=utf-8

"""
假设输入为一行文字，是由“0”到“9”的数字、“+”、“-” 、“*” 、“/” 、“(” 、“)”组成的四则运算式。现要求对输入字符串进行分析，按照四则运算的要求计算出结果。

要求：

1.  参与运算的数均为十进制整数，数字的解析方式参照数学表达式规则；
2.  加减乘除以及括号的优先级顺序参照数学表达式规则；
3.  要求支持括号嵌套，大括号“{}”和中括号“[]”均由小括号“()”替代；
4.  最终结果用分数（真分数、假分数、带分数均可）表示，保留所有精度，要求为最简分数（即分子分母互素）；
5.  输入数字为-10000~10000以内的整数，但输出结果位数不限
"""

import re
import warnings

operators = ["+", "-", "*", "/", "(", ")"]


class my_number:  # convert int number to a number with fraction.
    int_part = 0
    numerator_part = 0
    denominator_part = 1

    def convert_from_str(self, int_str):
        self.numerator_part = int(int_str)
        self.denominator_part = 1

    def add(self, other):
        self.numerator_part \
            = self.numerator_part * other.denominator_part + self.denominator_part * other.numerator_part
        self.denominator_part = self.denominator_part * other.denominator_part

    def min(self, other):
        self.numerator_part \
            = self.numerator_part * other.denominator_part - self.denominator_part * other.numerator_part
        self.denominator_part = self.denominator_part * other.denominator_part

    def mul(self, other):
        self.numerator_part *= other.numerator_part
        self.denominator_part *= other.denominator_part

    def div(self, other):
        self.numerator_part *= other.denominator_part
        self.denominator_part *= other.numerator_part

    def print_result(self):
        if self.numerator_part > self.denominator_part:
            self.int_part = self.numerator_part / self.denominator_part
            self.numerator_part = self.numerator_part % self.denominator_part

        smaller = self.numerator_part
        hcf = 1
        for i in range(1, smaller + 1):
            if ((self.numerator_part % i == 0) and (self.denominator_part % i == 0)):
                hcf = i
        self.numerator_part /= hcf
        self.denominator_part /= hcf

        if self.numerator_part == 0:
            print "The result is %d" % self.int_part
        elif self.int_part == 0:
            print "The result is %d/%d" % (self.numerator_part, self.denominator_part)
        else:
            print "The result is %d(%d/%d)" % (self.int_part, self.numerator_part, self.denominator_part)


def nifix2suffix(exp):
    stack = []
    suffix = []
    index = 0
    num = ""
    for c in exp:
        if c in operators:
            if 0 == len(stack):
                stack.append(c)
            else:
                if check_need_pop(c, stack[-1]):
                    op = stack.pop()
                    stack.append(c)
                    suffix.append(op)
                elif ")" == c:
                    while 1:
                        op = stack.pop()
                        if "(" == op:
                            break
                        else:
                            suffix.append(op)
                else:
                    stack.append(c)
        else:
            num += c
            if exp.__len__() - 1 == index:
                suffix.append(num)
                num = ""
                while len(stack) > 0:
                    op = stack.pop()
                    suffix.append(op)
            elif exp[index + 1] in operators:
                suffix.append(num)
                num = ""
        index += 1
    # print suffix
    calculate_suffix(suffix)


def check_need_pop(op, top_stack):
    high_priority = ["*", "/"]
    low_priority = ["+", "-"]
    if top_stack in high_priority and op in low_priority:
        return True
    else:
        return False


def calculate_suffix(exp_list):
    number_stack = []
    for item in exp_list:
        if item not in operators:
            # number_stack.append(item)
            _num = my_number()
            _num.convert_from_str(item)
            number_stack.append(_num)
        else:
            num2 = number_stack.pop()
            num1 = number_stack.pop()
            # number_stack.append(calculate(item, float(num1), float(num2)))
            number_stack.append(calculate_new(item, num1, num2))
    number_stack.pop().print_result()


def calculate(operator, num1, num2):  # need use my_number to calculate
    if "+" == operator:
        return num1 + num2
    elif "-" == operator:
        return num1 - num2
    elif "*" == operator:
        return num1 * num2
    elif "/" == operator:
        return num1 / num2


def calculate_new(operator, num1, num2):
    if "+" == operator:
        num1.add(num2)
    elif "-" == operator:
        num1.min(num2)
    elif "*" == operator:
        num1.mul(num2)
    elif "/" == operator:
        num1.div(num2)
    return num1

def check_expression(exp):
    p = re.compile(r'\d+')
    operator = p.split(exp)
    for _str in operator:
        if '' == _str:
            continue
        else:
            for c in _str:
                if c not in operators:
                    warnings.warn("There is an invalid operator %s in your expression, please check your input" % c)
                    return False
    return True


def main():
    option = raw_input("Please select a test case to run or enter your own case:\n"
                       "    (A) 1+2*3+(4*5+6)*7 \n"
                       "    (B) 1+((2-3)+4)*5/6 \n"
                       "    (Y)our case\n"
                       "    (Q)uit\n")
    if "A" == option or "a" == option:
        nifix2suffix("101+33*3+(73-9)/117")

    elif "B" == option or "b" == option:
        nifix2suffix("1+((2-3)+4)*5/6")

    elif "Y" == option or "y" == option:
        expression = raw_input("Please input your expression (without space):\n")
        if check_expression(expression):
            nifix2suffix(expression)

    elif "Q" == option or "q" == option:
        exit()
    else:
        print "Invalid option\n"
    print "\n\n\n"
    main()


if __name__ == "__main__":
    main()