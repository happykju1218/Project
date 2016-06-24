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
      for i in range(len(TweetSet)):
            if(TweetSet[i][0] == word):
                  del TweetSet[i]                 
      return print('deleted')

def deleteTweetUser(user):
      global TweetSet
      for i in range(len(TweetSet)):
            if(TweetSet[i][1] == user):
                  del TweetSet[i]
      return print('deleted')

def deleteFriendFrom(user):
      global FriendSet
      for i in range(len(FriendSet)):
            if(FriendSet[i][1] == user):
                  del FriendSet[i]

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


#A = [[1,'ㄱㅣㅁ'],[2,'ㅈㅓㅇ'],[3,'ㅇㅜㄱ']]
#heapsort(A,1)

#print(A)
#A.sort()
#print(('A'))
#print(top5Tweet())
#k = input('input :')
#a = searchUserWord(k)

#for i in range(len(a)):
#    print(a[i])

