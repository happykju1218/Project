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

totalUserNum = 0
totalFriendNum = 0
totalTweetNum = 0

UserSet = []
FriendSet = []
TweetSet = []

def initUserSet():
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
                  totalUserNum = totalUserNum + 1
            k= k + 1
      
def initFriendSet():
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
                  totalFriendNum = totalFriendNum  + 1
            k = k + 1

def initTweetSet():
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
                  totalTweetNum = totalTweetNum + 1
            k = k + 1
            


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
      print('Total users : ' + str(totalUserNum))
      print('Total friendship records : ' + str(totalFriendNum))
      print('Total tweets : ' + str(totalTweetNum))

def Controller():
      
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


########## Main ###################################################

FLOW = True
while FLOW:
      FLOW = Controller()
