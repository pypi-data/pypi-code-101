# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gfluent']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.3.0,<3.0.0',
 'google-cloud-bigquery>=2.13.1,<3.0.0',
 'google-cloud-storage>=1.37.1,<2.0.0']

setup_kwargs = {
    'name': 'gfluent',
    'version': '0.1.16',
    'description': 'A fluent API for Google Cloud Python Client',
    'long_description': '# Google Cloud Fluent Client\n\n[![UT & SIT](https://github.com/simple-dev-tools/gfluent/actions/workflows/ut-and-sit.yml/badge.svg?branch=develop)](https://github.com/simple-dev-tools/gfluent/actions/workflows/ut-and-sit.yml)\n\nThis is a lightweight wrapper on top of Google Cloud Platform Python SDK client library. It provides\na fluent-style to call the methods. The motivation is, too many parameters for GCP `Storage` and\n`BigQuery` library, and most of them are ok to be set as default values. \n\nThis wrapper is suitable for Data Engineers to quickly create simple data pipeline based on GCP\n`BigQuery` and `Storage`, here are two examples.\n\n\n## Build Data Pipeline on BigQuery\n\nYou (A Data Engineer) are asked to,\n\n- load multiple `json` files from your local drive to GCS\n\n- import those files to a BigQuery staging table\n\n- run another query based on the staging table by joining existing tables, and store the result to another table\n\n\nTo accomplish the task, here are the source code,\n\n```python\n\nfrom gfluent import BQ, GCS\n\nproject_id = "here-is-you-project-id"\nbucket_name = "my-bucket"\ndataset = "sales"\ntable_name = "products"\nprefix = "import"\nlocal_path = "/user/tom/products/" # there are many *.json files in this directory\n\n# uplaod files to GCS bucket\n(\n    GCS(project_id)\n    .local(path=local_path, suffix=".json" )\n    .bucket(bucket_name)\n    .prefix(prefix)\n    .upload()\n)\n\n# if you need to create the dataset\nBQ(project_id).create_dataset(dataset, location="US")\n\n# load data to BigQuery table\n\nuri = f"gs://{bucket_name}/{prefix}/*.json"\nnumber_of_rows = (\n    BQ(project_id)\n    .table(f"{dataset}.{table_name}")\n    .mode("WRITE_APPEND")               # don\'t have to, default mode\n    .create_mode("CREATE_IF_NEEDED")    # don\'t have to, default mode\n    .format("NEWLINE_DELIMITED_JSON")   # don\'t have to, default format\n    .gcs(uri).load(location="US")\n)\n\nprint(f"{number_of_rows} rows are loaded")\n\n\n# run a query\n\nfinal_table = "sales_summary"\n\nsql = """\n    select t1.col1, t2.col2, t2.col3\n    FROM\n        sales.products t1\n    JOIN\n        other.category t2\n    ON  t1.prod_id = t2.prod_id\n"""\n\nnumber_of_rows = (\n    BQ(product_id)\n    .table(f"{dataset}.{final_table}")\n    .sql(sql)\n    .create_mode("CREATE_NEVER")    # have to, don\'t want to create new table\n    .query()\n)\n\nprint(f"{number_of_rows} rows are appended")\n\n\n# now let\'s query the new table\n\nrows = (\n    BQ(product_id)\n    .sql(f"select col1, col2 from {dataset}.{final_table} limit 10")\n    .query()\n)\n\nfor row in rows:\n    print(row.col1, row.col2)\n```\n\n\n## Loading data from Spreadsheet to BigQuery\n\n```python\nimport os\nfrom gfluent import Sheet, BQ\n\nproject_id = \'your project id\'\nsheet_id = \'your Google sheet id`\n\n# assume the data is on the sheet `data` and range is `A1:B4`\nsheet = Sheet(\n    os.getenv("GOOGLE_APPLICATION_CREDENTIALS")\n).sheet_id(sheet_id).worksheet("data!A1:B4")\n\nbq = BQ(project=project_id).table("target_dataset.table")\n\nsheet.bq(bq).load(location="EU")\n```\n\n## Documents\n\nHere is the [document](https://gfluent.readthedocs.io/en/latest/#), and please refer to the test\ncases to see more real examples.\n\n\n## Installation\n\n\nInstall from PyPi,\n\n```bash\npip install -U gfluent\n```\n\nOr build and install from source code,\n\n```bash\npip install -r requirements-dev.txt\npoetry build\npip install dist/gfluent-<versoin>.tar.gz\n```\n\n\n## Contribution\n\nAny kinds of contribution is welcome, including report bugs, add feature or enhuance document. Please\nbe noted, the Integration Test is using a real GCP project, and you may not have the permission to\nset up the test data.\n',
    'author': 'Simple Dev Tools',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/simple-dev-tools/gfluent',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.10',
}


setup(**setup_kwargs)
