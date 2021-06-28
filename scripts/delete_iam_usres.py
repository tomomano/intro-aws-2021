import boto3
import argparse, string, random, json

def main(groupname, prefix):

    client = boto3.client('iam')

    # get a list of users
    resp = client.list_users(
        MaxItems=300
    )
    users = resp.get("Users")

    for user in users:
        name = user["UserName"]
        if name.startswith(prefix):
            client.remove_user_from_group(
                GroupName=groupname,
                UserName=name
            )
            client.delete_login_profile(
                UserName=name
            )
            # delete access keys
            keys = client.list_access_keys(
                UserName=name,
            ).get("AccessKeyMetadata")
            for key in keys:
                client.delete_access_key(
                    UserName=name,
                    AccessKeyId=key["AccessKeyId"]
                )
            # delete user!
            client.delete_user(
                UserName=name
            )
            print("Deleted user", name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--groupname", type=str, help="Group name to which the users will be added")
    parser.add_argument("-p", "--prefix", type=str, default="student", help="Prefix of the user name")
    args = parser.parse_args()

    main(args.groupname, args.prefix)
