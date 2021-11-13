from distutils.core import setup

long_des = """obj2html lib
=============================

You can use that lib to create html file from a .obj path:

    from obj2html import obj2html

    html_string = obj2html(obj_path)

    obj2html(obj_path, 'index.html')

    # firefox index.html

.. image:: https://gitlab.com/nicolalandro/obj2html/imgs/colab_sample.png
  :width: 400
  :alt: Colab example

Use in a Jupyter notebook to display a .obj 3D file:

    ! pip install obj2html
    
    ! wget https://gitlab.com/nicolalandro/obj2html/-/raw/main/test/assets/model.obj
    
    from obj2html import obj2html

    from IPython.display import display, HTML

    obj_path = 'model.obj'

    obj2html(obj_path, 'index.html')

    display(HTML('index.html'))

"""

setup(
  name = 'obj2html',
  packages = ['obj2html'],
  version = '0.4',
  license='MIT',
  description = 'Create an html with three.js that contains the given .obj file.',
  long_description = long_des,
  author = 'Nicola Landro',
  author_email = 'nicolaxx94@live.it',
  url = 'https://gitlab.com/nicolalandro/obj2html',
  keywords = ['3D', '.obj', '.html', 'jupyter', '3D viewer'],
)