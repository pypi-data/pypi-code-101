from io import BytesIO
from warnings import warn
from typing import Iterable, List, Optional, Text
import requests
from requests.models import Response
from PIL import Image
from PIL.ImageFile import ImageFile

from nasa.exceptions import NASAContentTypeNotImage
from nasa.warnings import InvalidInputWarning


def get_url_image(url: Text, ignore_non_image: bool = False) -> Optional[ImageFile]:
    """Parse Response Content Image to PIL Image

    Args:
        url (Text): URL containing image
        ignore_non_image (bool, optional): If True, Gave warning but return None, else raise an error. Defaults to False.

    Raises:
        NASAContentTypeNotImage: The response content type is not image.

    Returns:
        ImageFile: PIL ImageFile Object
    """
    response: Response = requests.get(url)
    content_type: Text = response.headers.get("Content-Type")
    if content_type.split("/")[0] == "image":
        content: bytes = response.content
        image: ImageFile = Image.open(BytesIO(content))
        return image
    elif ignore_non_image:
        message: Text = u"Response Content-Type is not Image."
        warn(message, InvalidInputWarning)
        return None
    else:
        message: Text = u"Response Content-Type is not Image."
        raise NASAContentTypeNotImage(message)


def get_urls_images(
    urls: Iterable[Text], ignore_non_image: bool = False
) -> List[Optional[ImageFile]]:
    """Parse response contents from list of urls to list of image

    Args:
        urls (Iterable[Text]): List of URLs containing images
        ignore_non_image (bool, optional): If True, Gave warning but return None, else raise an error. Defaults to False.

    Returns:
        List[Optional[ImageFile]]: List of PIL ImageFile Object
    """
    return [get_url_image(url, ignore_non_image) for url in urls]
