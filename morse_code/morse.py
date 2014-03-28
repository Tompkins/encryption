from data.morse_dict import sheet

def reverse_key_value(a = {1:'1'}):
    b = dict()
    for key in a:
        b[a[key]] = key
    return b

class Morse:
    def __init__(self, sheet = {}):
        self.sheet = sheet
    def code(self, data):
        pass
