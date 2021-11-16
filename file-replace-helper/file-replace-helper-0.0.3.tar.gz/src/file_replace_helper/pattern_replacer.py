from typing import List


class Replace:
    """ replace_with ===== regex pattern to replace
    replace_on ==== regex pattern to replace with
    replace_all ==== replace all required if regex pattern matches early and
     there is still more pattern to be replaced, use this to fully replace
    """
    def __init__(self, replace_with: str, replace_on: str, replace_all=False):
        self.replace_with = replace_with
        self.replace_on = replace_on
        self.replace_all = replace_all


class PatternReplace:
    def __init__(self, path: str, replacer: List[Replace]):
        self.path = path
        if len(replacer) == 0:
            print(f'no replace patterns specified for path {path}')
            exit(1)
        self.replacer = replacer
