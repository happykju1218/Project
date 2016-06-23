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
      selected = input('Select Menu :')
      try:
            selected = int(selected)
            return selected
      except ValueError:
            print('input should be integer type')
            SelectMenu()

UserInterFace()
