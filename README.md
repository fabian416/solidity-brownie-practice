# SimpleStorage Project

This is a simple Ethereum blockchain project that demonstrates basic smart contract interactions with the Ethereum blockchain, using the Brownie Python framework. 

## Project Overview

The project consists of a single smart contract (`SimpleStorage.sol`) that stores a number on the blockchain. The contract has two main functions - one for storing a number and one for retrieving 
the stored number. 

Development practice in Solidity and deployment of smart contracts in Sepolia using Brownie. The 'SimpleStorage' contract enables basic interactions with the Ethereum blockchain. The project 
includes a Python virtual environment and a requirements file.txt to facilitate the installation of dependencies.

## Getting Started

1. Clone this repository.
2. Create a Python virtual environment (Optional, but recommended). The project has been tested with Python 3.9.6. Newer versions may cause issues with Brownie installation 
due to the `cytoolz` dependency.
3. Run 'pip install -r requirements.txt' to install the project dependencies.

## Deployment

This project has been set up to be easily deployed on the Sepolia test network. You will need an Infura account and set the project ID and private key in the `.env` file.

To deploy, simply run the following command:brownie run scripts/deploy.py --network sepolia






