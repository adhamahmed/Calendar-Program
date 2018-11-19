userChoice = input ("Welcome! \n \nPlease choose an option using the numbers: \n 1 View all calendar entries \n 2 Write a new entry \n 3 Edit existing entries \n 4 Exit the program \n \nChoice: ")

while (userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4'):
  print ("\nSorry, I didn't quite get that ")
  userChoice = input ("Choice: ")

if userChoice == '1': #this if statement prints all the existing entries
  print ("\nCalendar Entries:\n ")
  f = open('calendar.txt','r')
  message = f.read()
  print(message)
  f.close()
if userChoice == '2': #this if statement allows you to create a new entry, with an entry ID, date, and event name
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
if userChoice == '3': #this if statement allows you to edit existing entries
   pass
if userChoice == '4': #this if statement ends the program
 print("The program is now closing")
 exit()
