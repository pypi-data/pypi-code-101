from distutils.core import setup

# it do not work on install
# import os
# with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pipy_readme.rst'), 'r') as f:
#   long_des = f.read()
long_des = """obj2html lib
=============================

You can use that lib to create html file from a .obj path: 

.. code-block:: python

    from obj2html import obj2html
    obj2html('model.obj', 'index.html')
    # firefox index.html


.. image:: https://gitlab.com/nicolalandro/obj2html/-/raw/main/imgs/colab_sample.png
  :alt: Colab example

Use in a Jupyter notebook to display a .obj 3D file:

.. code-block:: python

    ! pip install obj2html
    ! wget https://gitlab.com/nicolalandro/obj2html/-/raw/main/test/assets/model.obj
    from obj2html import obj2html
    from IPython.display import display, HTML
    obj2html('model.obj', 'index.html')
    display(HTML('index.html'))

It is also possible to set the scale factor, light and camera options:

.. code-block:: python

    camera={
      "fov": 45,
      "aspect": 2,
      "near": 0.1,
      "far": 100,
      "pos_x": 0,
      "pos_y": 10,
      "pos_z": 20,
      "orbit_x": 0,
      "orbit_y": 5,
      "orbit_z": 0,
    },
    light={
      "color": "0xFFFFFF",
      "intensity": 1,
      "pos_x": 0,
      "pos_y": 10,
      "pos_z": 0,
      "target_x": -5,
      "target_y": 0,
      "target_z": 0,
    },
    obj_options={
      "scale_x": 30,
      "scale_y": 30,
      "scale_z": 30,
    }
    obj2html('model.obj', 'index.html', camera, light, obj_options)
"""

setup(
  name = 'obj2html',
  packages = ['obj2html'],
  version = '0.8',
  license='MIT',
  description = 'Create an html with three.js that contains the given .obj file.',
  long_description = long_des,
  author = 'Nicola Landro',
  author_email = 'nicolaxx94@live.it',
  url = 'https://gitlab.com/nicolalandro/obj2html',
  keywords = ['3D', '.obj', '.html', 'jupyter', '3D viewer'],
  project_urls={
    'Source': 'https://gitlab.com/nicolalandro/obj2html',
  },
)