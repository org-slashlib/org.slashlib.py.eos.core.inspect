## frameworks ##

### [python](https://www.python.org/) ###

This package is written in python and requires a matching environment.

### [python virtual environment]() ###

Use pythons virtual environment to setup a clean and cloned python environment, separated from the python environment installed on your system.  

For accessing custom pypi repositories during installation, you can add a <code>pip.ini</code> file into the virtual environments root.

```ini
[install]
extra-index-url =
    http://<user>:<access-token>@gitlab.example.domain/api/v4/projects/<projectid:int>/packages/pypi/simple

trusted-host =
    gitlab.example.domain

```

### [linting with flake8](https://pypi.org/project/flake8/) ###

Code analysis for improving code quality and, if activated in the editor, for faster detection of errors.
<code>pip install flake8</code>

### [typing with annotations (type hints) and mypy](http://mypy-lang.org/) ###

Optional static type checking for better code quality.

### documentation ###

Pydoc style used in sourcecode. Currently there is no framework in use for generation the documentation.

### [testing with unittest](https://docs.python.org/3/library/unittest.html) ###

The package <code>unittest</code> is pythons builtin unit testing framework.

### [packaging & building](https://packaging.python.org/tutorials/packaging-projects/) ###

Packaging and building is done, using pythons default tools. Follow the header link for more.  

Python packages required for building the project:  
<code>pip install build</code>

Command to run the build:  
<code>python -m build</code>

### [package registry gitlab](https://docs.gitlab.com/ee/user/packages/pypi_repository/) ###

Python packages required for uploading pypi packages to gitlab:  
<code>pip install twine</code>  
<code>pip install wheel</code>  

For being able to upload packages to your custom pypi registry, add a <code>.pypirc</code> folder to your home directory and insert a custom config file:
```
[distutils]
index-servers =
    gitlab

[gitlab]
repository = http://gitlab.example.domain/api/v4/projects/<projectid:int>/packages/pypi
username = <userid>
password = <access-token>
```
Note: pip and twine use different configuration files, which is why the same url has to be provided in two separate configuration files.  
When running twine, you now may pass the file above as custom configuration file.  
<code>python -m twine upload --config-file $filename --repository gitlab dist/*</code>
