#!/bin/bash

# rm packages.zip

# ROOT="$(pwd)"
# PACKAGES="$(pwd)/.venv/lib64/python3.11/site-packages"

# cd "$PACKAGES"

# zip -r "$ROOT/packages.zip" .

# cd $ROOT

# zip packages.zip lambda_function.py

rm packages.zip

dir_name=package/

mkdir -p $dir_name

pip install --target $dir_name -r requirements.txt

cp lambda_function.py $dir_name

cd $dir_name

zip -r ../packages.zip .

cd ../

rm -rf $dir_name
