
class DTM :


    def encoding(self, key, text):
        text_result = ''
        for index in range(len(text)):
            let = text[index]
            ascii_code = ord(let)
            if let.isupper():
                text_result += chr((ord(let) + int(key) - 65) % 26 + 65)
            elif let.islower():
                text_result += chr((ord(let) + int(key) - 97) % 26 + 97)
            elif let.isdigit():
                shift_after = key
                if key == -10 or key == 10:
                    shift_after = key / 2
                text_result += chr((ord(let) + int(shift_after) - 48) % len({48: '0',49: '1',50: '2',51: '3',52: '4',53: '5',54: '6',55: '7',56: '8',57: '9',}) + 48)
            else:
                if ascii_code <= 47:
                    text_result += chr((ord(let) + int(key) - 32) % len({32: ' ',33: '!',34: '"',35: '#',36: '$',37: '%',38: '&',39: "'",40: '(',41: ')',42: '*',43: '+',44: ',',45: '-',46: '.',47: '/',}) + 32)
                elif 47 < ascii_code <= 64:
                    text_result += chr((ord(let) + int(key) - 58) % len({58: ':',59: ';',60: '<',61: '=',62: '>',63: '?',64: '@',}) + 58)
                elif 64 < ascii_code <= 96:
                    text_result += chr((ord(let) + int(key) - 91) % len({91: '[',92: '\\',93: ']',94: '^',95: '_',96: '`'}) + 91)
                elif 96 < ascii_code <= 126:
                    text_result += chr((ord(let) + int(key) - 123) % len({123: '{',124: '|',125: '}',126: '~'}) + 123)
        return text_result

    def decoding(self, key, text):
        text_result = ''
        key -= key * 2
        for index in range(len(text)):
            let = text[index]
            ascii_code = ord(let)
            if let.isupper():
                text_result += chr((ord(let) + int(key) - 65) % 26 + 65)
            elif let.islower():
                text_result += chr((ord(let) + int(key) - 97) % 26 + 97)
            elif let.isdigit():
                shift_after = key
                if key == -10 or key == 10:
                    shift_after = key / 2
                text_result += chr((ord(let) + int(shift_after) - 48) % len({48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8', 57: '9', }) + 48)
            else:
                if ascii_code <= 47:
                    text_result += chr((ord(let) + int(key) - 32) % len({32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')',42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', }) + 32)
                elif 47 < ascii_code <= 64:
                    text_result += chr((ord(let) + int(key) - 58) % len({58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', }) + 58)
                elif 64 < ascii_code <= 96:
                    text_result += chr((ord(let) + int(key) - 91) % len({91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`'}) + 91)
                elif 96 < ascii_code <= 126:
                    text_result += chr((ord(let) + int(key) - 123) % len({123: '{', 124: '|', 125: '}', 126: '~'}) + 123)
        return text_result

    def encoding_file(self, key, path , name_new_file):
        text_result = ''
        for text in open(path,'r').read().splitlines():
            for index in range(len(text)):
                let = text[index]
                ascii_code = ord(let)
                if let.isupper():
                    text_result += chr((ord(let) + int(key) - 65) % 26 + 65)
                elif let.islower():
                    text_result += chr((ord(let) + int(key) - 97) % 26 + 97)
                elif let.isdigit():
                    shift_after = key
                    if key == -10 or key == 10:
                        shift_after = key / 2
                    text_result += chr((ord(let) + int(shift_after) - 48) % len({48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8',57: '9', }) + 48)
                else:
                        if ascii_code <= 47:
                            text_result += chr((ord(let) + int(key) - 32) % len({32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(',41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', }) + 32)
                        elif 47 < ascii_code <= 64:
                            text_result += chr((ord(let) + int(key) - 58) % len({58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', }) + 58)
                        elif 64 < ascii_code <= 96:
                            text_result += chr((ord(let) + int(key) - 91) % len({91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`'}) + 91)
                        elif 96 < ascii_code <= 126:
                            text_result += chr((ord(let) + int(key) - 123) % len({123: '{', 124: '|', 125: '}', 126: '~'}) + 123)
            text_result += "\n"
        open(name_new_file + ".txt","a").write(text_result)
        return True

    def decoding_file(self, key, path, name_new_file):
        text_result = ''
        key -= key * 2
        for text in open(path,'r').read().splitlines():
            for index in range(len(text)):
                let = text[index]
                ascii_code = ord(let)
                if let.isupper():
                    text_result += chr((ord(let) + int(key) - 65) % 26 + 65)
                elif let.islower():
                    text_result += chr((ord(let) + int(key) - 97) % 26 + 97)
                elif let.isdigit():
                    shift_after = key
                    if key == -10 or key == 10:
                        shift_after = key / 2
                    text_result += chr((ord(let) + int(shift_after) - 48) % len({48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7', 56: '8',57: '9', }) + 48)
                else:
                    if ascii_code <= 47:
                        text_result += chr((ord(let) + int(key) - 32) % len({32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'", 40: '(', 41: ')',42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/', }) + 32)
                    elif 47 < ascii_code <= 64:
                        text_result += chr((ord(let) + int(key) - 58) % len({58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?', 64: '@', }) + 58)
                    elif 64 < ascii_code <= 96:
                        text_result += chr((ord(let) + int(key) - 91) % len({91: '[', 92: '\\', 93: ']', 94: '^', 95: '_', 96: '`'}) + 91)
                    elif 96 < ascii_code <= 126:
                        text_result += chr((ord(let) + int(key) - 123) % len({123: '{', 124: '|', 125: '}', 126: '~'}) + 123)
            text_result += "\n"
        open(name_new_file +'.txt',"a").write(text_result)
        return True
