from pollination.annual_sky_radiation.entry import AnnualSkyRadiationEntryPoint
from queenbee.recipe.dag import DAG


def test_annual_sky_radiation():
    recipe = AnnualSkyRadiationEntryPoint().queenbee
    assert recipe.name == 'annual-sky-radiation-entry-point'
    assert isinstance(recipe, DAG)
