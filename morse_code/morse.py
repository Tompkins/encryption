from data.morse_dict import sheet

def reverse_key_value(a = {1:'1'}):
    b = dict()
    for key in a:
        b[a[key]] = key
    return b

class Morse:
    def __init__(self, sheet = {}):
        self.sheet = reverse_key_value(sheet)
    def code(self, data):
        result = ''
        for i in data:
            result += self.sheet[i]
        return result + '00'
