from dataclasses import dataclass
from typing import List, Optional, Type, Union

from apispec import APISpec
from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html
from pydantic import BaseModel
from pydantic.schema import schema
from starlette.responses import JSONResponse


@dataclass
class TagAndModels:
    models: Union[Type[BaseModel], List[Type[BaseModel]]]
    tag: Optional[str] = None
    description: Optional[str] = None


def _model_to_doc_str(model: Type[BaseModel], title: bool = False):
    clsname = model.__name__
    schema_title = f'## {clsname}\n'
    schema_description = model.__doc__ + '\n' if model.__doc__ is not None else ''
    # The double return carriage is important. DO NOT REMOVE THEM.
    schema_ref = f'<SchemaDefinition schemaRef="#/components/schemas/{clsname}"/>\n\n'
    if title:
        return f'{schema_title}{schema_description}{schema_ref}'

    return f'{schema_description}{schema_ref}'


def make_docs_router(
    title: str,
    description: str,
    logo_url: str,
    logo_alt_text: str,
    tags_and_models: List[TagAndModels],
) -> APIRouter:
    """Creates a FastAPI docs router.

    Args:
        title: Title of the API documentation page.
        description: Description section for the API documentation.
        logo_url: URL to a logo to use in the API documentation.
        logo_alt_text: Alternate text to the logo.
        tags_and_models: A list of TagAndModels.

    Returns:
        The generated APIRouter.
    """
    tags = []
    models = []
    for t_n_m in tags_and_models:
        tag_description = t_n_m.description + '\n' if t_n_m.description else ''
        if isinstance(t_n_m.models, list):
            for model in t_n_m.models:
                models.append(model)
                tag_description += _model_to_doc_str(model=model, title=True)
        else:
            model = t_n_m.models
            models.append(model)
            tag_description += _model_to_doc_str(model=model)
        if t_n_m.tag is None:
            continue
        tags.append(
            {
                'name': t_n_m.tag,
                'description': tag_description,
            }
        )

    custom = {
        'tags': tags,
        'x-tagGroups': [{'name': 'Models', 'tags': [tag['name'] for tag in tags]}],
    }

    model_docs = APISpec(
        title=title,
        version='1.0',
        openapi_version='3.0.0',
        info={'description': description, 'x-logo': {'url': logo_url, 'altText': logo_alt_text}},
        **custom,
    )

    for model in models:
        model_docs.components.schema(
            model.__name__,
            # Place the model definition in the right place for redoc to be happy
            # and set the relative reference.
            schema([model], ref_prefix='#/components/schemas/')['definitions'][model.__name__],
        )

    router = APIRouter()

    @router.get('/openapi.json', include_in_schema=False)
    async def spec():
        return JSONResponse(model_docs.to_dict())

    @router.get('/redoc', include_in_schema=False)
    async def redoc():
        return get_redoc_html(openapi_url='openapi.json', title=title)

    return router
