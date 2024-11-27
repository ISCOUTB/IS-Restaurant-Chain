# IS-Restaurant-Chain

## Deploy Web app

https://restaurant-chain-9nr7.onrender.com


## Developer team

- [Luis Daniel Arias Marrugo](https://github.com/luisariass)
- [Brandold Vega Pérez](https://github.com/BRNDLD)
- [Michel Augusto Castellano Severiche](https://github.com/Michse017)
- [Andrés Felipe García Sosa](https://github.com/Rex10202)


## Overview

A restaurant chain operates on legacy POS systems, separate loyalty programs, and mobile apps, leading to overhead inefficiencies. Data is isolated across systems, limiting customer insights. Scaling requires replicating changes across systems, and adding new data/features requires complex coordination.

The fragmented systems limit the restaurant chain's ability to deliver seamless omnichannel experiences. For example, promotions and ordering are not integrated across POS, mobile apps, and loyalty programs, resulting in inconsistent messaging and experiences.

## Solution

The company needs cross-channel data sharing to enable personalized engagements, inventory coordination, and process optimization. The solution involves building microservices oriented around restaurant capabilities like ordering and loyalty programs. These would expose customer, sales, and menu data APIs managed by a gateway. This data is streamed to a cloud analytics platform for ML optimization. This approach incrementally decomposes monoliths over time into focused, decoupled services that deliver unified data access through standardized APIs.

### Specifications

- Develop microservices for ordering, loyalty, pricing, and promotions.
- Expose customer, menu, and sales data via APIs controlled by a gateway.
- Stream API data into a cloud analytics platform.
- Apply analytics and ML to optimize pricing and promotions.

## Project Structure

```plaintext
IS-Restaurant-Chain/
├── .github/
│   └── workflows/
├── .vscode/
├── domain/
│   ├── entities/
│   └── use_cases/
├── infrastructure/
│   ├── api/
│   └── repositories/
├── interfaces/
├── styles/
├── templates/
├── test/
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── sonar-project.properties
```

## Prerequisites

- Python 3.9 or higher
- Docker (optional, if you want to run the application in a container)

## Installation

### Clone the repository


```sh
git clone https://github.com/tu-usuario/IS-Restaurant-Chain.git
cd IS-Restaurant-Chain
```

### Create and activate a virtual environment

```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
### Install dependencies

```console
pip install -r [requirements.txt](http://_vscodecontentref_/5)
```
### Configure environment variables
Make sure to configure the necessary environment variables, such as the database connection string.

### Run the application
```console
uvicorn main:app --reload
 ```

 The application will be available at http://127.0.0.1:8000.


## Using Docker
### Build the Docker image

```console
docker build -t is-restaurant-chain .
```
### Run the container
```console
docker run -p 8000:8000 is-restaurant-chain
```
The application will be available at http://127.0.0.1:8000.

## Running Tests
To run the tests, use the following command:
```console
pytest
```
## Contributing 
If you want to contribute to this project, please follow these guidelines:

    1. Fork the repository.
    2. Create a new branch (git checkout -b feature/new-feature).
    3. Make your changes and commit them (git commit -am 'Add new feature').
    4. Push to the branch (git push origin feature/new-feature).
    5. Open a Pull Request.

## LICENSE
    This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.