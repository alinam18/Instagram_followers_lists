import pandas
followersList = 'followers_list.txt'
followingList = 'following_list.txt'

def creatingDictionary(dictionary, filelist):
    dictionary = {}
    with open(filelist, 'r') as file:
        line_number = 1
        for line in file:
            stripped_line = line.strip()
            # print(stripped_line)
            dictionary[line_number] = stripped_line
            line_number += 1
    return dictionary


followers_dictionary = {}
followers_dictionary = creatingDictionary(followers_dictionary, followersList)
following_dictionary = {}
following_dictionary = creatingDictionary(following_dictionary, followingList)
# for line in line_dictionary:

followers = set(followers_dictionary.values())
following = set(following_dictionary.values())

# People you follow who don't follow you back
not_following_back = following - followers

# Display result
print("People who don't follow you back:")
count = 0
for user in sorted(not_following_back):
    count += 1
    print(user)
print('Total Count = %d', count)