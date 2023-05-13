from setuptools import setup

setup(
    name='cleaner',
    version='0.0.3',
    description='Good cleaner',
    url='http://github.com/dummy_user/useful',
    author='ST:AND',
    author_email='astoyan2002@gmail.com',
    license='MIT',
    packages=["clean_folder"],
    entry_points={'console_scripts':['clean-folder=clean_folder.clean:main']}
)
