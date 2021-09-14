# Design Approach:
# create functions to display board grids as needed
# game spaces represented as a data structure
# receive input from the user to determine which index of the board lists shall be replaced with their choice



# create empty board spaces
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# create welcome message and head border
head_string = " "
for number in range(1, len(board)+1):
  head_string += " | " + str(number) + " | "
welcome_message = "~ Welcome to CoNnEcT fOuR ~\n"
space_length = int((len(head_string) - len(welcome_message))/2)
print(' '*space_length + welcome_message + ' '*space_length)
print('-'*(len(head_string)+1))
print(head_string)

# define horizontal line function
def horizontal_line():
  hor_string = ""
  for i in range(1,len(head_string)+2):
    hor_string += "-"
  print(hor_string)

horizontal_line()

# create remaining grid lines
# add all column grid lines
for row in range(len(board[0])):
  print('|      ' * (len(board) +1))
  
  #add all row grid lines plus items
  filled_rows = ""

  for col in range(len(board)):
    filled_rows += ('|   ' + str(board[col][row])) + '  '
  print(filled_rows + '|')
  print('|      ' * (len(board) +1))
  print('o------' * (len(board)) + 'o')

# print bottom grid line
horizontal_line()



