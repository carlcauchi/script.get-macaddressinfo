# script.get-macaddressinfo
Script to get the manufacturer company name from a provided mac address

# Git Clone the repository

`git clone https://github.com/carlcauchi/script.get-macaddressinfo.git`

# Configure the API Key

Modify the config file under `'config/app.config'` with your registered macaddress.io API Key
Visit https://macaddress.io/api to create a free account and generate an API Key. 

# Build Docker Image

To build the image, run Docker build from command line that is in the root directory of the application.

`docker build --tag get-macaddressinfo .`

This will 'tag' the image get-macaddressinfo and build it.
After it is built, you can run the image as a container.

# Run Docker Image

To run the Container, run the following command and replace the `--mac AA-BB-CC-DD-EE-FF` with
the MAC address that you would like to search.

`docker run --rm -it --name get-macaddressinfo-container get-macaddressinfo --mac AA-BB-CC-DD-EE-FF`
