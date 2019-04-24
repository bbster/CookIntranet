#!/usr/bin/env bash

if [ -e client_build/ ]
then
    cd client_build/
    git pull origin master
    cd ..
else
    git clone https://github.com/k0603156/CookIntranetBuild.git client_build
fi
