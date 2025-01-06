followerstemp = []
with open("followers.txt", "r") as followersfile:
    for line in followersfile:
        a = line.strip()
        followerstemp.append(a)
followerslist = [i for i in followerstemp if i != '·' and i[-15:] != 'profile picture']
# both username and name
followingtemp = []
with open("following.txt", "r") as followingfile:
    for line in followingfile:
        a = line.strip()
        followingtemp.append(a)
followinglist = [i for i in followingtemp if i != '·' and i[-15:] != 'profile picture']
print(followinglist)

for i in followinglist:
    if i not in followerslist:
        print(i)