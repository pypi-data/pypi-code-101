import tempfile
from PIL import Image


def form_image_helper(caption_list, dummy=True, image_suffix='.jpg'):
    """
    :param caption_list: <class 'list'>
    :param dummy: <class 'bool'>
    :param image_suffix: <class 'str'>
    :return: <class 'dict'> [dict of dummy images for form submission in django unittest]
    """
    try:
        res = {}
        image = Image.new('RGB', (100, 100))
        tmp_file = tempfile.NamedTemporaryFile(suffix=image_suffix)
        image.save(tmp_file)
        with open(tmp_file.name, 'rb') as fp:
            for title in caption_list:
                res[title] = fp
        return res
    except Exception as e:
        print(str(e))
        raise ValueError(str(e))

