from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import str
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from future import standard_library
standard_library.install_aliases()
import uuid

import pytest
from gcloud.rest.auth import BUILD_GCLOUD_REST  # pylint: disable=no-name-in-module
from gcloud.rest.storage import Storage

# Selectively load libraries based on the package
if BUILD_GCLOUD_REST:
    from requests import Session
else:
    from aiohttp import ClientSession as Session


#@pytest.mark.asyncio
def test_metadata_multipart(bucket_name, creds):
    object_name = '{}/{}.txt'.format((uuid.uuid4().hex), (uuid.uuid4().hex))
    original_data = '{}'.format((uuid.uuid4().hex))
    original_metadata = {'Content-Disposition': 'inline',
                         'metadata':
                         {'a': 1,
                          'b': 2,
                          'c': [1, 2, 3],
                          'd': {'a': 4, 'b': 5}}}
    # Google casts all metadata elements as string.
    google_metadata = {'Content-Disposition': 'inline',
                       'metadata':
                       {'a': str(1),
                        'b': str(2),
                        'c': str([1, 2, 3]),
                        'd': str({'a': 4, 'b': 5})}}

    with Session() as session:
        storage = Storage(service_file=creds, session=session)

        # Without metadata
        res0 = storage.upload(bucket_name, object_name, original_data,
                                    force_resumable_upload=False)
        data0 = storage.download(bucket_name, res0['name'])
        storage.download_metadata(bucket_name, res0['name'])

        # With metadata
        res = storage.upload(bucket_name, object_name, original_data,
                                   metadata=original_metadata)
        data = storage.download(bucket_name, res['name'])
        data_metadata = storage.download_metadata(bucket_name,
                                                        res['name'])

        assert res['name'] == object_name
        assert str(data, 'utf-8') == original_data
        assert data == data0

        assert data_metadata.pop('contentDisposition') == 'inline'
        assert data_metadata['metadata'] == google_metadata['metadata']


#@pytest.mark.asyncio
def test_metadata_resumable(bucket_name, creds):
    object_name = '{}/{}.txt'.format((uuid.uuid4().hex), (uuid.uuid4().hex))
    original_data = '{}'.format((uuid.uuid4().hex))
    original_metadata = {'Content-Disposition': 'inline',
                         'metadata':
                         {'a': 1,
                          'b': 2,
                          'c': [1, 2, 3],
                          'd': {'a': 4, 'b': 5}}}
    # Google casts all metadata elements as string.
    google_metadata = {'Content-Disposition': 'inline',
                       'metadata':
                       {'a': str(1),
                        'b': str(2),
                        'c': str([1, 2, 3]),
                        'd': str({'a': 4, 'b': 5})}}

    with Session() as session:
        storage = Storage(service_file=creds, session=session)

        # Without metadata
        res0 = storage.upload(bucket_name, object_name, original_data,
                                    force_resumable_upload=True)
        data0 = storage.download(bucket_name, res0['name'])
        storage.download_metadata(bucket_name, res0['name'])

        # With metadata
        res = storage.upload(bucket_name, object_name, original_data,
                                   metadata=original_metadata,
                                   force_resumable_upload=True)
        data = storage.download(bucket_name, res['name'])
        data_metadata = storage.download_metadata(bucket_name,
                                                        res['name'])

        assert res['name'] == object_name
        assert str(data, 'utf-8') == original_data
        assert data == data0

        assert data_metadata.pop('contentDisposition') == 'inline'
        assert data_metadata['metadata'] == google_metadata['metadata']


#@pytest.mark.asyncio
def test_metadata_copy(bucket_name, creds):
    object_name = '{}/{}.txt'.format((uuid.uuid4().hex), (uuid.uuid4().hex))
    copied_object_name = '{}.copy'.format((object_name))
    original_data = '{}'.format((uuid.uuid4().hex))
    original_metadata = {'Content-Disposition': 'inline',
                         'metadata':
                         {'a': 1,
                          'b': 2,
                          'c': [1, 2, 3],
                          'd': {'a': 4, 'b': 5}}}
    # Google casts all metadata elements as string.
    google_metadata = {'Content-Disposition': 'inline',
                       'metadata':
                       {'a': str(1),
                        'b': str(2),
                        'c': str([1, 2, 3]),
                        'd': str({'a': 4, 'b': 5})}}

    with Session() as session:
        storage = Storage(service_file=creds, session=session)

        # Without metadata
        res0 = storage.upload(bucket_name, object_name, original_data,
                                    force_resumable_upload=True)
        data0 = storage.download(bucket_name, res0['name'])

        storage.copy(bucket_name, object_name, bucket_name,
                           new_name=copied_object_name,
                           metadata=original_metadata)

        data = storage.download(bucket_name, copied_object_name)
        data_metadata = storage.download_metadata(
            bucket_name, copied_object_name
        )

        assert data == data0

        assert data_metadata.pop('contentDisposition') == 'inline'
        assert data_metadata['metadata'] == google_metadata['metadata']
