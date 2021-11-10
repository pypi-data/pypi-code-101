from fastapi.testclient import TestClient

from toolip.utils.redoc import make_docs_router


def test_make_docs_router():
    router = make_docs_router(
        title='Test Doc',
        description='',
        logo_url='',
        logo_alt_text='test logo',
        tags_and_models=[],
    )

    client = TestClient(router)
    redoc_response = client.get('/redoc')
    assert redoc_response.status_code == 200

    openapi_response = client.get('/openapi.json')
    assert openapi_response.status_code == 200
    assert openapi_response.json()['info']['title'] == 'Test Doc'
