# CoPlay-Collector
A simple python script to scan a network for devices running CoPlay and log the data in a MySQL database

## Installation

`pip install -r requirements.txt`

## Configuration

Edit config.py with your preferred text editor

## Usage

`python3 collect.py`

## Querying latest recorded results

`python3 query.py`

Sample output:

```
Serial          Last updated         Last IP        Last Battery State    OS version              Installed apps count  App status
--------------  -------------------  -------------  --------------------  --------------------  ----------------------  ------------
1PASH9AQ4N9477  2021-07-01 11:33:35  192.168.20.26  99% and charging      user-1396940.13060.0                      44  OK
```