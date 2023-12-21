## Team Project - G7



# How to use app
## For Users

1. Open folder `/app`
2. Run file `g7cli.exe`
```shell
   app/g7cli.exe
```
> You can add app to **PATH** and use it from the console anywhere


## For Developers

### How to create new build
1. [Download](https://www.python.org/downloads/) and install Python 3+
2. Create virtual environment python
```shell
python -m venv /path/to/new/virtual/environment
```
3. Run virtual env 

In **cmd.exe** run command:
```commandline
venv\Scripts\activate.bat
```

In **PowerShell** run command:
```shell
venv\Scripts\Activate.ps1
```

4. Install requirements packages
```shell
pip install -r requirements.txt
```

5. Run this command in the project root directory and the build will be rebuilt.
```shell
python setup.py build   
``` 
6. Open folder `/app`
7. Run file `g7cli.exe`
```shell
   app/g7cli.exe
```