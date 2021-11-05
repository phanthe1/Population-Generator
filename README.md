# Population-Generator
The Population Generator is a software that will generate a population size number given the
input of the state and year. In addition, the application will also receive a CSV input (input.csv)
when it starts and create an output.csv that contains the year, state, and population size. The data
generated is specific to the user’s query. The software is created using the microservice architectural style and
is written in Python.

The Population Generator integrates with the Person Generator microservice. The Person
Generator was created by another developer. The application takes in the year and state. Then,
the application outputs the population size with the list of addresses  to the console.

RPyC exposes the Population Generator application to a port (port 18801) on a machine, in
which other applications can make requests to that exposed port and use its functionality and
vice versa.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
To run the GUI, run the following command
```
python population-generator.py
```

If there is an input CSV file, please make sure you have the following:
1. Ensure that the input.csv file is located within the same directory as the python files.
2. The required format for ```input.csv``` (with header): ```input_year, input_state```

Then, run the following command 
```
python population-generator.py input.csv
```
Check output file ```output.csv``` for results

## Built With
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The framework library used
* [RPyC](https://rpyc.readthedocs.io/en/latest/install.html)- Python library for remote procedure calls
