import random
import mysql.connector as sqltr
mycon=sqltr.connect(host="localhost",user="root",passwd="12345",database="flightbook")
cursor=mycon.cursor()
print("******WELCOME TO INDIGO AIRLINES FLIGHT BOOKING WEBSITE*******")
chfirst=0
mod=0
while(mod==0):
    print("**********************************************************************************************")
    print("Please enter 1 if you want to book your tickets")
    print("Please enter 2 if you are an existing user and want to review your tickets")
    print("Please enter 3 if you are a manager(REQUIRES ADMIN ACCESS)")
    print("Please enter 4 to exit the portal")
    chfirst=int(input("Enter your response here:"))
    while(chfirst!=1 and chfirst!=2 and chfirst!=3 and chfirst!=4):
            if(chfirst!=1 and chfirst!=2 and chfirst !=3 and chfirst!=4):
                chfirst=int(input("Please enter a valid option:"))
    if(chfirst==1):
        cuname=input("Please enter your name:")
        cuphone=int(input("Please enter your phone number:"))
        while(len(str(cuphone))!=10):
            cuphone=int(input("Please enter correct 10 digit phone number:"))
        cuphone=int(cuphone)
        passenger=int(input("Please enter number of passengers:"))
        onerou=""
        while(onerou!="r" and onerou!="R" and onerou!="o" and onerou!="O"):
            onerou=input("Please choose round/oneway flight as per your flight preference r/R/o/O:")
            if(onerou!="r" and onerou!="R" and onerou!="o" and onerou!="O"):
                print("Please enter a valid option between oneway as o/O or round as r/R")
        departplace=input("From:")
        arriveplace=input("To:")
        departdate=input("Please enter departure date in the format yyyy/mm/dd:")
        if(onerou=="r" or onerou=="R"):
            modifier=False
            while(modifier!=True):
                arrivedate=input("Please enter your date of return in the same format(yyyy/mm/dd):")
                if(arrivedate<=departdate):
                    print("Please enter a valid date after you date of departure")
                else:
                    modifier=True
        modifier=False
        discount="n"
        discno=0
        while(modifier==False):
            discount=input("PLease enter y if you have a 6E discount code or n if you dont:")
            if(discount!="n" and discount!="y"):
                print("Please enter a correct choice between y and n")
            else:
                modifier=True
        if(discount=="y"):
            discno=int(input("Please enter the discount code that you have:"))
            modifier=False
            while(modifier==False):
                d=discno
                ldisc=0
                while(d>0):
                    ldisc=ldisc+1
                    d=int(d/10)
                if(ldisc==12):
                    d=discno
                    discsum=0
                    while(d>0):
                        tedisc=d%10
                        d=int(d/10)
                        discsum=discsum+tedisc
                    if(discsum%11==0):
                        print("SUCCESS!! The code entered by you was applied for 15% discount")
                        modifer=True
                        break
                    else:
                        print("Please enter a correct code")
                        e=input("Please enter n if you dont want to enter the code:")
                        if(e=="n"):
                            modifier=True
                            discount="n"
                            break
                        else:
                            discno=int(input("Please enter the code:"))
                else:
                    print("Please enter a correct code")
                    e=input("Please enter n if you dont want to enter the code:")
                    if(e=="n"):
                        modifier=True
                        discount="n"
                        break
                    else:
                        discno=int(input("Please enter the code:"))
        flght=""
        modi=(random.randint(1,4))
        if(modi==1):
            cursor.execute("select * from flight1 order by srno")
            flght=cursor.fetchall()
        if(modi==2):
            cursor.execute("select * from flight2 order by srno")
            flght=cursor.fetchall()
        if(modi==3):
            cursor.execute("select * from flight3 order by srno")
            flght=cursor.fetchall()
        if(modi==4):
            cursor.execute("select * from flight4 order by srno")
            flght=cursor.fetchall()
        print("Sr No. Flight Timing Flight Name   Duration         Fare")
        for i in flght:
            for j in i:
                if(j==10):
                    print(j,end='     ')
                elif(j=="50m" or j=="55m"):
                    print(j,end='         ')
                elif(j=="1h" or j=="2h" or j=="3h"):
                    print(j,end='          ')
                elif(j=="2h 5m"):
                    print(j,end='       ')
                else:
                    print(j,end='      ')
            print()
        flightno=0
        modifier=False
        while(modifier==False):
            print("Please enter the serial number of the flight as per your preference")
            flightno=int(input("Please enter your response from as the number here(1-10):"))
            if(flightno==1 or flightno==2 or flightno==3 or flightno==4 or flightno==5 or flightno==6 or flightno==7 or flightno==8 or flightno==9 or flightno==10):
                print("Thank you for choosing this flight")
                modifier==True
                break
            else:
                print("Please enter a number from 1 to 10 corresponding to the flight of your choosing")
        flightno2=0
        modi2=modi
        if(onerou=="r" or onerou=="R"):
            while(modi==modi2):
                modi2=(random.randint(1,4))
            if(modi2==1):
                cursor.execute("select * from flight1 order by srno")
                flght=cursor.fetchall()
            if(modi2==2):
                cursor.execute("select * from flight2 order by srno")
                flght=cursor.fetchall()
            if(modi2==3):
                cursor.execute("select * from flight3 order by srno")
                flght=cursor.fetchall()
            if(modi2==4):
                cursor.execute("select * from flight4 order by srno")
                flght=cursor.fetchall()
            print("Sr No. Flight Timing Flight Name   Duration         Fare")
            for i in flght:
                for j in i:
                    if(j==10):
                        print(j,end='     ')
                    elif(j=="50m" or j=="55m"):
                        print(j,end='         ')
                    elif(j=="1h" or j=="2h" or j=="3h"):
                        print(j,end='          ')
                    elif(j=="2h 5m"):
                        print(j,end='       ')
                    else:
                        print(j,end='      ')
                print()
            print("Now please choose your round flight on",arrivedate)
            modifier=False
            while(modifier==False):
                print("Please enter the serial number of the flight as per your preference")
                flightno2=int(input("Please enter your response from as the number here(1-10):"))
                if(flightno2==1 or flightno2==2 or flightno2==3 or flightno2==4 or flightno2==5 or flightno2==6 or flightno2==7 or flightno2==8 or flightno2==9 or flightno2==10):
                    print("Thank you for choosing this flight")
                    modifier==True
                    break
                else:
                    print("Please enter a number from 1 to 10 corresponding to the flight of your choosing")
        print("\n"*10)
        print("************INDIGO AIRLINES TICKET******************")
        print("Name:",cuname)
        print("Phone Number:",cuphone)
        print("Passengers:",passenger)
        if(onerou=="R" or onerou=="r"):
            print("Flight type:Round")
        else:
            print("Flight type:Oneway")
        print("From:",departplace)
        print("To:",arriveplace)
        print("Departure date:",departdate)
        if(onerou=="R" or onerou=="r"):
            print("Departure date for round flight:",arrivedate)
        if(discount=="y"):
            print("Discount applied:15%")
        else:
            print("No discount code applied")
        d=""
        if(modi==1):
            cursor.execute("select * from flight1 where srno=%s" %(flightno))
            d=cursor.fetchall()
        elif(modi==2):
            cursor.execute("select * from flight2 where srno=%s" %(flightno))
            d=cursor.fetchall()
        elif(modi==3):
            cursor.execute("select * from flight3 where srno=%s" %(flightno))
            d=cursor.fetchall()
        else:
            cursor.execute("select * from flight4 where srno=%s" %(flightno))
            d=cursor.fetchall()
        totfar=0
        flttm=""
        fltnm=""
        fltdur=""
        fltnm2=""
        flttm2=""
        fltdur2=""
        for i in d:
            print("Flight timing:",i[1])
            print("Flight name:",i[2])
            print("Duration:",i[3])
            print("Fare:",i[4])
            totfar=totfar+int((i[4])[4:])
            flttm=i[1]
            fltnm=i[2]
            fltdur=i[3]        
        d2=""
        if(onerou=="R" or onerou=="r"):
            if(modi2==1):
                cursor.execute("select * from flight1 where srno=%s" %(flightno2))
                d2=cursor.fetchall()
            elif(modi2==2):
                cursor.execute("select * from flight2 where srno=%s" %(flightno2))
                d2=cursor.fetchall()
            elif(modi2==3):
                cursor.execute("select * from flight3 where srno=%s" %(flightno2))
                d2=cursor.fetchall()
            else:
                cursor.execute("select * from flight4 where srno=%s" %(flightno2))
                d2=cursor.fetchall()
            for i in d2:
                print("Flight timing for round flight:",i[1])
                print("Flight name for round flight:",i[2])
                print("Duration of round flight:",i[3])
                print("Fare:",i[4])
                totfar=totfar+int((i[4])[4:])
                flttm2=i[1]
                fltnm2=i[2]
                fltdur2=i[3]
                fltfr2=i[4]
        totfar=totfar*passenger
        if(discount=="y"):
            totfar=totfar-totfar*0.15
        print("Your total fare for the flight(s) is:INR",totfar,"(inclusive of all taxes and discount if applicable")
        print("\n"*10)
        modifier=False
        tktchk=""
        while(modifier==False):
            tktchk=input("Please enter y if you want to book these tickets or n if you want to cancel these tickets:")
            if(tktchk=="y" or tktchk=="n"):
                modifier=True
                break
        if(tktchk=="y"):
            if(onerou=="r" or onerou=="R"):
                cursor.execute("INSERT INTO customeround(name,phonenum,dest_place,dest_date,ret_place,ret_date,passengers,flight_name_dest,flight_name_ret,cost,disc)VALUES('{}',{},'{}','{}','{}','{}',{},'{}','{}',{},'{}')".format(cuname,cuphone,departplace,departdate,arriveplace,arrivedate,passenger,fltnm,fltnm2,totfar,discount))
                mycon.commit()
                print("Your tickets have been successfully booked")
            else:
                cursor.execute("INSERT INTO customeroneway(name,phonenum,dest_place,dest_date,passengers,Flight_Name,cost,disc)VALUES('{}',{},'{}','{}',{},'{}',{},'{}')".format(cuname,cuphone,departplace,departdate,passenger,fltnm,totfar,discount))
                mycon.commit()
                print("Your tickets have been successfully booked")
        print("***************THANK YOU FOR TRYING INDIGO AIRLINES***************")
    if(chfirst==2):
        print("**********WELCOME EXISTING INDIGO USER****************")
        cuname=input("Please enter your name:")
        modifier=False
        while(modifier==False):
            cuphone=int(input("Please enter your 10 digit phone number:"))
            cuphone=str(cuphone)
            l=len(cuphone)
            if(l!=10):
                print("Please enter a valid ten digit phone number")
            else:
                cuphone=int(cuphone)
                modifier=True
        modifier=False
        onerou=""
        temp=(cuname,cuphone)
        while(modifier==False):
            onerou=input("Please enter r if you booked a round flight or o if you booked a oneway flight:")
            if(onerou=="o" or onerou=="r"):
                modifier=True
        d=""
        stat=""
        if(onerou=="o"):
            stat="select * from customeroneway where name=%s and phonenum=%s"
        else:
            stat="select * from customeround where name=%s and phonenum=%s"
        cursor.execute(stat,temp)
        d=cursor.fetchall()
        desti=''
        dest_datei=''
        passeni=0
        fltnmi=""
        costi=0
        disci=""
        fltnmi2=""
        reti=""
        duri=""
        dur2i=""
        ret_datei=""
        if(d==[]):
            print("*********Please check your details.The information you have entered is not saved by us*************")
            print("\n"*5)
        else:
            if(onerou=="o"):
                for i in d:
                    desti=i[2]
                    dest_datei=i[3]
                    passeni=i[4]
                    fltnmi=i[5]
                    costi=i[6]
                    disci=i[7]
            else:
                for i in d:
                    desti=i[2]
                    dest_datei=i[3]
                    reti=i[4]
                    ret_datei=i[5]
                    passeni=i[6]
                    fltnmi=i[7]
                    fltnm2i=i[8]
                    costi=i[9]
                    disci=i[10]
            print("\n"*10)
            print("*************USER DETAILS************")
            print("Name:",cuname)
            print("Phone Number:",cuphone)
            if(onerou=="o"):
                print("Flight Type:Oneway")
            else:
                print("Flight Type:Round")
            if(disci=="y"):
                print("Discount Applied")
            modifier=False
            fltdet=""
            cursor.execute("select * from flight1 where flight_name='%s'" %(fltnmi))
            fltdet=cursor.fetchall()
            if(fltdet==[]):
                cursor.execute("select * from flight2 where flight_name='%s'" %(fltnmi))
                fltdet=cursor.fetchall()
            if(fltdet==[]):
                cursor.execute("select * from flight3 where flight_name='%s'" %(fltnmi))
                fltdet=cursor.fetchall()
            if(fltdet==[]):
                cursor.execute("select * from flight4 where flight_name='%s'" %(fltnmi))
                fltdet=cursor.fetchall()
            fltdet2=""
            if(onerou=="r"):
                cursor.execute("select * from flight1 where flight_name='%s'" %(fltnm2i))
                fltdet2=cursor.fetchall()
                if(fltdet2==[]):
                    cursor.execute("select * from flight2 where flight_name='%s'" %(fltnm2i))
                    fltdet2=cursor.fetchall()
                if(fltdet2==[]):
                    cursor.execute("select * from flight3 where flight_name='%s'" %(fltnm2i))
                    fltdet2=cursor.fetchall()
                if(fltdet2==[]):
                    cursor.execute("select * from flight4 where flight_name='%s'" %(fltnm2i))
                    fltdet2=cursor.fetchall()
            for i in fltdet:
                duri=i[1]
            for i in fltdet2:
                dur2i=i[1]
            print("Flight Name:",fltnmi)
            print("Flight Timing:",duri)
            print("Destination:",desti)
            print("Date of departure:",dest_datei)
            if(onerou=="r"):
                print("Flight Name for return flight:",fltnm2i)
                print("Flight timing for return flight:",dur2i)
                print("Place of return:",reti)
                print("Date of return",ret_datei)
            print("Passengers:",passeni)
            print("Total Fare:",costi)
            print("\n"*5)
            print("********************IF YOU WISH TO CANCEL YOUR TICKETS PLEASE ENTER n OTHERWISE CONTINUE WITH ANY LETTER****************")
            canchk=input("Enter your response here:")
            if(canchk=="n"):
                if(onerou=="o"):
                    cursor.execute("delete from customeroneway where name='%s' and phonenum=%s" %(cuname,cuphone))
                    mycon.commit()
                else:
                    cursor.execute("delete from customeround where name='%s' and phonenum=%s" %(cuname,cuphone))
                    mycon.commit()
                print("*********TICKET CANCELLED SUCCESSFULLY************")
                print("WE HOPE YOU BOOK TICKETS WITH US IN THE FUTURE")
        print("************THANK YOU FOR TRYING INDIGO ONLINE SERVICE***************")
    if(chfirst==3):
        print("*************WELCOME MANAGER**************")
        usnm=input("Please enter username:")
        passw=input("Please enter password to verify yourself:")
        check="select * from manager where user=%s and password=%s"
        inp=(usnm,passw)
        cursor.execute(check,inp)
        chk=cursor.fetchall()
        if(chk==[]):
            print("*****Please enter valid details and login again or exit if you are not an authorised user*****")
            print("\n"*5)
        else:
            yesno="y"
            print("WELCOME ADMIN")
            while(yesno=="y"):
                onerou=input("Please enter o to check oneway details or r to check round details:")
                modifier=False
                while(modifier==False):
                    if(onerou=="o" or onerou=="r"):
                        modifier=True
                        break
                    else:
                        onerou=input("Please enter o(ONEWAY) or r(ROUND):")
                if(onerou=="r"):
                    cursor.execute("select * from customeround ")
                else:
                    cursor.execute("select * from customeroneway")
                d=cursor.fetchall()
                if(d==[]):
                    print("There are no records found in this category please try again later")
                else:
                    for i in d:
                        print(i)
                    l=len(d)
                    print("*************************************")
                    print("Please enter 1 to delete a record")
                    print("Please enter 2 to update the EDITABLE DETAILS(NAME AND/OR PHONE NUMBER)")
                    print("Please enter 3 to check the status of flights")
                    print("Enter n to go back")
                    che=input("Pease enter your response here:")
                    modifier=False
                    while(modifier==False):
                        if(che!="1" and che!="2" and che!="3" and che!="n"):
                            che=input("Please enter correct choice or n to go back")
                            if(che=="n"):
                                modifier=True
                                break
                        else:
                            modifier=True
                            break
                    if(che=="1"):
                        delrec=int(input("Please enter the serial number/record number of the record you want to delete:"))
                        while(delrec>l or delrec<=0):
                            delrec=int(input("Please enter a correct record number:"))
                        temp=d[delrec-1]
                        nm=""
                        nm=i[0]
                        delerecor=(nm)
                        dle=""
                        if(onerou=="o"):
                            cursor.execute("delete from customeroneway where name='%s'" %(delerecor))
                            mycon.commit()
                        else:
                            cursor.execute("delete from customeround where name='%s'" %(delerecor))
                            mycon.commit()
                        print("********************Record Successfully Deleted***********************")
                        print("\n"*10)
                    if(che=="2"):
                        uprec=int(input("Please enter the serial number/record number of the record you want to update"))
                        while(uprec>l or uprec<0):
                            uprec=int(input("Please enter correct record number"))
                        upchk="y"
                        nm=""
                        phn=0
                        dc=""
                        while(upchk=="y"):
                            temp=d[uprec-1]
                            mo=""
                            mo=temp[0]
                            print("Please enter 1 to update the name of the user")
                            print("Please enter 2 to update the phone number of the user")
                            print("Please enter 3 to go back")
                            uprecord=int(input("Enter your response here"))
                            while(uprecord!=1 and uprecord !=2 and uprecord !=3):
                                uprecord=int(input("Please enter correct number"))
                            if(uprecord==1):
                                nm=input("Please enter the new name here:")
                                if(onerou=="o"):
                                    cursor.execute("update customeroneway set name='{}' where name='{}'".format(nm,mo))
                                    mycon.commit()
                                else:
                                    cursor.execute("update customeround set name='{}' where name='{}'".format(nm,mo))
                                    mycon.commit()
                                print("Name updated successfully")
                            if(uprecord==2):
                                phn=int(input("Please enter new 10digit phone number"))
                                while(len(str(phn))!=10):
                                    phn=int(input("Please enter correct 10 digit phone number"))
                                phn=int(phn)
                                if(onerou=="o"):
                                    cursor.execute("update customeroneway set phonenum={} where name='{}'".format(phn,mo))
                                    mycon.commit()
                                else:
                                    cursor.execute("update customeround set phonenum={} where name='{}'".format(phn,mo))
                                    mycon.commit()
                                print("Phone number updated successfully")
                            if(uprecord==3):
                                upchk=="n"
                                break
                    if(che=="3"):
                        c=random.randint(0,100)
                        if(c<40):
                            f=10
                            while(f%10==0):
                                f=random.randint(1000,9999)
                            print("Flight Number 6E",f,end='')
                            g=random.randint(0,3)
                            if(g==0):
                                print(" is currently off schedule.")
                            if(g==1):
                                print(" is under a technical issue")
                            if(g==2):
                                print(" is undergoing repairs")
                            if(g==3):
                                print(" is undergoing maintenance")
                        else:
                            print("No issues detected in any flight")
                yesno=input("Please enter y to continue editing the details or n to exit:")
                while(yesno!="y" and yesno!="n"):
                    yesno=input("Please enter a correct option:")
                print("\n"*5)
    if(chfirst==4):
        mod=mod+1
        print("*******PLEASE VISIT OUR SITE AGAIN*********")
        print("*******THANK YOU FOR VISITING OUR SITE********")
mycon.close()
