
'''Neo has a bag of candies and wants to share them with his friends.He has 'c' candies in total.
He intends to distribute them equally among his 'f' friends, but he also wants to keep 'r' candies for himself.
Write a program to calculate how many candies each friend will get and the number of candies Neo will keep for himself.'''


c = int(input())
f = int(input())
r = int(input()) 
distributed_candies = (c-r)
no_of_candies_each_friend_recieve = distributed_candies//f
no_of_candies_left = distributed_candies%f
print(no_of_candies_each_friend_recieve)
print(no_of_candies_left)
