# pyMincHeader

pyMincHeader is a tool to fetch header information from MINC files in python.

## Requirements

* Python 3.5.0 or later

* MINC tools

For more information about the Minc toolkit, visit the [software website](http://www.bic.mni.mcgill.ca/ServicesSoftware/MINC)

## Installation

Download and unzip repository, or clone using the following command:

`git clone https://github.com/mathieuboudreau/pyMincHeader.git`

If you want to add this package to your PATH on a Mac, add this line to the 
~/.bash_profile file:

`export PYTHONPATH=$PYTHONPATH:/path/where/repo/was/cloned/pyMincHeader/pymincheader`

Substitute `/path/where/repo/was/clone` for the path where you unzipped or cloned the repository.

## Tests

To ensure the package is working as intended, in a terminal session go to `/path/where/repo/was/cloned/pyMincHeader/`
and execute the following command:

`python -m unittest`

All tests should be successful.

## Usage

* Import the class module:

`from pymincheader import PyMincHeader`

* Initiate an instance of the class:

`demoHeader = PyMincHeader('demo/demo.mnc')`

* Search for an attribute:

`searchResult = demoHeader.search('repetition')`

`searchResults` will be a dictionary with 3 keys: `'value'`, `'attribute'`, and `'line'`. For this example case, the result is:

* `searchResults[value]` = `2.3`
* `searchResults[attribute]` = `'acquisition:repetition_time'`
* `searchResults[line]` = `'acquisition:repetition_time = 2.3 ;'`

If the search does not find an entry, the values will all be set to `None`

## About me

**Mathieu Boudreau** is a PhD Candidate at McGill University in the Department of Biomedical Engineering.
He holds a BSc in Physics from the Universite de Moncton ('09), and a MSc in Physics from the University 
of Western Ontario ('11).