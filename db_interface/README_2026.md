# User Interface for the Wave Energy Converter Catalogue
# Archived documentation: This file is preserved for historical reference. Installation instructions and licensing statements may be outdated. See the main project README for the current version.

The main interface is built in Dash.


## Getting Started
### Using the demo

The first step is to create and activate an environment for the application to run.
Within the environment we will install python v3.6 and pip

```
// Initially:
>> conda create -n wec_db_interface python=3.6 pip
>> conda activate wec_db_interface

// For the new version of the 17/10/2026
>> py -0p
>> python --version
>> python3 -m pip --version
>> pip --version
>> conda --version
>> conda create -n wec2019 python=3.7 pip -y
>> conda activate wec2019
>> python --version
>> conda run -n wec2019 python --version
>> conda env list
>> Get-Command conda
>> Get-Command python
>> $env:CONDA_PREFIX
>> conda run -n wec2019 python -m pip --version

// An alternative option, just by curiosity
// This creates a Python 3.8 environment without changing the main Python installation
>> New-Item -ItemType Directory -Force "$env:USERPROFILE\venvs" | Out-Null
>> py -3.8 -m venv "$env:USERPROFILE\venvs\wec-py38"
>> & "$env:USERPROFILE\venvs\wec-py38\Scripts\python.exe" --version7
>> $py38 = "$env:USERPROFILE\venvs\wec-py38\Scripts\python.exe"

```

After updating pip to the latest version, install the application requirements specified in 
the requirements.txt.
WARNING: Numpy has to be listed first in the requirements.txt file, because other packages
depend on it to build.


```
// Previous version
(wec_db_interface)>> pip install --upgrade pip
(wec_db_interface)>> pip install -r requirements.txt

// New verison using the conda (not fully activate, yet present, environment)
>> conda run -n wec2019 pip install --upgrade pip
>> conda run -n wec2019 pip install -r requirements.txt

// If you want to try without the conda environment you can atempt but python is above 3.7
>> pip install --upgrade pip
>> pip install -r requirements-py38-experiment.txt

// The final curiosity approach is 
>> & $py38 -m pip install --only-binary=numpy,pandas,scipy,scikit-learn,h5py,pyrsistent -r .\requirements-py38-experiment.txt
>> & $py38 -m pip check
>> & $py38 -c "import numpy, pandas, scipy, sklearn, h5py, flask, dash; print('Imports OK')"

```  


### Running the app locally

After the requirements are installed run the application on a local server by typing:  

```
// Previous version
python3 run.py

// New version
conda run -n wec2019 python run.py

// Curiosity version
>> & $py38 run.py

```

## About the app
### How does it work?


## Built With
* [Dash](https://dash.plot.ly/) - Main server and interactive components
* [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on the code development,
and the process for submitting pull requests.

## Authors

* **Francesco Ferri** - *Initial Work on the db_interface* - [@fferri](https://github.com/fferri)
* **Ophélie Choupin** - *CoreFunctions and the entire model and database design* - [@Kophlorie](https://github.com/Kophlorie)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

## Screenshots
