from filemod import reader,writer


def number_detect(letter):
    """Detect the nature of letter is number or not"""

    try:
        int(letter)
        return True
    except :
        return False


def collab_words_in_list(list):
    """collab word into strings"""
    return ''.join(list)


def extract_keys(txt_file_data):
    """extract keys from file"""
    characters = list(txt_file_data)
    temp = []
    keys = []
    for index in range(len(characters)):
        if characters[index] == "\n":
            for value_index in range(index, len(characters)):
                if characters[value_index] == ":":
                    keys.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                if characters[value_index] not in [":", "\n", " "]:
                    temp.append(characters[value_index])

    return keys


def extract_values(txt_file_data):
    """extract values from file"""
    temp = []
    values = []
    characters = list(txt_file_data)

    for index in range(len(characters)):
        if characters[index] == ":":
            for value_index in range(index, len(characters)):
                if characters[value_index] == "\n":
                    values.append(collab_words_in_list(temp))
                    temp.clear()
                    break
                if characters[value_index] not in [":", "'", "\n", " ", '"']:
                    temp.append(characters[value_index])
    return values


def extract_data(data):
    """create a dictonary"""
    keys = extract_keys(data)
    values = extract_values(data)
    return {keys[index]: values[index] for index in range(len(keys))}


def load_txt(data):
    """compiling the text file"""
    from json_txt import compiler
    return compiler.compiles(data)


def edit_data(filename, key, value):
    if number_detect(value) == False:
        value = '"'+value+'"'
    data = reader(filename)
    keys = extract_keys(data)
    values = extract_values(data)
    temp = keys.index(key)
    values.pop(temp)
    values.insert(temp, value)
    writing_file = '{ \n'

    for size in range(len(keys)):
        writing_file = writing_file+str(keys[size])+":"+str(values[size])+"\n"
    writing_file = writing_file+"\n"+"}"
    writer(filename, writing_file, "w")
    return True


def add_data(filename, newkeys, newvalues):
    """append data into txt file"""
    if number_detect(newvalues) == False:
        newvalues = '"'+newvalues+'"'
    data = reader(filename)
    keys = extract_keys(data)
    values = extract_values(data)
    keys.append(newkeys)
    values.append(newvalues)
    write_file = "{ \n"
    for size in range(len(keys)):
        write_file = write_file+str(keys[size])+":"+str(values[size])+"\n"
    write_file = write_file+"\n"+"}"
    writer(filename, write_file, "w")
    return True

