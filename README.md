<h1 align="center">GeoSMS2 Backend</h1>

<p align="center">
  <img alt="badge-lastcommit" src="https://img.shields.io/github/last-commit/GaryHilares/GeoSMS2_Backend?style=for-the-badge">
  <img alt="badge-openissues" src="https://img.shields.io/github/issues-raw/GaryHilares/GeoSMS2_Backend?style=for-the-badge">
  <img alt="badge-license" src="https://img.shields.io/github/license/GaryHilares/GeoSMS2_Backend?style=for-the-badge">
  <img alt="badge-contributors" src="https://img.shields.io/github/contributors/GaryHilares/GeoSMS2_Backend?style=for-the-badge">
  <img alt="badge-codesize" src="https://img.shields.io/github/languages/code-size/GaryHilares/GeoSMS2_Backend?style=for-the-badge">
</p>

## What is GeoSMS2 Backend?
GeoSMS2 Backend is a backend API created for the GeoSMS2 project. It provides functionality to carry out many actions, such as translating text, getting the latest news, telling jokes, searching in Google, and solving mathematical expressions.

Currently the API replies to any queries in Spanish. English support may or may not be added.

### Platforms
- Cross-platform

### Dependencies
#### Development
- Python 3
- PIP

## Motivation

## Installation and usage
To build and run the server, you can follow the next steps:
1. Install the dependencies:
    1. Download and install Python 3 and PIP from [Python's website](https://www.python.org/downloads/) or by using the package manager of your choice.
    2. Go to the root directory of the project and run `pip install -r requirements.txt` (or the equivalent command for your toolchain).
2. Run GeoSMS2 Backend:
    - If you're in a development environment, you can just run `index.py` and it will start Flask's development server for you.
    - For a production deployment, disable the `debug` option from `index.py` and set up a WSGI server to run Flask from.

Once you do this, you should be able to connect to `https://localhost/` and use the form there to execute commands to the main API, which listens to `https://localhost/command` for requests.

## Contributors
Thanks to these wonderful people for making GeoSMS2 Backend possible!

<p align="center"><a href="https://github.com/GaryHilares/GeoSMS2_Backend/graphs/contributors"><img src="https://contrib.rocks/image?repo=GaryHilares/GeoSMS2_Backend" /></a></p>

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://github.com/GaryHilares/GeoSMS2_Backend/blob/main/LICENSE).