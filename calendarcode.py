# Calendar Program is a utility program set inside a command line interface that allows you 
# to read, write, and edit entries in a calender which is stored within a text file.

# Gets the user input
userChoice = input ("Welcome! \n \nPlease choose an option using the numbers: \n 1 View all calendar entries \n 2 Write a new entry \n 3 Edit existing entries \n 4 Exit the program \n \nChoice: ")

# If user inputs an incorrect number it will loop back
while (userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4'):
  print ("\nSorry, I didn't quite get that ")
  userChoice = input ("Choice: ")

# This if statement prints all the existing entries
if userChoice == '1': 
  print ("\nCalendar Entries:\n ")
  f = open('calendar.txt','r')
  message = f.read()
  print(message)
  f.close()
  
# This if statement allows you to create a new entry, with an entry ID, date, and event name
if userChoice == '2': 
  print ("\nAdd a new entry:\n ")
  f = open('calendar.txt','a')
  newEntryID = input ("Please enter a new entry number ")
  f.write("\n")
  f.write(newEntryID)

  f.write(" ")

  newDay = input ("Please enter the Day")
  f.write(newDay)
  f.write("/")

  newMonth = input ("Please enter the Month")
  f.write(newMonth)
  f.write("/")

  newYear = input ("Please enter the Year ")
  f.write(newYear)

  print ("\n")
  newEvent = input ("What event would you like to add? ")
  print ("")
  f.write(" ")
  f.write(newEvent)

  print ("New entry has been added to the calendar")
  f.close() 
  
# This if statement allows you to edit existing entries  
if userChoice == '3': #this if statement allows you to edit existing entries
   pass
  
# This if statement ends the program  
if userChoice == '4': 
 print("The program is now closing")
 exit()
