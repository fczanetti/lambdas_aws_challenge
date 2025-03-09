#!/bin/bash

rm process_image_from_s3_package.zip

dir_name=package/

mkdir -p $dir_name

pip install --target $dir_name -r requirements.txt

cp lambda_function.py $dir_name

cd $dir_name

zip -r ../process_image_from_s3_package.zip .

cd ../

rm -rf $dir_name