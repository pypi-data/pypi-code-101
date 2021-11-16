# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smb']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.4.3', 'numpy>=1.21.4', 'torch>=1.10.0', 'torchvision>=0.11.1']

setup_kwargs = {
    'name': 'smb-optimizer',
    'version': '0.1.1',
    'description': 'Implementation for Pytorch of the method described in our paper "Bolstering Stochastic Gradient Descent with Model Building", S. Ilker Birbil, Ozgur Martin, Gonenc Onay, Figen Oztoprak, 2021 (see https://arxiv.org/abs/2111.07058)',
    'long_description': '# Stochastic Model Building (SMB)\n\nThis repository includes a new fast and robust stochastic optimization algorithm for training deep learning models. The core idea of the algorithm is based on building models with local stochastic gradient information. The details of the algorithm is given in our [recent paper](https://arxiv.org/abs/2111.07058).\n\n![SMB](./img/SMB_vs_SGD_and_Adam.png)\n\n**Abstract**\n\nStochastic gradient descent method and its variants constitute the core optimization algorithms that achieve good convergence rates for solving machine learning problems. These rates are obtained especially when these algorithms are fine-tuned for the application at hand. Although this tuning process can require large computational costs, recent work has shown that these costs can be reduced by line search methods that iteratively adjust the stepsize. We propose an alternative approach to stochastic line search by using a new algorithm based on forward step model building. This model building step incorporates a second-order information that allows adjusting not only the stepsize but also the search direction. Noting that deep learning model parameters come in groups (layers of tensors), our method builds its model and calculates a new step for each parameter group. This novel diagonalization approach makes the selected step lengths adaptive. We provide convergence rate analysis, and experimentally show that the proposed algorithm achieves faster convergence and better generalization in most problems. Moreover, our experiments show that the proposed method is quite robust as it converges for a wide range of initial stepsizes.\n\n_Keywords_: model building; second-order information; stochastic gradient descent; convergence analysis\n\n\n## Installation\n\n`pip install git+https://github.com/sbirbil/SMB.git`\n\n## Testing\n\nHere is how you can use SMB:\n\n```python\n\nimport smb\n\noptimizer = smb.SMB(model.parameters(), independent_batch=False) #independent_batch=True for SMBi optimizer\n\nfor epoch in range(100):\n    \n    # training steps\n    model.train()\n    \n    for batch_index, (data, target) in enumerate(train_loader):\n            \n        # create loss closure for smb algorithm\n        def closure():\n            optimizer.zero_grad()\n            loss = torch.nn.CrossEntropyLoss()(model(data), target)\n            return loss\n        \n        # forward pass\n        loss = optimizer.step(closure=closure)\n```\n\nYou can also check our [tutorial](https://github.com/sibirbil/SMB/blob/main/tutorial.ipynb) for a complete example (or the [Colab notebook](https://colab.research.google.com/drive/1wjUmy8-PmkBpnXxGKKEgSgmwN-VYY1xD#scrollTo=2skrH1RF_cbu) without installation). Set the hyper-parameter `independent_batch` to `True` in order to use the `SMBi` optimizer. Our [paper](http://www.optimization-online.org/DB_HTML/2021/11/8683.html) includes more information. \n\n## Reproducing The Experiments \n\nSee the following [script](smb/paper/reproducing_paper.py) in order to reproduce the results in our [paper](https://arxiv.org/abs/2111.07058).\n',
    'author': 'Ilker BIRBIL',
    'author_email': 's.i.birbil@uva.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sibirbil/SMB',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
