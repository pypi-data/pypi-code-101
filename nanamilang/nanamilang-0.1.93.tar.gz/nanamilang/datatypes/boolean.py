"""NanamiLang Boolean Data Type"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

from .base import Base


class Boolean(Base):
    """NanamiLang Boolean Data Type Class"""

    name: str = 'Boolean'
    _expected_type = bool
    _python_reference: bool = None

    def __init__(self, reference: bool) -> None:
        """NanamiLang Boolean, initialize new instance"""

        super(Boolean, self).__init__(reference=reference)

    def format(self):
        """NanamiLang Boolean, format() method implementation"""

        return f'{"true" if self.reference() is True else "false"}'
