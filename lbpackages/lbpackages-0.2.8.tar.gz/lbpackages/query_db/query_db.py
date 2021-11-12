"""Function to retrieve stocks data from DB."""
from sqlalchemy.sql import text


def query_db(dbclient):
    """Retrieves stocks data from the DB.

    Parameters
    ----------
    dbclient: lbpackages.models.dbclient
        is a dbclient object to interact with the db.
    Returns
    -------
    pd.DataFrame
        a DataFrame containing the required information.
    """
    query = text(
        "select date, symbol, close from stock_value where date > DATE(NOW()) - 7 order by date asc"
    )

    return dbclient.to_frame(sql=query)
