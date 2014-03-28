# -*- coding:utf-8 -*-
from data.morse_dict import sheet

class Morse:
    def __init__(self, data = sheet):
        self.sheet = self.reverse_key_value(data)
    def code(self, data):
        result = ''
        for i in data:
            result += self.sheet[i]
        return result + '00'
    def reverse_key_value(self, rev_dict = {}):
        b = dict()
        for key in rev_dict:
            b[rev_dict[key]] = key
        return b
