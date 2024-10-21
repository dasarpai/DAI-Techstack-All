Readme by Hari Thapliyal 

## Python Package vs Python Module 

### Package 
Let's assume we want to create a calc package. It should have following folder structure.  
calc/
├── `__init__.py`  
├── `__main__.py`  
└── other_module.py  

what should be inside `__init__.py` file?   
you can keep it empty. It serves following purpose.

If you do not have any code inside this `__init__.py` file:
1. It automatically import any modules or functions.
2. User will have the convenience of importing directly from the package.
3. User need not to import specific modules or functions explicitly.
4. The package will have any immediately accessible attributes or submodules.

If you want to have above convinience then you can have following code in this file.   
from .other_module import add_func, mult_func

What is inside `__main__.py`?   
You must have following minimum code inside this file.  

```
# calc/`__main__`.py
def main():
    print("Running calc as a module!")

if `__name__` == "`__main__`":
    main()

```
	
How to call package?  
python -m calc (from one level above the folder)

How to import package within some program?  
import calc

How to call some functions from package?  
If other_module module of the calc package has a function "multiply", then it can be called like this.  
calc.other_module.multiply(10, 20)

### Python Module 
It will be a single file. It contains all the functions or classes.

How to call module?  
python module_name.py 

## Important Commands with Python at command prompt
### 1. **Running a Python Script**
```bash
python script.py
```
This command runs a Python script named `script.py`. Make sure you are in the directory where the script is located or provide the full path.

### 2. **Interactive Python Shell**
```bash
python
```
This command starts an interactive Python shell where you can execute Python commands one at a time.

### 3. **Checking Python Version**
```bash
python --version
```
This command displays the version of Python installed on your system.

### 4. **Installing Packages with pip**
```bash
pip install package_name
```
Use this command to install a package from the Python Package Index (PyPI). Replace `package_name` with the name of the package you want to install.

### 5. **Listing Installed Packages**
```bash
pip list
```
This command lists all the packages installed in your Python environment along with their versions.

### 6. **Upgrading a Package**
```bash
pip install --upgrade package_name
```
This command upgrades an installed package to the latest version.

### 7. **Starting a Simple HTTP Server**
```bash
python -m http.server 8000
```
Starts a simple HTTP server serving files from the current directory on port 8000.

### 8. **Running a Module as a Script**
```bash
python -m module_name
```
This command runs a module as a script. For example, you can use it to run the `http.server` module or any other module that has a `__main__.py` file.

### 9. **Creating a Virtual Environment**
```bash
python -m venv env_name
```
This command creates a new virtual environment named `env_name`. Virtual environments are useful for managing dependencies for different projects.

### 10. **Activating a Virtual Environment**
- **Windows**:
  ```bash
  env_name\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source env_name/bin/activate
  ```

### 11. **Deactivating a Virtual Environment**
```bash
deactivate
```
This command deactivates the current virtual environment, returning you to the system's default Python environment.

### 12. **Checking Installed Python Modules**
```bash
pip show package_name
```
Displays detailed information about the specified installed package, including version, location, and dependencies.

### 13. **Running a Python Script in the Background (Linux)**
```bash
nohup python script.py &
```
This command runs a Python script in the background, allowing it to continue running after you log out.

### 14. **Checking Syntax Errors**
```bash
python -m py_compile script.py
```
This command checks a Python script for syntax errors and compiles it to bytecode without running it.

### 15. **Executing a One-liner**
```bash
python -c "print('Hello, World!')"
```
This command allows you to run a single line of Python code from the command line.

These commands can greatly enhance your efficiency while working with Python and help you manage projects effectively!
