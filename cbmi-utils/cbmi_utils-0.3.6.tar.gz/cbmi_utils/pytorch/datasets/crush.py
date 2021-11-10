from pathlib import Path
from typing import Callable, Optional

from .h5_dataset import H5Dataset


class Crush96x96(H5Dataset):
    """
    Data and further information can be found at TODO
    """

    def __init__(self, root: str, sub_set: str, transform: Optional[Callable] = None, transform_target: Optional[Callable] = None):
        assert sub_set in ['train', 'valid', 'test']

        super().__init__(data_path=Path(root) / f'{sub_set}.h5',
                         data_key='image',
                         target_path=Path(
                             root) / f'{sub_set}.h5',
                         target_key='label',
                         transform=transform,
                         transform_target=transform_target)

        self.classes = ['C', 'T']  # C=crush and T=tumor

    @classmethod
    def from_avocado(cls, sub_set: str = 'train', transform: Optional[Callable] = None, transform_target: Optional[Callable] = None):
        return cls('/data/ldap/histopathologic/processed_read_only/Crush_96', sub_set, transform, transform_target)

    @staticmethod
    def normalization_values():
        raise NotImplementedError("To be implemented")
