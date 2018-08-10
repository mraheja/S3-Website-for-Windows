@echo off

aws s3api create-bucket --bucket <ENTER NAME>
aws s3api put-bucket-policy --bucket <ENTER NAME> --policy file://bucket.json
del init.bat

pause
