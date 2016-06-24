global UserSet
global FriendSet
global TweetSet
global SelectedUser
UserSet = []
FriendSet = []
TweetSet = []


"""---------------------heap sort Start------------------------"""

def heapify(A,i,heapsize,t):
    l = left(i)
    r = right(i)
    if l < heapsize and A[l][t] > A[i][t]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r][t] > A[largest][t]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A,largest,heapsize,t)

def buildheap(A,t):
    for i in range(len(A)//2 + 1,0,-1):
        heapify(A,i-1,len(A),t)

def heapsort(A,t):
    buildheap(A,t)
    for i in range(len(A),1,-1):
        A[i-1],A[0] = A[0],A[i-1]
        heapify(A,0,i - 1,t)

def parent(n):
    return (n-1)//2

def left(n):
    return 2*n+1

def right(n):
    return 2*n+2

'''binary search'''

def binary_search(a, x, l):
      hi = len(a)
      lo = 0
      while lo < hi:
            mid = (lo+hi)//2
            midval = a[mid][l]
            if midval < x:
                  lo = mid+1
            elif midval > x:
                  hi = mid
            else:
                  return mid
      return None


import copy

WHITE = 0
GRAY = 1
BLACK = 2

class Adj:
    def __init__(self):
        self.n = 0
        self.next = None

class Vertex:
    def __init__(self):
        self.color = WHITE
        self.parent = -1
        self.name = '(none)'
        self.n = 0
        self.first = None
    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

class BFSVertex(Vertex):
    def __init__(self):
        super().__init__()
        self.d = 1E10

class DFSVertex(Vertex):
    def __init__(self):
        super().__init__()
        self.d = 0
        self.f = 0

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []
    def create_queue(self,sz):
        self.sz = sz
        self.buf = list(range(sz)) 
    def enqueue(self,val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz
    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res
    def is_empty(self):
        return self.front == self.rear

def print_vertex(vertices,n):
    print (vertices[n].name, end=' ')
    print (vertices[n].color, end=' ')
    print (vertices[n].parent, end=' ')
    print (vertices[n].d, end=':')
    p = vertices[n].first
    while p:
        print (vertices[p.n].name, end = ' ')
        p = p.next
    print('')

class DepthFirstSearch:
    def __init__(self):
        self.time = 0;
        self.vertices = None
    def set_vertices(self,vertices):
        self.vertices = vertices
    def dfs(self):
        for u in self.vertices:
            u.color = WHITE
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == WHITE:
                self.dfs_visit(u)
    def dfs_visit(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = GRAY
        v = u.first
        while v:
            if self.vertices[v.n].color == WHITE:
                self.vertices[v.n].parent = u.n
                self.dfs_visit(self.vertices[v.n])
            v = v.next;
        u.color = BLACK
        self.time = self.time + 1
        u.f = self.time
    def print_vertex(self,n):
        print (self.vertices[n].name, end=' ')
        print (self.vertices[n].color, end=' ')
        print (self.vertices[n].parent, end=' ')
        print (self.vertices[n].d, end=' ')
        print (self.vertices[n].f, end=':')
        p = self.vertices[n].first
        while p:
            print (self.vertices[p.n].name, end = ' ')
            p = p.next
        print('')

    def transpose(self):
        new_vertices = copy.deepcopy(self.vertices)
        for m in range(0,len(new_vertices)):
            new_vertices[m].first = None
        for i in range(0,len(new_vertices)):
            k = self.vertices[i].first
            while k:
                new_vertices[k.n].add(new_vertices[i])
                k = k.next
        self.vertices = new_vertices

def bfs(vertices, s):
    for u in vertices:
        if u.n != s.n:
            u.color = WHITE
            u.d = 1E10
            u.parent = -1
    s.color = GRAY
    s.d = 0
    s.parent = -1
    q = Queue()
    q.create_queue(len(vertices))
    q.enqueue(s.n)
    while not q.is_empty():
        u = q.dequeue()
        adj_v = vertices[u].first
        while adj_v:
            if vertices[adj_v.n].color == WHITE:
                vertices[adj_v.n].color = GRAY
                vertices[adj_v.n].d = vertices[u].d + 1
                vertices[adj_v.n].parent = u
                q.enqueue(adj_v.n)
            adj_v = adj_v.next
        vertices[u].color = BLACK

def getFriend(user):
    friend = []
    for i in range(len(FriendSet)):
        if(user == FriendSet[i][0]):
            friend.append(FriendSet[i][0])
    return friend

def BFS_main():
    global UserSet
    global FriendSet
    vertices = []
    for i in range(len(UserSet)):
        vertices.append(BFSVertex())
        vertices[i].name = UserSet[i][1]
        vertices[i].n = UserSet[i][0]

    for i in range(len(vertices)):
        friendList = getFriend(vertices[i].n)
        for t in range(len(friendList)):
            f = binary_search(UserSet,friendList[t],0)
            if (f != None):
                vertices[i].add(vertices[f])

    DFS = DepthFirstSearch()
    DFS.set_vertices(vertices)    
    DFS.transpose()
    DFS.dfs()
    for i in range(0,len(vertices)):
        DFS.print_vertex(i)

"""------------------read data------------------"""
def readUserProfile():
      UserProfile = open('user.txt')
      return UserProfile
      
def readFriendship():
      Friendship = open('friend.txt')
      return Friendship

def readWordTweet():
      WordTweet = open('word.txt', encoding='utf-8')
      return WordTweet


def initUserSet():
      global UserSet
      UserProfile = readUserProfile()
      k = 0
      tmpUserId = None
      tmpUserName = None
      for line in UserProfile:
            line = line[0:-1]
            determinent = k%4
            if(determinent == 0):
                  tmpUserId = int(line)
            elif(determinent == 2):
                  tmpUserName = line
                  UserSet.append([tmpUserId,tmpUserName])
            k= k + 1
      heapsort(UserSet,0)
      
def initFriendSet():
      global FriendSet
      Friendship = readFriendship()
      k = 0
      tmpFriendFrom = None
      tmpFriendTo = None
      for line in Friendship:
            line = line[0:-1]
            determinent = k%3
            if(determinent == 0):
                  tmpFriendFrom = int(line)
            elif(determinent == 1):
                  tmpFriendTo = int(line)
                  FriendSet.append([tmpFriendFrom,tmpFriendTo])
            k = k + 1
      heapsort(FriendSet,0)

def initTweetSet():
      global TweetSet
      WordTweet = readWordTweet()
      k = 0
      tmpTweetBy = None
      tmpTweetWord = None
      for line in WordTweet:
            line = line[0:-1]
            determinent = k%4
            if(determinent == 0):
                  tmpTweetBy = int(line)
            elif(determinent == 2):
                  tmpTweetWord = line
                  TweetSet.append([tmpTweetBy,tmpTweetWord])
            k = k + 1
      heapsort(TweetSet,0)

def searchTweetWord(word):
      global TweetSet
      index = []
      for i in range(len(TweetSet)):
            if(TweetSet[i][1] == word):
                  index.append(i)
      return index

def searchTweetUser(user):
      global TweetSet
      index = []
      for i in range(len(TweetSet)):
            if(TweetSet[i][1] == user):
                  index.append(i)
      return index

def deleteTweetWord(word):
      global TweetSet
      l = len(TweetSet)
      for i in range(l):
            if(TweetSet[l-i-1][0] == word):
                  del TweetSet[l-i-1]                 
      return print('deleted')

def deleteTweetUser(user):
      global TweetSet
      l = len(TweetSet)
      for i in range(l):
            if(TweetSet[l - i -1][1] == user):
                  del TweetSet[l - i -1]
      return print('deleted')

def deleteFriendFrom(user):
      global FriendSet
      l = len(FriendSet)
      for i in range(l):
            if(FriendSet[l - i -1][1] == user):
                  del FriendSet[l - i -1]

def getUserName(user):
    global UserSet
    return UserSet[binary_search(UserSet, user, 0)][1]

def minFriend():
      global FriendSet
      heapsort(FriendSet,0)
      Min = len(FriendSet)
      tmpUser = FriendSet[0][0]
      tmpFriendNum = 0
      for i in range(len(FriendSet)):
            if(tmpUser == FriendSet[i][0]):
                  tmpFriendNum = tmpFriendNum + 1
            else:
                  if(Min > tmpFriendNum):
                        Min = tmpFriendNum
                        tmpUser = TweetSet[i][0]
                        tmpFriendNum = 1
                  else:
                        tmpUser = TweetSet[i][0]
                        tmpFriendNum = 1
      return Min

def maxFriend():
      global FriendSet
      heapsort(FriendSet,0)
      Max = 0
      tmpUser = FriendSet[0][0]
      tmpFriendNum = 0
      for i in range(len(FriendSet)):
            if(tmpUser == FriendSet[i][0]):
                  tmpFriendNum = tmpFriendNum + 1
            else:
                  if(Max < tmpFriendNum):
                        Max = tmpFriendNum
                        tmpUser = TweetSet[i][0]
                        tmpFriendNum = 1
                  else:
                        tmpUser = TweetSet[i][0]
                        tmpFriendNum = 1
      return Max

def minTweet():
      global TweetSet
      heapsort(TweetSet,0)
      Min = len(TweetSet)
      tmpUser = TweetSet[0][0]
      tmpTweetNum = 0
      for i in range(len(TweetSet)):
            if(tmpUser == TweetSet[i][0]):
                  tmpTweetNum = tmpTweetNum + 1
            else:
                  if(Min > tmpTweetNum):
                        Min = tmpTweetNum
                        tmpUser = TweetSet[i][0]
                        tmpTweetNum = 1
                  else:
                        tmpUser = TweetSet[i][0]
                        tmpTweetNum = 1
      return Min

def maxTweet():
      global TweetSet
      heapsort(TweetSet,0)
      TweetMax = 0
      tmpUser = TweetSet[0][0]
      tmpTweetNum = 0
      for i in range(len(TweetSet)):
            if(tmpUser == TweetSet[i][0]):
                  tmpTweetNum = tmpTweetNum + 1
            else:
                  if(TweetMax < tmpTweetNum):
                        TweetMax = tmpTweetNum
                        tmpUser = TweetSet[i][0]
                        tmpTweetNum = 1
                  else:
                        tmpUser = TweetSet[i][0]
                        tmpTweetNum = 1
      return TweetMax

def top5Tweet():
      global TweetSet
      heapsort(TweetSet,1)
      uniqueWord = []
      tmpWord = TweetSet[0][1]
      tmpWordNum = 0
      for i in range(len(TweetSet)):
            if(tmpWord == TweetSet[i][1]):
                  tmpWordNum = tmpWordNum + 1
            else:
                  uniqueWord.append([tmpWord,tmpWordNum])
                  tmpWord = TweetSet[i][1]
                  tmpWordNum = 1
      heapsort(uniqueWord,1)
      top5Word = []
      for i in range(5):
          top5Word.append(uniqueWord[len(uniqueWord) - i -1])
      return top5Word

def top5User():
      global TweetSet
      heapsort(TweetSet,0)
      uniqueUser = []
      tmpUser = TweetSet[0][0]
      tmpUserNum = 0
      for i in range(len(TweetSet)):
            if(tmpUser == TweetSet[i][0]):
                  tmpUserNum = tmpUserNum + 1
            else:
                  uniqueUser.append([tmpUser,tmpUserNum])
                  tmpUser = TweetSet[i][0]
                  tmpUserNum = 1
      heapsort(uniqueUser,1)
      top5User = []
      for i in range(5):
          top5User.append(getUserName(uniqueUser[len(uniqueUser)-i-1][0]))
      return top5User

def searchUserWord(word):
    index = searchTweetWord(word)
    mentionUser = []
    for i in range(len(index)):
        mentionUser.append(TweetSet[index[i]][0])
    return mentionUser

def friendofUser(user):
    friend = []
    for i in range(len(FriendSet)):
        if(user == FriendSet[i][0]):
            friend.append(getUserName(FriendSet[i][0]))
    return friend

def getFriend(user):
    friend = []
    for i in range(len(FriendSet)):
        if(user == FriendSet[i][0]):
            friend.append(FriendSet[i][0])
    return friend
            

########## User Interface################################################

def UserInterFace():
      MenuList()
      return SelectMenu()


def MenuList():
      print('0. Read data files')
      print('1. Display statistics')
      print('2. Top 5 most tweeted users')
      print('3. Top 5 most tweeted users')
      print('4. Find users who tweeted a word(e.g, yeounsaedae)')
      print('5. Find all people who are friends of the above users')
      print('6. Delete all mentions of a word')
      print('7. Delete all users who mentioned a word')
      print('8. Find strongly connected components')
      print('9. Find shortest path from a given user')
      print('99. Quit')

def SelectMenu():
      selected = input('Select Menu : ')
      try:
            selected = int(selected)
            if(((selected >= 0)and(selected <= 9)) or selected == 99):
                  return selected
            else:
                  print('No such Menu')
                  SelectMenu()
      except ValueError:
            print('input should be integer type')
            SelectMenu()

def Menu0():
      initUserSet()
      initFriendSet()
      initTweetSet()
      print('Total users : ' + str(len(UserSet)))
      print('Total friendship records : ' + str(len(FriendSet)))
      print('Total tweets : ' + str(len(TweetSet)))

def Menu1():
      global UserSet
      global FriendSet
      global TweetSet
      print('Average numer of friends : ' + str(len(FriendSet)/len(UserSet)))
      print('Minimum friends : ' + str(minFriend()))
      print('Maximum number of friends : '  + str(maxFriend()))
      print('')
      print('Average tweets per user : ' + str(len(TweetSet)/len(UserSet)))
      print('Minimum tweets by user : ' + str(minTweet()))
      print('Maximum tweets by user : ' + str(maxTweet()))


def Menu2():
    print('Top 5 most tweeted words : ')
    print(top5Tweet())

def Menu3():
    print('Top 5 most tweeted users : ')
    print(top5User())

def Menu4():
    word = input('keyword : ')
    users = searchUserWord(word)
    for i in range(len(users)):
        print(getUserName(users[i]))
    return users

def Menu5(users):
    print('who are friend of the above users')
    friends = []
    for i in range(len(users)):
        print(friendofUser(users[i]))

def Menu6():
    word = input('keyword to delete : ')
    deleteTweetWord(word)

def Menu7():
    word = input('keyword to delete who mentioned : ')
    users = searchUserWord(word)
    users.sort(reverse = True)
    for i in range(len(users)):
        k = binary_search(UserSet, users[i], 0)
        if(k != None):
            del UserSet[k]
        deleteTweetUser(users[i])
        deleteFriendFrom(users[i])

def Controller():
      global SelectedUser
      Selected = UserInterFace()
      
      if(Selected == 0):
            Menu0()
            return True
      elif(Selected == 1):
            Menu1()
            return True
      elif(Selected == 2):
            Menu2()
            return True
      elif(Selected == 3):
            Menu3()
            return True
      elif(Selected == 4):
            SelectedUser = Menu4()
            return True
      elif(Selected == 5):
            Menu5(SelectedUser)
            return True
      elif(Selected == 6):
            Menu6()
            return True
      elif(Selected == 7):
            Menu7()
            return True
      elif(Selected == 8):
            Menu8()
            return True
      elif(Selected == 9):
            Menu9()
            return True
      elif(Selected == 99):
            return False


########## Main ###################################################

FLOW = True
while FLOW:
      FLOW = Controller()
      print('')

BFS_main()

