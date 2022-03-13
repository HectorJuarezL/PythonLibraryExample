from distutils.core import setup
setup(
  name = 'libreria',         # How you named your package folder (MyLib)
  packages = ['libreria'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Example of Library ',   # Give a short description about your library
  author = 'Author name',                   # Type in your name
  author_email = 'fake@email.com',      # Type in your E-Mail
  url = 'https://github.com/url',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/url',
  keywords = ['library', 'keyword1', 'keyword2','keyword3'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'py7zr'
      ],
  extras_require = { #pip install libreria["componente extra"]
        "full" :["tensorflow","torch"],
        "tf":  ["tensorflow"],
        "torch": ["torch"],
        ":python_version<'3.8'": ["pickle5"]
    },
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',      #Specify which pyhton versions that you want to support
  ],
)

#los siguientes tres comandos son para subir la libreria a pypi
#pip install twine
#python setup.py sdist
#twine upload dist/*


#el siguiente comando es solo para instalarla
#python setup.py install