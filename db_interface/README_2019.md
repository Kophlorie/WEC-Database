# User Interface for the Wave Energy Converter Catalogue
# Archived documentation: This file is preserved for historical reference. Installation instructions and licensing statements may be outdated. See the main project README for the current version.

The main interface is built in Dash.


## Getting Started
### Using the demo

The first step is to create and activate an environment for the application to run.
Within the environment we will install python v3.6 and pip

```

>> conda create -n wec_db_interface python=3.6 pip

>> conda activate wec_db_interface

```

After updating pip to the latest version, install the application requirements specified in 
the requirements.txt.
WARNING: Numpy has to be listed first in the requirements.txt file, because other packages
depend on it to build.


```

(wec_db_interface)>> pip install --upgrade pip
(wec_db_interface)>> pip install -r requirements.txt

```  


### Running the app locally

After the requirements are installed run the application on a local server by typing:  

```
python3 run.py

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
