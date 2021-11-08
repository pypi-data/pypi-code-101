# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metamaker',
 'metamaker.commands',
 'metamaker.commands.run',
 'metamaker.commands.sagemaker']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.19.9,<2.0.0',
 'fastapi>=0.70.0,<0.71.0',
 'pydantic>=1.8.2,<2.0.0',
 'pyyaml>=5.0,<6.0',
 'sagemaker[local]>=2.68.0,<3.0.0',
 'uvicorn>=0.15.0,<0.16.0']

entry_points = \
{'console_scripts': ['metamaker = metamaker.__main__:run']}

setup_kwargs = {
    'name': 'metamaker',
    'version': '0.1.0',
    'description': 'Simple CLI to train and deploy your ML models with AWS SageMaker',
    'long_description': 'metamaker\n=========\n\n[![Actions Status](https://github.com/altescy/metamaker/workflows/CI/badge.svg)](https://github.com/altescy/metamaker/actions/workflows/main.yaml)\n[![License](https://img.shields.io/github/license/altescy/metamaker)](https://github.com/altescy/metamaker/blob/master/LICENSE)\n\nSimple command line tool to train and deploy your machine learning models with AWS SageMaker\n\n## Features\n\nmetamaker enables you to:\n\n- Build a docker image for training and inference with [poetry](https://python-poetry.org/) and [FastAPI](https://fastapi.tiangolo.com/)\n- Train your own machine learning model with SageMaker\n- Deploy inference endpoint with SageMaker\n\n## Usage\n\n1. Create poetry project and install metamaker\n\n```\n❯ poetry new your_module\n❯ cd your_module\n❯ poetry add git+https://github.com/altescy/metamaker#main\n```\n\n2. Define scripts for traning and inference in `main.py`\n\n```main.py\nfrom pathlib import Path\nfrom typing import Any, Dict\n\nfrom metamaker import MetaMaker\n\nfrom your_module import Model, Input, Output\n\napp = MetaMaker[Model, Input, Output]()\n\n@app.trainer\ndef train(\n    dataset_path: Path,\n    artifact_path: Path,\n    hyperparameters: Dict[str, Any],\n) -> None:\n    model = Model(**hyperparameters)\n    model.train(dataset_path / "train.csv")\n    model.save(artifact_path / "model.tar.gz")\n\n@app.loader\ndef load(artifact_path: Path) -> Model:\n    return Model.load(artifact_path / "model.tar.gz")\n\n@app.predictor\ndef predict(model: Model, data: Input) -> Output:\n    return model.predict(data)\n```\n\n3. Write metamaker configs in `metamaker.yaml`\n\n```metamaker.yaml\nhandler: main:app\ndataset_path: s3://your-bucket/path/to/dataset/\nartifact_path: s3://your-bucket/path/to/artifacts/\nhyperparameter_path: ./hparams.yaml\n\nimage:\n  name: metamaker\n  includes:\n    - your_module/\n    - main.py\n  excludes:\n    - __pycache__/\n    - \'*.py[cod]\'\n\ntraining:\n  execution_role: arn:aws:iam::xxxxxxxxxxxx:role/SageMakerExecutionRole\n  instance:\n    type: ml.m5.large\n    count: 1\n\ninference:\n  endpoint_name: your_endpoint\n  instance:\n    type: ml.t2.meduim\n    count: 1\n```\n\n4. Build docker image and push to ECR\n\n```\nmetamaker build --deploy .\n```\n\n5. Train your model with SageMaker and deploy endpoint\n\n```\nmetamker sagemaker train --deploy\n```\n',
    'author': 'altescy',
    'author_email': 'altescy@fastmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/altescy/metamaker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
