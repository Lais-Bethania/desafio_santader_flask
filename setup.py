from distutils.core import setup

setup(
    name='desafio_santander',
    version='1.0',
    packages=['resources'],
    install_requires=['Flask-RESTful', 'flask'],
    license='GNU',
    author='Laís Bethania',
    author_email='laisbethania@gmail.com',
    description='REST app that prints Santander String'
)
