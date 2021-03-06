import datetime
import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='mysql',
                           database='TheWoods')
while True:
    password=input("Enter password for access to THE WOODS database:")
    if password=="jack123":
        break
    else:
        print("Wrong password, please try again.")
        print()
        print()
        print()
        continue
while True:
    print("""

  ------------------------------------------------------
 |======================================================|
 |========        THE WOODS GOLFING CLUB        ========|
 |======================================================|
  ------------------------------------------------------

 1 : Course Details
 2 : Add a new membership- Member details
 3 : Show all packages
 4 : Add/Delete Membership
 5 : Show all Memberships
 6 : Tournaments and Busy dates
 7 : Find Member
 8 : About us

""")
    ch=int(input("Enter your choice: "))
    if (ch==1):
        c1='y'
        while (c1=='y'):
            print()
            cursor=db.cursor()
            cursor.execute("Select * from Courses;")
            lis1=[]
            row=cursor.fetchone()
            while row is not None:
                lis1.append(row)
                row=cursor.fetchone()
            print ("="*60)
            print("{0:10}{1:^16}{2:^20}{3:>10}".format("TEE","YARDAGE","COURSE RATING",
                                                              "SLOPE RATING"))
            print ("-"*60)
            for element in lis1:
                  print ("{0:10}{1:^16}{2:^20}{3:>10}".format(element[0],element[1],
                                                                     element[2],element[3]))
            print ("-"*60)
            cursor.close()
            print()
            print()
            co=input("Press Enter to return to main menu:")
            if co:
                break
            break
    elif (ch==2):
        cl='y'
        while (cl=='y'):
            print ()
            name=input("Enter name: ")
            phone=input("Enter phone number: ")
            doj=input("Enter date-of-joining in <yyyy-mm-dd>: ")
            memid=input("Enter member ID: ")
            sex=input ("Enter sex: ")
            cursor=db.cursor()
            query="insert into Names values(%s,%s,%s,%s,%s)"
            data=(name,phone,doj,memid,sex)
            cursor.execute(query,data)
            db.commit()
            cursor.close()
            print()
            print ("The member has been added to the database!")
            print()
            c1=input("Do you want to continue <y/n>: ")
            if c1=='y':
                continue
            else:
                print()
                print()
                print()
                break
    elif (ch==3):
        c1='y'
        while (c1=='y'):
            print()
            print()
            print ("""
 1.BRONZE MEMBERSHIP
   Enjoy access to our coveted courses, driving range and free use of our
   in-house equipment. All other THE WOODS services are available and
   chargeable. Restricted areas not included.

 2.SILVER MEMBERSHIP
   Enjoy access to our coveted courses, driving range and free use of
   our in-house equipment. Complimentary drinks on arrival. Entry in
   "The 19th bar" included. Free Coupons worth $50 of the "All day lounge"
   per month. Free access to the gym, tennis court and swimming pool

 3.GOLD MEMBERSHIP
   All the perks in the sliver memnership. Free Coupons worth $200 of the
   "All day lounge" per month. Free Callaway Putter on start of membership.
   Use of conference room available and chargeable. Complimentary drinks at
   "The 19th Bar".
   """)
            print()
            print()
            cursor=db.cursor()
            cursor.execute("Select * from Packages;")
            lis1=[]
            row=cursor.fetchone()
            while row is not None:
                lis1.append(row)
                row=cursor.fetchone()
            print ("="*45)
            print ("{0:<16}{1:^16}{2:>10}".format("MEMBERSHIP TYPE", "DURATION",
                                                  "FEE"))
            print ("-"*45)
            for element in lis1:
                   print ("{0:<16}{1:^16}{2:>10}".format(element[0],element[1],
                                                         element[2]))
            print ("-"*45)
            cursor.close()
            print()
            print()
            co=input("Press Enter to return to main menu:")
            if co:
                break
            break
    elif (ch==4):
        cl='y'
        while (cl=='y'):
            print ()
            while True:
                print ("""
 a : Add Member
 b : Remove Member
 c : Exit
            """)
                ch1=input("Enter what do you want to do: ")
                if (ch1=='a'):
                    cl1='y'
                    while (cl1=='y'):
                        print ()
                        Mem_ID=input("Enter Member ID: ")
                        name=input("Enter name: ")
                        package=input("Enter package: ")
                        duration=input("Enter duration: ")
                        start=input("Enter start date in <yyyy-mm-dd>: ")
                        ev_id=input("Enter upcoming event ID: ")
                        if not ev_id:
                            ev_id='nil'
                        cursor=db.cursor()
                        query="insert into Memberships values(%s,%s,%s,%s,%s,%s);"
                        data=(Mem_ID,name,package,duration,start,ev_id)
                        cursor.execute(query,data)
                        db.commit()
                        cursor.close()
                        print()
                        print ("The member has been added to the Memberships list!")
                        print()
                        cl1=input("Do you want to continue? <y/n>: ")
                        if (co=='y'):
                            continue
                        else:
                            break
                elif (ch1=='b'):
                    cl1='y'
                    while (cl1=='y'):
                        print()
                        Mem_ID=input("Enter the ID of the member who you want to remove: ")
                        cursor=db.cursor()
                        query=("delete from Memberships where Member_Id="+Mem_ID+";")
                        cursor.execute(query)
                        db.commit()
                        cursor.close()
                        print()
                        print ("The Member has been removed from the Membership table!")
                        print()
                        cl1=input("Do you want to continue? <y/n>: ")
                        if (cl1=='y'):
                            continue
                        else:
                            break
                elif (ch1=='c'):
                    break
                break
            break
    elif (ch==5):
        print()
        print()
        cursor=db.cursor()
        cursor.execute ("select * from Memberships;")
        lis1=[]
        row=cursor.fetchone()
        while row is not None:
                lis1.append(row)
                row=cursor.fetchone()
        print ("="*105)
        print("{0:15}{1:^20}{2:^16}{3:^16}{4:^20}{5:>18}".format("Member ID","Name","Package",
                                                                 "Duration", "Starting Date",
                                                                 "Upcoming Event ID"))
        print ("-"*105)
        for el in lis1:
            print ("{0:15}{1:^20}{2:^16}{3:^16}{4:^20}{5:>18}".format(el[0],el[1],el[2],
                                                                      el[3],el[4].strftime("%Y-%m-%d"),
                                                                      el[5]))
        cursor.close()
        print ("-"*105)
        print()
        print()
        co=input("Press Enter to return to Main Menu:")
        if co:
            break
    elif (ch==6):
        print()
        print()
        cursor=db.cursor()
        cursor.execute ("select * from Events;")
        lis1=[]
        row=cursor.fetchone()
        while row is not None:
                lis1.append(row)
                row=cursor.fetchone()
        print ("="*133)
        print("{0:35}{1:^35}{2:^18}{3:^20}{4:>15}".format("Event","Date",
                                                          "Prize Money","Exclusivity",
                                                          "Status"))
        print ("-"*133)
        for el in lis1:
              print("{0:35}{1:^35}{2:^18}{3:^20}{4:>15}".format(el[0],el[1],el[2],
                                                                el[3],el[4]))
        cursor.close()
        print ("-"*133)
        print()
        print()
        co=input("Press Enter to return to Main Menu:")
        if co:
            break
    elif (ch==7):
        print()
        print()
        Mem_Id=input("Enter the Member Id: ")
        cursor=db.cursor()
        query=("select * from Memberships where Member_Id="+Mem_Id+";")
        cursor.execute(query)
        el = cursor.fetchone()
        print ("="*105)
        print("{0:15}{1:^20}{2:^16}{3:^16}{4:^20}{5:>18}".format("Member ID","Name","Package",
                                                                 "Duration", "Starting Date",
                                                                 "Upcoming Event ID"))
        print ("-"*105)
        print ("{0:15}{1:^20}{2:^16}{3:^16}{4:^20}{5:>18}".format(el[0],el[1],el[2],
                                                                  el[3],el[4].strftime("%Y-%m-%d"),
                                                                  el[5]))
        cursor.close()
        print ("-"*105)
        print()
        print()
        co=input("Press Enter to return to Main Menu:")
        if co:
            break
    else:
        print()
        print()
        print ("""
                          THE WOODS GOLFING CLUB

        
    Opened in 2005, The Woods begins atop a massive sand dune, then
    quickly opens into a sprawling meadow. The routing then works higher
    into the coastal forest, before finally returning to finish in the
    dunes. The course is enjoyable to walk and is a constant reminder of
    how the game was originally createdmong inland rolling dunes with
    dramatic ocean vistas.

    The Woods, the centerpiece of The Leela Kempinski, remains one of
    India’s most celebrated golf courses. It has served as the site of
    more single golf championships than any course in India and hosted
    back-to-back Louis Phillipe Open and Tissot Championships for the first
    time in 2014. The Louis Phillipe Open will return in 2024.

    
    The Woods is best known for its crowned, undulating greens, which are some
    of the most complex and widely hailed in the world. Ross believed in
    providing golfers with strategic choices, and Pinehurst No. 2 was intended
    to epitomize that philosophy.
              """)
        print()
        print()
        co=input("Press Enter to return to Main Menu:")
        if co:
            break
