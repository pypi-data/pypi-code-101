"""
Copyright 2020 Odd Gunnar Aspaas

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import io
import tokenize
import re

def read_file(file_path):
    with open(file_path) as f:
        doc = f.read()
    return doc


def get_comments(doc):
    res = []
    stringio = io.StringIO(doc)

    for toktype, tokval, begin, end, line in tokenize.generate_tokens(stringio.readline):
        if toktype == tokenize.COMMENT: # inline comments
            res.append((toktype, tokval))
        elif toktype == tokenize.STRING:
            if tokval.startswith('"""') and tokval.endswith('"""'): # docstrings
                res.append((toktype, tokval))

    return tokenize.untokenize(res)


def file_contains_license(comments):
    keywords = ["copyright", "license"]
    comments = comments.lower()
    if any(keyword in comments for keyword in keywords):
        return True
    else:
        return False



def write_license_to_file(file, author, year=2021):
    LICENSE = f'''"""
Copyright {year} {author}

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""'''

    with open(file, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(LICENSE.rstrip('\r\n') + '\n' + '\n' + content)

