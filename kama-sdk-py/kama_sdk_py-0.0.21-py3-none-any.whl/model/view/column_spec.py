from typing import Any, Optional

from kama_sdk.model.base.mc import KOD_KW, ATTR_KW
from kama_sdk.model.base.model import Model
from kama_sdk.model.base.model_decorators import model_attr
from kama_sdk.model.supplier.base.supplier import Supplier
from kama_sdk.model.view.view_spec import ViewSpec, SPEC_KEY
from kama_sdk.utils.logging import lerr
from kama_sdk.utils.utils import cautiously

class ColumnSpec(Model):

  @model_attr(cached=True)
  def get_key(self):
    return self.get_attr(KEY_KEY) or self.get_id()

  @model_attr(cached=True)
  def get_transformer(self) -> Optional[Supplier]:
    """
    Optional reference to a Supplier to transform the row data.
    :return:
    """
    return self.get_attr(TRANSFORMER_KEY)

  def finalize_data_item(self, item_data: Any) -> Any:
    """
    Transforms the row item given the parent table (e.g TableViewSpec),
    typically to let you re-used views. The transformer is simply
    a Supplier that, when hard-patched with `source`, should
    return a new value that will be used by the view spec.
    :param item_data:
    :return:
    """
    if transformer := self.get_transformer():
      transformer.write_source_data(item_data)
      result, error = cautiously(lambda: transformer.resolve())
      if error:
        msg = f"transformer {transformer.sig()} raised"
        lerr(msg, exc=True, sig=self.sig())
      return item_data if error else result
    else:
      return item_data

  def get_primed_view_spec(self, item_data: Any) -> ViewSpec:
    """
    Called by the parent table (e.g TableViewSpec) when it
    needs to render a cell in this column. Accepts an `item_data`
    that represents the row item, loads a view spec with the `item_data`
    strong-patched into it as "item".
    :param item_data:
    :return:
    """
    final_data = self.finalize_data_item(item_data)
    if VIEW_SPEC_KEY in self.get_config().keys():
      spec = self.get_attr(VIEW_SPEC_KEY)
      model = ViewSpec.inflate({SPEC_KEY: spec, ITEM_KEY: final_data})
      model.set_parent(self)
      return model
    else:
      return self.inflate_child(
        ViewSpec,
        attr=VIEW_SPEC_MODEL_KEY,
        patch={ITEM_KEY: final_data}
      )


ITEM_KEY = "item"
KEY_KEY = "key"
VIEW_SPEC_KEY = "view_spec"
VIEW_SPEC_MODEL_KEY = "view_spec_model"
TRANSFORMER_KEY = "data_transformer"
