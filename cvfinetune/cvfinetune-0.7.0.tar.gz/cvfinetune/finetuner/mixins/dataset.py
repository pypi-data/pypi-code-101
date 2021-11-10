import abc
import logging
import typing as T

from collections import namedtuple
from cvdatasets import AnnotationType
from cvdatasets.dataset.image import Size

from cvfinetune.finetuner.mixins.base import BaseMixin


class _DatasetMixin(BaseMixin):
    """
        This mixin is responsible for annotation loading and for
        dataset and iterator creation.
    """

    def __init__(self,
                 *args,
                 data: str,
                 dataset: str,
                 dataset_cls: T.Type,
                 dataset_kwargs_factory: T.Optional[T.Callable] = None,

                 label_shift: int = 0,
                 input_size: int = 224,
                 part_input_size:  T.Optional[int] = None,
                 **kwargs):

        super().__init__(*args, **kwargs)
        self.annot = None
        self.info_file = data
        self.dataset_name = dataset
        self.dataset_cls = dataset_cls
        self.dataset_kwargs_factory = dataset_kwargs_factory

        self.input_size = Size(input_size)

        if part_input_size is None:
            self.part_input_size = self.input_size

        else:
            self.part_input_size = Size(self.part_input_size)

        self._label_shift = label_shift


    def read_annotations(self):
        """Reads annotations and creates annotation instance, which holds important infos about the dataset"""
        opts = namedtuple("Opt", "data dataset")(self.info_file, self.dataset_name)
        self.annot = AnnotationType.new_annotation(opts, load_strict=False)
        self.dataset_cls.label_shift = self._label_shift

    def init_datasets(self):
        self._check_attr("prepare")
        self._check_attr("_center_crop_on_val")

        logging.info(" | ".join([
            f"Image input size: {self.input_size}",
            f"Parts input size: {self.part_input_size}",
        ]))

        self.train_data = self.new_dataset("train")
        self.val_data = self.new_dataset("test")


    @property
    def n_classes(self):
        return self.ds_info.n_classes + self._label_shift

    @property
    def data_info(self):
        assert self.annot is not None, "annot attribute was not set!"
        return self.annot.info

    @property
    def ds_info(self):
        return self.data_info.DATASETS[self.dataset_name]

    def new_dataset(self, subset: str):
        """Creates a dataset for a specific subset and certain options"""
        if self.dataset_kwargs_factory is not None and callable(self.dataset_kwargs_factory):
            kwargs = self.dataset_kwargs_factory(subset)
        else:
            kwargs = dict()

        kwargs = dict(kwargs,
            subset=subset,
            dataset_cls=self.dataset_cls,
            prepare=self.prepare,
            size=self.input_size,
            part_size=self.part_input_size,
            center_crop_on_val=self._center_crop_on_val,
        )


        ds = self.annot.new_dataset(**kwargs)
        logging.info(f"Loaded {len(ds)} images")
        return ds


