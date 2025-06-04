# PythonRefProp

Functions / Packages to connect Python and RefProp

## Refpropwrapper

Contains function / wrapper to connect Python 3.6 / 3.7 to RefProp 10.
In case functions do not work properly with your RefProp Version, try dll in
folder.

### Installation 

In order to use this package, you can either install it via pip install (see
below) or simply download the python files and use them in your own script. I 
suggest installation.
Installation steps are:
1.  Download repository via git: 
`git clone https://git.rwth-aachen.de/EBC/Team_BES/connectors/pythonrefprop.git`
2. Install package via pip. Use python prompt console:
`pip install <local path to git repo>\pythonrefprop`

When installation is finished, you can use the package in python via 
`import rp_wrapper` 

### Developing the package

In case you are developing the package, change the pip install command to

`pip install -e <local path to git repo>\pythonrefprop`

to go into development mode in Python so changes will be adapted directly and 
no further install command is needed.


## Functionality

- Note: REFPROP needs to be installed at your computer. In case it's missing, you could link to the files of REFPROP at your computer by using the command in python:
`os.environ["RPPREFIX"] = <path to REFPROP folder>`
- Connection to REFPROP database to calculate fluid properties. The wrapper is able to calculate transport properties as well as state properties in dependency of two state variables.
- Script / GUI to generate data for a T-h, log(p)-h or T-s diagram is included as well.


