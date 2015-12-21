#!/bin/bash

# report if pip not installed
if hash pip 2>/dev/null; then
        printf "pip already installed...\n"
else
        printf "they dont want us to use python. install python and pip before proceeding...\n"
        exit 1
fi

# install virtualenv if not installed
if hash virtualenv 2>/dev/null; then
        printf "virtualenv already installed...\n"
else
        printf "they dont want us to use virtualenv. installing...\n"
        pip install virtualenv
fi

# create flask
if [ ! -d "flask" ]; then
        printf "creating flask...\n"
        virtualenv flask
        flask/bin/pip install flask
fi

chmod +x run.sh
chmod +x test.sh

printf "ready to run...\n"
