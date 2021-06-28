import boto3
import os, argparse, string, random, json

def main(groupname, num_users, root_id):

    client = boto3.client('iam')
    if not os.path.exists("users"):
        os.makedirs("users")

    for i in range(num_users):
        user_data = {}
        # generate random user name and password
        username = "student-" + ''.join(random.choice(string.ascii_lowercase) for _ in range(6))

        pw = random.choice(string.ascii_lowercase)
        pw += random.choice(string.ascii_uppercase)
        pw += random.choice(string.digits)
        pw += random.choice(["@", "#", "!", "$"])
        pw += ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
        pw = ''.join(random.sample(pw, len(pw)))

        resp = client.create_user(
            UserName=username,
        )
        resp = client.add_user_to_group(
            GroupName=groupname,
            UserName=username
        )
        # set random password
        resp = client.create_login_profile(
            UserName=username,
            Password=pw,
            PasswordResetRequired=False
        )
        # create access key
        resp = client.create_access_key(
            UserName=username
        )
        
        # return user data
        user_data["UserName"] = username
        user_data["Password"] = pw
        user_data["AccessKeyId"] = resp["AccessKey"]["AccessKeyId"]
        user_data["SecretAccessKey"] = resp["AccessKey"]["SecretAccessKey"]
        user_data["Sign in link"] = f"https://{root_id}.signin.aws.amazon.com/console"

        # save user data
        with open(os.path.join("users", username + ".json"), "w") as f:
            json.dump(user_data, f, indent=3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_users", type=int, help="Number of users to create")
    parser.add_argument("-g", "--groupname", type=str, help="Group name to which the users will be added")
    parser.add_argument("-r", "--rootid", type=str, help="Root account id")
    args = parser.parse_args()

    main(args.groupname, args.num_users, args.rootid)
