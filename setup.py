from setuptools import setup

setup(
    name='CanIStreamIt',
    version='0.2',
    url='https://github.com/Bulv1ne/CanIStreamIt',
    license='MIT',
    author='Niels Lemmens',
    author_email='draso.odin@gmail.com',
    description='Can I Stream It api',
    packages=['canistreamit'],
    platforms='any',
    install_requires=[
        'requests>=2.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
