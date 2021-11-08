# coding: utf8

__all__ = ["Definition"]

from typing import TYPE_CHECKING

from .._content_provider import ContentProviderLayer
from ..data_grid._tools import get_output_and_data_grid_type
from ...tools import create_str_definition

if TYPE_CHECKING:
    from .._types import ExtendedParams, OptBool, OptDict


class Definition(ContentProviderLayer):
    """
    This class describe the universe (list of instruments), the fields (a.k.a. data items) and
    parameters that will be requested to the data platform

    Parameters:
    ----------
    universe : list
        The list of RICs
    fields : list
        List of fundamental field names
    parameters : dict, optional
        Global parameters for fields
    use_field_names_in_headers : bool, optional
        If value is True we add field names in headers.
    extended_params : dict, optional
        Other parameters can be provided if necessary

    Examples
    --------
     >>> from refinitiv.data.content import fundamental_and_reference
     >>> definition = fundamental_and_reference.Definition(["IBM"], ["TR.Volume"])
     >>> definition.get_data()

     Using get_data_async
     >>> import asyncio
     >>> task = asyncio.gather(
     ...    definition.get_data_async(),
     ...)
     >>> asyncio.get_event_loop().run_until_complete(task)
     >>> response, *_ = task.result()
    """

    def __init__(
        self,
        universe: list,
        fields: list,
        parameters: "OptDict" = None,
        use_field_names_in_headers: "OptBool" = False,
        extended_params: "ExtendedParams" = None,
    ):
        from .. import ContentType

        self.universe = universe
        self.fields = fields
        self.parameters = parameters
        self.use_field_names_in_headers = use_field_names_in_headers
        self.extended_params = extended_params

        output, data_grid_type = get_output_and_data_grid_type()
        super().__init__(
            content_type=ContentType.DATA_GRID,
            universe=self.universe,
            fields=self.fields,
            parameters=self.parameters,
            use_field_names_in_headers=self.use_field_names_in_headers,
            extended_params=self.extended_params,
            data_grid_type=data_grid_type,
            output=output,
        )

    def __repr__(self):
        return create_str_definition(
            self,
            middle_path="content",
            content=f"{{name='{self.universe}'}}",
        )
