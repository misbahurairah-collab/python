c = int(input())
f = int(input())
r = int(input()) 

distributed_candies = (c-r)
no_of_candies_each_friend_recieve = distributed_candies//f
no_of_candies_left = distributed_candies%f
print(no_of_candies_each_friend_recieve)
print(no_of_candies_left)