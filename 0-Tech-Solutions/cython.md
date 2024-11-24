## Code 
D:\github\2-Experiments\cython

## python program runs slower than program written in c. Is it true?

In general, programs written in C tend to run faster than programs written in Python. This is because C is a compiled language, which means that the code is translated into machine-readable instructions before it is executed. Python, on the other hand, is an interpreted language, which

## Can't we compile python program in advance?

Yes, it is possible to compile Python code in advance using tools such as Cython or Numba. These tools allow you to write Python code that can be compiled down to machine code for improved performance. However, even with these tools, the performance of a compiled Python program is still generally not as fast as a program written in C, because Python has certain limitations that make it inherently slower than languages like C.

One reason for this is that Python is a dynamically typed language, which means that variable types are determined at runtime. This introduces overhead compared to statically typed languages like C, where variable types are known at compile-time.

Additionally, Python has a garbage collector that automatically manages memory allocation and deallocation, which can also introduce overhead. In contrast, C requires the programmer to manually manage memory, which can be more efficient in certain cases.

Overall, while it is possible to compile Python code in advance for improved performance, it is still unlikely to be as fast as C in most cases due to the inherent limitations of the Python language.


Hari Thapliyaal
can you give me example code to complie python code using cython?
Sure! Here's an example of how to use Cython to compile a Python function to C:

Let's say you have the following Python function that calculates the sum of two numbers:

## python:Copy code

def add_numbers(a, b):
    return a + b
You can use Cython to compile this function to C by creating a separate .pyx file with the Cython code. Here's what the add_numbers.pyx file might look like:

## cython:Copy code

def add_numbers_cython(int a, int b):
    return a + b
Note that we've changed the function name to add_numbers_cython, and we've also explicitly specified that the input parameters a and b are of type int.

To compile this Cython code to a C extension module, you'll need to create a setup.py file that tells Cython how to build the module. Here's an example setup.py file:

## python:Copy code

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("add_numbers.pyx")
)
This setup.py file tells Cython to build a C extension module from the add_numbers.pyx file.

To build the C extension module, you can run the following command in the terminal:

## css: Copy code
python setup.py build_ext --inplace
This will create a .so file (or a .pyd file on Windows) that contains the compiled C code. You can then import this module in your Python code like so:

## python: Copy code (add_number_1.py)
from add_numbers import add_numbers_cython

result = add_numbers_cython(2, 3)
print(result)  # Output: 5

This will call the add_numbers_cython function from the compiled C extension module, which should be faster than the original Python implementation.
## Execute code 
python add_number_1.py


## How to install Microsoft Visual C++ 14.0
Microsoft Visual C++ 14.0 is a compiler toolset required by some Python packages, such as NumPy, to build their extensions. Here's how you can install it:

Download and install Microsoft Visual C++ Build Tools: Go to the Microsoft Visual C++ Build Tools download page (https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019), and click on the "Download" button for the version of Build Tools that matches your version of Visual Studio or Visual Studio Community.

Install the Build Tools: Run the downloaded executable file, and select the "C++ build tools" option in the installer. Follow the prompts to complete the installation.

Verify the installation: Open the Command Prompt or PowerShell and run the following command to verify that the Build Tools were installed correctly:

Copy code
cl.exe
This should print information about the version of the C++ compiler that was installed. If you get an error message saying that "cl.exe" is not recognized as an internal or external command, then the Build Tools were not installed correctly.

That's it! Once you have installed Microsoft Visual C++ Build Tools, you should be able to install Python packages that require Microsoft Visual C++ 14.0 to build their extensions.


## Microsoft Visual C++ 14.0 or greater is required. 

Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

This error message typically appears when you're trying to install a Python package that requires compilation of native code, such as NumPy or SciPy, and you don't have the required version of Microsoft Visual C++ installed on your system.

To resolve this issue, you'll need to install Microsoft Visual C++ 14.0 or a later version. Here's how to do it:

Go to the Microsoft Visual C++ Build Tools download page: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Scroll down to the "Tools for Visual Studio" section and click on the "Download" button for the version of Build Tools that matches your version of Visual Studio or Visual Studio Community.

Run the downloaded installer and select the "C++ build tools" option. Make sure to select the "Windows 10 SDK" option as well, as this is also required for building some Python packages.

Complete the installation process and restart your computer if necessary.

After installing Microsoft Visual C++ Build Tools, you should be able to install the Python package that was previously giving you the error message.


## There are many versions of build tools. I have windows 2010 Pro edition on my machine. Which version I should select?

If you have Windows 10 installed on your machine, you should be able to use the latest version of Microsoft Visual C++ Build Tools. As of March 2023, the latest version is "Microsoft Visual Studio 2022 Build Tools". You can download it from the following link:

https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022

Note that the Build Tools require a lot of disk space, so make sure you have enough free space on your hard drive before installing it. Also, the installation process may take some time, depending on your internet connection speed and hardware specs.


## pyconfig.h(59): fatal error C1083: Cannot open include file: 'io.h': No such file or directory

The error message you're seeing indicates that the C compiler cannot find the "io.h" header file, which is required for building some Python modules that rely on low-level I/O operations.

To fix this issue, you can try one or more of the following solutions:

Install Microsoft Visual C++ Build Tools: As mentioned earlier, some Python packages require Microsoft Visual C++ Build Tools to be installed in order to build their extensions. Make sure that you have installed the latest version of Build Tools on your system, and that you have selected the "C++ build tools" and "Windows 10 SDK" options during the installation.

Install Windows SDK: The "io.h" header file is part of the Windows SDK, which is a collection of tools and libraries that developers use to build Windows applications. You can download and install the latest version of Windows SDK from the following link:

https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/

During the installation, make sure to select the "Windows SDK for desktop C++ x86 and x64" option.

Specify the include path: If you have already installed Microsoft Visual C++ Build Tools or Windows SDK, you can try specifying the include path to the "io.h" header file using the C compiler's command-line options. For example, you can try adding the following option to your build command:

python: Copy code
-I"C:\Program Files (x86)\Windows Kits\10\Include\10.0.xxxxx.x\ucrt"
Replace "10.0.xxxxx.x" with the version number of the Windows SDK that you have installed.

Check your environment variables: Make sure that your environment variables are set up correctly. Specifically, check that the "INCLUDE" environment variable includes the path to the directory that contains the "io.h" header file. You can check this by running the following command in the Command Prompt or PowerShell:

## bash: Copy code

echo %INCLUDE%
This should print a list of directories separated by semicolons. Make sure that one of the directories contains the "io.h" header file.

I hope one of these solutions helps you fix the "io.h" header file not found error.