# encoding=utf8
# -*- coding: utf-8 -*-
import operator

##########Class and Functions for Administrivia###################################################

'''------------------linked list START-----------------'''
class linkedListNode:
      def __init__(self,val):
            self.val = val
            self.prev = None
            self.next = None
            
class linkedList:
      def __init__(self):
            self.start = None
      def insert(self,val):
            newNode = linkedListNode(val)
            tmpS = self.start
            self.start = newNode
            newNode.next = tmpS
            if(tmpS != None):
                  tmpS.prev = newNode
      def delete(self,val):
            current = self.start
            while current:
                  if(val == current.val):
                        if(current.prev != None):
                              current.prev.next = current.next
                              current.next.prev = current.prev
                        else:
                              self.start = current.next
                              current.next.prev = None
                  current = current.next
                  
"""-------------------linked list END-----------------------"""

"""--------------------binary search (pointer)tree Start-----------------------"""

class binarySearchPointerTreeNode:
      def __init__(self,point,val):
            self.val = val
            self.point = point
            self.left = None
            self.right = None
            self.parant = None # if parant is none => root node.

class binarySearchPointerTree:
      def __init__(self):
            self.root = None

      def insert(self, point, val):
            newNode = binarySearchPointerTreeNode(point,val)
            if (self.root == None):
                  self.root = newNode
                  return 
            else:
                  tmp1 = self.root
                  tmp2 = None
                  tmp3 = True
                  while tmp1:
                        tmp2 = tmp1
                        if (tmp1.val < newNode.val):
                              tmp1 = tmp1.right
                        elif(tmp1.val > newNode.val):
                              tmp1 = tmp1.left
                              tmp3 = False
                        else:
                              return print('error(has same value)')
                  if (tmp3):
                        tmp2.right = newNode
                        newNode.parant = tmp2
                        return 
                  else:
                        tmp2.left = newNode
                        newNode.parant = tmp2
                        return 
                  return print('error')

      def search(self,val):
            tmp = self.root
            while tmp:
                  if (tmp.val < val):
                        tmp = tmp.right
                  elif(tmp.val > val):
                        tmp = tmp.left
                  else:
                        return tmp
            return None
            
      def delete(self,val):
            tmp = self.search(val)
            if (tmp != None):
                  if(tmp.left == None):
                        self.transplant(tmp,tmp.right)
                  elif (tmp.right == None):
                        self.transplant(tmp,tmp.left)
                  else:
                        tmpS = tmp.right
                        while tmpS.left:
                              tmpS = tmpS.left
                        if (tmpS.parant != tmp):
                              self.transplant(tmpS,tmpS.right)
                              tmpS.right = tmp.right
                              tmpS.right.parant = tmpS
                        self.transplant(tmp,tmpS)
                        tmpS.left = tmp.left
                        tmpS.left.parnat = tmpS
            else:
                  return None

      def transplant(self,f,g):
            if (f.parant == None):
                  self.root = g
            elif (f == f.parant.left):
                  f.parant.left = g
            else:
                  f.parant.right = g
            if(g != None):
                  g.parant = f.parant

"""-------------------binary search (pointer)tree END--------------------------"""

"""-----------------heap sort Start------------------------"""

def heapify(A,i,heapsize):
    l = left(i)
    r = right(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A,largest,heapsize)

def buildheap(A):
    for i in range(len(A)//2 + 1,0,-1):
        heapify(A,i-1,len(A))

def heapsort(A):
    buildheap(A)
    for i in range(len(A),1,-1):
        A[i-1],A[0] = A[0],A[i-1]
        heapify(A,0,i - 1)

def parent(n):
    return (n-1)//2

def left(n):
    return 2*n+1

def right(n):
    return 2*n+2

"""---------------------heap sort END---------------------"""


############################################################################

##########Main Class##########################################################

"""-----------------User Manage------------------------"""

class User:
      def __init__(self):
            self.name = None
            self.id = None
            self.friends = linkedList()
            self.friendsNum = 0
            self.tweet = linkedList()
            self.tweetNum = 0
      def setName(self,name):
            self.name = name
      def setUserId(self,id):
            self.id = id
      def addFriend(self,friend):
            self.friends.insert(friend)
            self.friendsNum = self.friendsNum + 1
            global TotalFriendships
            TotalFriendships = TotalFriendships + 1
      def deleteFriend(self,friend):
            self.friends.delete(friend)
            if (self.friendsNum <= 0):
                  print('error(no_frined)')
            else:
                  self.friendsNum = self.friendsNum - 1
                  global TotalFriendships
                  TotalFriendships = TotalFriendships - 1
      def addTweet(self,tweet):
            self.tweet.insert(tweet)
            self.tweetNum = self.tweetNum + 1
            global TotalTweets
            TotalTweets = TotalTweets + 1
      def deleteTweet(self,tweet):
            self.tweet.delete(tweet)
            if (self.tweetNum <= 0):
                  print('error(no_tweet)')
            else:
                  self.tweetNum = self.tweetNum -1
                  global TotalTweets
                  TotalTweets = TotalTweets - 1

class UserSet:
      def __init__(self):
            self.userTree = binarySearchPointerTree()
            self.UserArr = []

      def insertUser(self,user):
            if(self.userTree.search(user.id) == None):
                  self.userTree.insert(user,user.id)
                  global TotalUsers
                  TotalUsers = TotalUsers + 1
            else:
                  print('error(has same value)')
      def deleteUser(self,userid):
            user = self.searchUser(userid)
            if(user != None):
                  global TotalUsers
                  TotalUsers = TotalUsers - 1
            ITweetSet.deletebyTweeter(userid)
            self.userTree.delete(userid)

      def searchUser(self,userid):
            searchedNode = self.userTree.search(userid)
            if(searchedNode != None):
                  return searchedNode.point
            else:
                  return None

      def getAllUser(self):
            self.UserArr = []
            self.travel(self.userTree.root)
            return self.UserArr
      
      def travel(self,tree):
            if (tree.left):
                  self.travel(tree.left)
            self.UserArr.append(tree.point)
            if (tree.right):
                  self.travel(tree.right)

"""-------------Tweet Manage-------------------"""

class Tweet:
      def __init__(self):
            self.tweetedBy = None
            self.tweetWord = None
            self.tweetTime = None
            self.prevTweet = None
            self.nextTweet = None
      def setTweeter(self,userid):
            self.tweetedBy = userid
            tmpTweeter = IUserSet.searchUser(userid)
            if (tmpTweeter != None):
                  tmpTweeter.addTweet(self)
      def setTweetWord(self,word):
            self.tweetWord = word
      def setTweetTime(self,time):
            self.tweetTime = time

class TweetSet:
      def __init__(self):
            self.tweetListStart = None
            self.tweetToArr = []
            
      def insertTweet(self,tweet):
            tmpS = self.tweetListStart
            self.tweetListStart = tweet
            tweet.nextTweet = tmpS
            if(tmpS != None):
                  tmpS.prevTweet = tweet
                  
      def deletebyWord(self,tweetWord):
            tmpS = self.tweetListStart
            while tmpS:
                  if(tmpS.tweetWord == tweetWord):
                        if(tmpS.prevTweet != None):
                              if(tmpS.nextTweet !=None):
                                    tmpS.prevTweet.nextTweet = tmpS.nextTweet
                                    tmpS.nextTweet.prevTweet = tmpS.prevTweet
                              else:
                                    tmpS.prevTweet.nextTweet = tmpS.nextTweet
                        else:
                              if(tmpS.nextTweet !=None):
                                    self.tweetListStart = tmpS.nextTweet
                                    tmpS.nextTweet.prevTweet = None
                              else:
                                    self.tweetListStart = tmpS.nextTweet
                  tmpS = tmpS.nextTweet

      def searchbyWord(self,tweetWord):
            tmpS =self.tweetListStart
            tmpArr = []
            while tmpS:
                  if(tmpS.tweetWord == tweetWord):
                        tmpArr.append(tmpS)
                  tmpS = tmpS.nextTweet
            return tmpArr

      def searchbyTweeter(self,TweeterId):
            tmpS =self.tweetListStart
            tmpArr = []
            while tmpS:
                  if(tmpS.tweetedBy == TweeterId):
                        tmpArr.append(tmpS)
                  tmpS = tmpS.nextTweet

            return tmpArr

      def deletebyTweeter(self,TweeterId):
            tmpS = self.tweetListStart
            while tmpS:
                  if(tmpS.tweetedBy == TweeterId):
                        if(tmpS.prevTweet != None):
                              if(tmpS.nextTweet !=None):
                                    tmpS.prevTweet.nextTweet = tmpS.nextTweet
                                    tmpS.nextTweet.prevTweet = tmpS.prevTweet
                              else:
                                    tmpS.prevTweet.nextTweet = tmpS.nextTweet
                        else:
                              if(tmpS.nextTweet !=None):
                                    self.tweetListStart = tmpS.nextTweet
                                    tmpS.nextTweet.prevTweet = None
                              else:
                                    self.tweetListStart = tmpS.nextTweet                  
                  tmpS = tmpS.nextTweet

      def makeTweetArr(self):
            tmp = self.tweetListStart
            while tmp:
                  self.tweetToArr.append(str(tmp.tweetWord))
                  tmp = tmp.nextTweet
            return self.tweetToArr
            
            

#####################################################################

##########Main Functions###############################################

"""--Variables--"""
global TotalUsers
TotalUsers = 0
global TotalFriendships
TotalFriendships = 0
global TotalTweets
TotalTweets = 0
#global IUserSet
IUserSet = UserSet()
#global ITweetSet0
ITweetSet = TweetSet()
global SearchedArray
SearchedArray = []

"""------------"""

"""------------read data----------------"""
def readUserProfile():
      UserProfile = open('user.txt')
      return UserProfile
      
def readFriendship():
      Friendship = open('friend.txt')
      return Friendship

def readWordTweet():
      WordTweet = open('word.txt', encoding='utf-8')
      return WordTweet
"""------------initialize data set--------------"""
def initUserSet(newUserSet):
      totalUserNum = 0
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
                  newUser = User()
                  newUser.setUserId(tmpUserId)
                  newUser.setName(tmpUserName)
                  newUserSet.insertUser(newUser)
                  totalUserNum = totalUserNum + 1
            k= k + 1
      return totalUserNum
      
      
def initFriendship(UserSet):
      totalFriendshipNum = 0
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
                  FromUser = UserSet.searchUser(tmpFriendFrom)
                  ToUser = UserSet.searchUser(tmpFriendTo)
                  if ((FromUser != None) & (ToUser != None)):
                        FromUser.addFriend(ToUser)
                        totalFriendshipNum = totalFriendshipNum + 1
            k = k + 1
      return totalFriendshipNum
      
def initTweetSet(newTweetSet):
      totalTweetsNum = 0
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
                  newTweet = Tweet()
                  newTweet.setTweeter(tmpTweetBy)
                  newTweet.setTweetWord(tmpTweetWord)
                  newTweetSet.insertTweet(newTweet)
                  totalTweetsNum = totalTweetsNum + 1
            k = k + 1
      return totalTweetsNum

"""----------------Statistics------------------"""

def stat_AvgNumFriends():
      global TotalUsers
      global TotalFriendships
      return TotalFriendships/TotalUsers

def stat_SortbyFriendNum(UserSet):
      tmp1Arr = UserSet.getAllUser()
      tmp2Arr = []
      for i in range(0,len(tmp1Arr)):
            tmp2Arr.append(tmp1Arr[i].friendsNum)
      heapsort(tmp2Arr)
      return tmp2Arr

def stat_MinMaxNumFriends(UserSet):
      tmp = stat_SortbyFriendNum(UserSet)
      return [tmp[0],tmp[len(tmp)-1]]

def stat_AvgNumTweets():
      global TotalTweets
      global TotalUsers
      return TotalTweets/TotalUsers

def stat_SortbyTweetNum(UserSet):
      tmp1Arr = UserSet.getAllUser()
      tmp2Arr = []
      for i in range(0,len(tmp1Arr)):
            tmp2Arr.append(tmp1Arr[i].tweetNum)
      heapsort(tmp2Arr)
      return tmp2Arr

def stat_MinMaxNumTweets(UserSet):
      tmp = stat_SortbyTweetNum(UserSet)
      return [tmp[0],tmp[len(tmp)-1]]

def stat_top5Tweet(TweetSet):
      Arr = TweetSet.makeTweetArr()
      result = dict(((x, Arr.count(x)) for x in set(Arr)))
      sortedTweet = sorted(result.items(), key=operator.itemgetter(1),reverse=True)
      top5Arr = []
      for i in range(5):
            top5Arr.append(sortedTweet[i][0])
      return top5Arr

def getKey(item):
      return item.tweetNum


def stat_top5User(UserSet):
      Arr = UserSet.getAllUser()
      Arr.sort(reverse = True, key = getKey)
      top5Arr = []
      for i in range(5):
            top5Arr.append(Arr[i].name)
      return top5Arr
      
"""graph"""

class Graph:
      def __init__(self):
           self.nodes = set()
           self.edges = defaultdict(list)
           self.distances = {}
      def add_node(self, value):
           self.nodes.add(value)

      def add_edge(self, from_node, to_node, distance):
           self.edges[from_node].append(to_node)
           self.edges[to_node].append(from_node)
           self.distances[(from_node, to_node)] = distance

def find_min(nodes, visited):
          min_node = None
          for node in nodes:
              if node in visited:
                  if min_node is None:
                      min_node = node
                  elif visited[node] < visited[min_node]:
                      min_node = node
          return min_node

def relax(graph, visited, current_weight, min_node):
        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
               path[edge] = min_node

def dijsktra(graph, initial):
          visited = {'initial': 0}
          path = {}
          nodes = set(graph.nodes)
          while nodes:
                    min_node = find_min(nodes)
                   nodes.remove(min_node)
                   current_weight = visited[min_node]

                    relax(graph, visited, current_weight, min_node)
          return visited, path

#TotalUsers = 0
#TotalFriendships = 0
#TotalTweets = 0


#################################################################

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
      

################################################################

##########Controller#################################################

def Menu0():
      global TotalUsers
      global TotalFriendships
      global TotalTweets
      TotalUsers = initUserSet(IUserSet)
      TotalFriendships = initFriendship(IUserSet)
      TotalTweets = initTweetSet(ITweetSet)
      print('Total users : ' + str(TotalUsers))
      print('Total friendship records : ' + str(TotalFriendships))
      print('Total tweets : ' + str(TotalTweets))

def Menu1():
      AvgNumFriends = stat_AvgNumFriends()
      MinMaxNumFriends = stat_MinMaxNumFriends(IUserSet)
      AvgNumTweets = stat_AvgNumTweets()
      MinMaxNumTweets = stat_MinMaxNumTweets(IUserSet)
      print('Average number of friends : ' + str(AvgNumFriends))
      print('Minimum friends : ' + str(MinMaxNumFriends[0]))
      print('Maximum friends : ' + str(MinMaxNumFriends[1]))
      print('Average tweets per user : ' + str(AvgNumTweets))
      print('Minimum tweets per user : ' + str(MinMaxNumTweets[0]))
      print('Maximum tweets per user : ' + str(MinMaxNumTweets[1]))

def Menu2():
      top5Tweets = stat_top5Tweet(ITweetSet)
      print('Top 5 most tweeted words')
      print(top5Tweets)

def Menu3():
      top5Users = stat_top5User(IUserSet)
      print('Top 5 most tweeted users')
      print(top5Users)

def Menu4():
      word = input('Word : ')
      searched = ITweetSet.searchbyWord(word)
      tmpArrs = []
      tmpUsers = []
      for i in range(len(searched)):
            tmpUser = IUserSet.searchUser(searched[i].tweetedBy)
            if (tmpUser != None):
                  tmpArrs.append(tmpUser.name)
                  tmpUsers.append(tmpUser)
      print('Users who mentioned ' + str(word))
      print(tmpArrs)
      return tmpUsers

def Menu5(searchedUser):
      friendOf = []
      for i in range(len(searchedUser)):
            tmp = searchedUser[i].friends.start
            while tmp:
                  friendOf.append(tmp.val.name)
                  tmp = tmp.next
      for i in range(len(friendOf)):
                  print(friendOf[i])

def Menu6():
      word = input('Word : ')
      searched = ITweetSet.searchbyWord(word)
      for i in range(len(searched)):
            tmpUser = IUserSet.searchUser(searched[i].tweetedBy)
            if (tmpUser != None):
                  tmpUser.deleteTweet(word)
      ITweetSet.deletebyWord(word)
      print('deleted')
      
def Menu7():
      word = input('Word : ')
      searched = ITweetSet.searchbyWord(word)
      for i in range(len(searched)):
            tmpUser = searched[i].tweetedBy
            if (tmpUser != None):
                  IUserSet.deleteUser(tmpUser)
      ITweetSet.deletebyWord(word)
      print('deleted')

def Menu8():
      

def Controller():
      
      Selected = UserInterFace()
      global SearchedArray
      
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
            SearchedArray = Menu4()
            return True
      elif(Selected == 5):
            Menu5(SearchedArray)
            return True
      elif(Selected == 6):
            Menu6()
            return True
      elif(Selected == 7):
            Menu7()
            return True
      elif(Selected == 8):
            return True
      elif(Selected == 9):
            return True
      elif(Selected == 99):
            return False

################################################################

########## Main ###################################################

FLOW = True
while FLOW:
      FLOW = Controller()
      

################################################################  

      
