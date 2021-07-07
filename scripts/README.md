## Set up

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## create_iam_users.py
This script creates a IAM users under a root AWS account.
The group name to which the usres will be added needs to be specified.

Usage:

```bash
# Assuming that the AWS credential is properly set
# Assuming that the IAM group named "students" is already created
python3 create_iam_users.py -g students -n 2 -r 0123456
```

## delete_iam_usres.py
This script deletes all IAM users whose name starts with `prefix` parameter (default = student).

```bash
# Assuming that the AWS credential is properly set
# Assuming that the IAM group named "students" is already created
python3 delete_iam_usres.py -g students
```
