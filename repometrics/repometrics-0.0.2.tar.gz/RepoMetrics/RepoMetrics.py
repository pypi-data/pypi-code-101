import json
import os
from pygments.lexers import guess_lexer_for_filename
from pygments.util import ClassNotFound


def main():
    path = "."
    language_dic = {}
    results = []
    all_length = 0
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            try:
                f = open(os.path.join(root, name), 'rb')
                content = f.read()
                language = guess_lexer_for_filename(name, content).name
                length = len(content)
                all_length += length
                if language_dic.get(language):
                    language_dic[language] += length
                else:
                    language_dic[language] = length
                result = {"path": os.path.join(root, name), "language": language}
                results.append(result)
            except ClassNotFound as e:
                pass
    print('summary: ')
    for k, v in language_dic.items():
        print(k + ': ' + str(v / all_length))
    print('results:')
    print(json.dumps(results, indent=4, sort_keys=True))


if __name__ == '__main__':
    main()

