# S3-Website-for-Windows
An easy way to publish your website to s3 to share with others

# Dependancies

1. AWS CLI (set this up with your account)
  ```
  pip install awscli
  ```
2. Python 3.6


# Usage
## Setup
To setup your website, first run setup.py which will ask you for the name of your website/s3 bucket. Make sure to not include capital or special characters and make this unique because it's shared between all users of AWS.

Once you have completed this, run

```
init
```

from the command line. This will setup the bucket then delete the init file.

## Updating your website
Everytime you want to sync your website with whatever is in the "Website" folder, run:

```
sync
```

To open the website in Chrome run:

```
open
```
