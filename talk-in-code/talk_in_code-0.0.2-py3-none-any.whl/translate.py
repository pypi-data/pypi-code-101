import translator

def run(natural_text: str):
    code = translator.print_structure(natural_text)
    print(code)
    return code

if __name__ == '__main__':
    run('print fala pessoal')