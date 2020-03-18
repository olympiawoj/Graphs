import random 
from util import Stack, Queue  # These may come in handy

'''

'''

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    ##  IMPLEMENT THIS!!!
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        #1, 2, 3  - TAKE ALL possible user friendship combinatinos (1, 2) (1, 2) (2, 3) - all possible friendship combos. Not no (2, 1) (3, 1)(3, 2 ) bc user 1 being friends with user 2 is same as user 2 being friends with user 1
        #when we call create freindship, we're creating TWO friendships

        # Add users
        # Write a for loop that calls create user the right amount of times 
        for i in range(num_users):
            #creates 10 users - we have an empty adjacency list iwth 10 users in this
            #{1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set(), 10: set()}
            self.add_user(f"User {i +1}")

        # Create friendships
        # To create N random friendships
        # you could create a list with all possible friendship combos
        # shuffle the list, then grab the first N elements from the list
        #12, 13, 14, 15, 16, 1 10, 23, 24, 25, 26.., 2 10, 8 9, 8 10, 9 10,
        #let's go through each user and match them up w EVERY user id larger than their current id 
        possible_friendships = []
        for user_id in self.users: 
            for friend_id in range(user_id+1,self.last_id +1): #if user 4, only care abt 5 6 7
                possible_friendships.append((user_id, friend_id))
        # print(possible_friendships)
        # time complexity of this operation is --- On^2 - classic for in a for loop
        # [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 7), (6, 8), (6, 9), (6, 10), (7, 8), (7, 9), (7, 10), (8, 9), (8, 10), (9, 10)]
        # on average n * (n/2) at beginning all of them, at end less of them - 0.5 * n^2 nd always frop the coeffiicent 
        #how to optimize for 1b users? 10 users is ok.
        random.shuffle(possible_friendships)
        # print(possible_friendships)

        #slice off first 10 from list, creating N friendships where n=average_friendships * num_users // 2 --> how did we get this? we know that
        #average_friendships = total_friendships / num_users
        #to solve for total_friendships = average_friendships * num_users
        #divided by 2 bc every time we create a friendships we're actually creating 2 friendships so we need to divde by 2
        for i in range(num_users * avg_friendships // 2):
            #get an int
            friendship = possible_friendships[i]
            #create friendship
            self.add_friendship(friendship[0], friendship[1])

        #10 users, 20 total friendships, 10 users with friendships each w diff len of friends
        


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        #BFS so create an empty queue 
        q = Queue()
        #  Enqueue means to add an element to front, dequeue to remove an element from front
        # Queue is FIFO
        q.enqueue([user_id])
        # q.enqueue({'id': user_id, 'path': [user_id]})

        #while the queue is not empty...
        while q.size()>0:
            print('q', q)
            #dequeue first path form the queue
            path = q.dequeue()
            #get current node from the last el in the path
            v = path[-1]
            print(f'path: {path}, v: {v}')

            #check if v is in our visited dict, if not
            if v not in visited: 
                #mark as visited
                visited[v] = path
                # visited[user['id']] = user['path']
                
                #then iterate through all friendships in the dict
                for friendship in self.friendships[v]:
                    print(f'friendship: {friendship}')
                    #add to the path as a list, PLUS the friensdship to the queue
                    q.enqueue(list(path) + [friendship])
                    # q.enqueue({'id': friend, 'path': visited[friend]})
        print('all visited', visited)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('friendships', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('connections', connections)

# >>> sg = SocialGraph()
# >>> sg.populate_graph(10, 2)
# >>> print(sg.friendships)
# {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
# >>> connections = sg.get_all_social_paths(1)
# >>> print(connections)
# # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]} 
#1, 9, 2, 6, 8, 3, 6, 10, 4, 4 9  
#key --> every user in that user's extended network, [] array is the PATH between them 
#Takes a user's user_id as an argument
#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.