users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab"]

sanju_followers=["sanju","rohit","kohli"]


mutual_friends=set(rahul_followers).intersection(set(sanju_followers))

# rahul_follow_suggestion=set(users).difference(set(rahul_followers))

print(mutual_friends)

