from __future__ import absolute_import, annotations
from typing import Any, Dict, Optional, Union
from urllib.parse import urlencode

import pandas as pd
import requests

from .api_config import ApiConfig
from . import common


def get_history(
        issuer_id: str,
        output_format: Optional[str] = None,
        api_key: Optional[str] = None) -> Union[pd.DataFrame, str, Dict[str, Any]]:
    """
    Get latest point-in-time snapshot of our data-driven predictions for all issuers along
    with associated metadata.

    Args:
        issuer_id:                      
        output_format:                  One-of 'pandas', 'json', or 'csv'.
        api_key:                        Your Migrations.ML API key.

    Returns:
        Union[DataFrame, str, Dict[str, Any]]


    """

    api_key = common.get_api_key(api_key)
    output_format = common.get_output_format(output_format)

    query_params = {
        'api_key': api_key,
        'issuer_id': issuer_id
    }

    url = ApiConfig.endpoint_base + '/history?' + urlencode(query_params)

    try:

        response = requests.get(url)

    except Exception as error:
        raise ConnectionError(
            'Failed to make request to Migrations.ML API: %s', error) from error

    if not response.ok:

        raise RuntimeError(
            'Migrations.ML API returned bad response: %s', response.reason)

    response_body = response.json()

    if response_body['status'] != 'success':

        raise RuntimeError('Migrations.ML API returned bad status')

    if output_format == 'json':

        return response_body

    dataframe = pd.DataFrame([
        {
            'migrations_issuer_id': response_body['result']['migrations_issuer_id'],
            'ticker': response_body['result']['ticker'],
            'name': response_body['result']['name'],
            'lei': response_body['result']['lei'],
            'exchange': response_body['result']['exchange'],
            'rating': response_body['result']['rating'],
            'rating_class': response_body['result']['rating_class'],
            'sic_code': response_body['result']['sic_code'],
            'industry': response_body['result']['industry'],
            **{k: v for k, v in row.items() if k not in 'transparency_factors'},
            'transparency_equity_performance': row['transparency_factors']['equity_performance'],
            'transparency_leverage': row['transparency_factors']['leverage'],
            'transparency_macro': row['transparency_factors']['macro'],
            'transparency_market_value': row['transparency_factors']['market_value'],
            'transparency_profitability': row['transparency_factors']['profitability'],
            'transparency_solvency': row['transparency_factors']['solvency'],
        }
        for row in response_body['result']['timeseries']
    ])

    if output_format == 'csv':

        return dataframe.to_csv(index=False)

    assert output_format == 'pandas'

    return dataframe
