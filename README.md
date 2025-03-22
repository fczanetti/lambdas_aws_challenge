# AWS Challenge [WIP]

These are the Lambdas required to complete the AWS Challenge [proposed here](https://github.com/fczanetti/aws_challenge).

The environment variables can be set in AWS Lambda Console. This may not be the safest approach (there is AWS Secrets Manager, but with a cost), but for learning purposes is OK.

The deploy is still manual, but simple. We just have to go into the directory of the lambda that we want to deploy, run the command `./create_package.sh` and wait for the .zip package to be created. After creating, just upload it through the AWS Lambda Console (Upload from .zip file).

## Configurations / permissions
...