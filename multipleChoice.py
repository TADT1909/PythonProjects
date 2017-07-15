# https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
ans=True
while ans:
    print ("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1":
      print("\n Student Added")
      exit()
    elif ans=="2":
      print("\n Student Deleted")
      exit()
    elif ans=="3":
      print("\n Student Record Found")
      exit()
    elif ans=="4":
      print("\n Goodbye")
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")