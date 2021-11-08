# """
# Image uploader for pixhost.to
# """

# from ...utils import html, http, types
# from .base import ImageHostBase

# import logging  # isort:skip
# _log = logging.getLogger(__name__)


# class PixhostImageHost(ImageHostBase):
#     """Upload images to pixhost.to"""

#     name = 'pixhost'

#     default_config = {
#         'base_url': 'https://api.pixhost.to',
#         'thumb_width': types.Integer(150, min=150, max=500),
#     }

#     # The file path is unique enough
#     cache_id = None

#     async def _upload(self, image_path):
#         return {
#             'url': 'foo',
#         }

#         # try:
#         #     response = await http.post(
#         #         url=self.options['base_url'] + '/images',
#         #         cache=False,
#         #         data={
#         #             'content_type': '1',
#         #             'max_th_size': self.options['thumb_width'],
#         #         },
#         #         files={
#         #             'img': image_path,
#         #         },
#         #     )
#         # except errors.RequestError as e:
#         #     # Reference: https://pixhost.to/api/index.html?shell#errors
#         #     if e.status_code == 413:
#         #         raise errors.RequestError('File size limit exceeded (10 MiB)')
#         #     else:
#         #         raise e

#         # else:
#         #     _log.debug('%s: Response: %r', self.name, response)
#         #     info = response.json()
#         #     _log.debug('%s: JSON: %r', self.name, info)
#         #     try:
#         #         return {
#         #             # We don't get an image URL; get it from the HTML
#         #             'url': self._get_image_url(info['show_url']),
#         #             'thumbnail_url': info['th_url'],
#         #         }
#         #     except KeyError:
#         #         raise RuntimeError(f'Unexpected response: {info}')

#     async def _get_image_url(self, html_url):
#         response = await http.get(html_url, cache=False)
#         doc = html.parse(response)
#         img_tag = doc.find('img', id='image')
#         _log.debug('Image tag: %r', img_tag)
#         if img_tag and img_tag.get('src'):
#             return img_tag['src']
#         else:
#             raise RuntimeError(f'Failed to find image: {html_url}')
