# -*- coding:utf-8 -*-
from data.morse_dict import sheet

class Morse:
    def __init__(self, data = sheet):
        self.sheet = self.reverse_key_value(data)
        self.sheet_2 = data
    def code(self, word):
        result = ''
        for i in word:
            result += self.sheet[i]
        return result + '00'
    def reverse_key_value(self, rev_dict = {}):
        b = dict()
        for key in rev_dict:
            b[rev_dict[key]] = key
        return b
    def decode(self, data):
        word_code = []
        for i in data.split('0000'):
            if not i == '':
                word_code.append(i+'00')
        alpha_code = []
        for i in word_code:
            alpha_code.extend(i.split('00'))
        word = ''
        for i in alpha_code:
            if not i == '':
                word += self.sheet_2[i+'00']
        return word
            
