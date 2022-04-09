while True:
    start=input("press start to continue")
    if(start=="start"):

        
            import datetime
            d=datetime= datetime.datetime.now()
            d=str(d)
            print("\t\t\t welcome to roshan's library")

            name=input("write your name-->")
            clas=input("write your class-->")
            roll=input("write your roll number-->")
            book=input("write the book name-->")

            f=open("library.txt","a")
            a=f.write("\nname= "+name)

            f=open("library.txt","a")
            a=f.write("\nclass= "+clas)

            f=open("library.txt","a")
            a=f.write("\nroll number= "+roll)

            f=open("library.txt","a")
            a=f.write("\nbook= "+book)

            f=open("library.txt","a")
            a=f.write("\ndate and time "+d)

            f=open("library.txt","a")
            a=f.write("\n---------------------------------------------------------------------------------------")

            conform=input("press y to save it")

            if(conform=="y"):
                print("you have successfully saved ")
                print("----------------------------------------------------")
    else:
        print("closing the program")
        exit()