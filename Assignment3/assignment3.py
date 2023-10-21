import sys
input= sys.argv[1]

with open(input,'r') as rf:
    with open ('output.txt','w') as wf:
        category_list=[]
        soldcategories=[]#it is include seperate list for every category.Each category list include seats and customer type information.        
        rows={}
        colums={}
        for line in rf:           
            content=line.split(" ")
            command=content[0]
            
            if command=='CREATECATEGORY':
                categoryname=content[1]
                char=content[2].split("x")
                row=char[0]
                if int(row)>26:
                    wf.write("Error: row can not be greater than 26./n")
                    print("Error: row can not be greater than 26./n")
                colum=char[1]
                capacity= int(row)*int(colum)                
                if  categoryname in category_list:
                    wf.write("Warning:   Cannot create the category for the second time. The stadium has already %s.\n"%( categoryname))
                    print("Warning:   Cannot create the category for the second time. The stadium has already %s.\n"%( categoryname))
                else:
                    wf.write("The category '%s' having %d seats has been created.\n"%( categoryname,capacity))
                    print("The category '%s' having %d seats has been created.\n"%( categoryname,capacity))
                    category_list.append(categoryname)
                    rows[categoryname]=row#adds all the rows to the 'rows' dictionary for using on  checking
                    colums[categoryname]=colum#adds all the colums to the 'colums' dictionary for using on checking              
                        
            if command=='SELLTICKET':
                customername=content[1]
                customertype=content[2]
                categorynames=content[3]                
                i=4
                
                for items in content[4:]:
                    if "\n" in items:
                        items=items.replace("\n", "")
                    bool=True #ı used this for checking whether values enter error conditions or not.                                           
                    small=[]
                    if len(items)<4:                        
                        c=colums[categorynames]
                        r=rows[categorynames]
                        num=items
                        num=num.lstrip(num[0])#deletes the char in front of the seat number.
                        small.append(items)
                        small.append(customertype) #I append customer type for make counting easier for balance command.
                                                                
                        if int(num) in range(0,int(c)):#checks column length
                            pass
                        else:
                            wf.write("Error:    The category '%s' has less column than the specified index %s!\n"%(categorynames,items))
                            print("Error:    The category '%s' has less column than the specified index %s!\n"%(categorynames,items))
                            bool=False 
                        if ord(items[0]) in (range(65,int(r)+65)):#checks row length
                            pass
                        else:
                            wf.write("Error:    The category '%s' has less row than the specified index %s!\n"%(categorynames,items))
                            print("Error:    The category '%s' has less row than the specified index %s!\n"%(categorynames,items))
                            bool=False                                                 
                        if bool==True:#if value entered error condition before it prevent to enter next error condition.
                            p=0
                            for element in soldcategories:                                               
                                if items in soldcategories[p]:
                                        wf.write("Error:    The seats %s cannot be sold to %s due some of them have already been sold!\n"%(outnum,customername))
                                        print("Error:    The seats %s cannot be sold to %s due some of them have already been sold!\n"%(outnum,customername))
                                        break                                                                           
                                p+=1                     
                    elif len(items)>=4:#it is for ranges.
                        outnum=items
                        number=items
                        number=number.lstrip(number[0])
                        number=number.split("-")
                        a=int(number[0])
                        b=int(number[1]) 
                        bool=True
                        c=colums[categorynames]
                        r=rows[categorynames]

                        if b in range(0,int(c)):#checks column length
                            pass
                        else:
                            wf.write("Error:    The category '%s' has less column than the specified index %s!\n"%(categorynames,items))
                            print("Error:    The category '%s' has less column than the specified index %s!\n"%(categorynames,items))
                            outnum=[]
                            bool=False 
                        if ord(items[0]) in (range(65,int(r)+65)):#checks row length.With ord() I called Ascıı values of char.
                            pass
                        else:
                            wf.write("Error:    The category '%s' has less row than the specified index %s!\n"%(categorynames,items))
                            print("Error:    The category '%s' has less row than the specified index %s!\n"%(categorynames,items))
                            outnum=[]
                            bool=False 
                        
                        rangelist=[]
                        for integers in range(a,b+1):#it is for accessing the seat number in  ranges 
                            number=items
                            index=number[0]+str(integers)
                            p=0
                            y=True
                            for element in soldcategories:
                                if bool==True:                                               
                                    if index  in soldcategories[p]:
                                        wf.write("Error:    The seats %s cannot be sold to %s due some of them have already been sold!\n"%(outnum,customername))
                                        print("Error:    The seats %s cannot be sold to %s due some of them have already been sold!\n"%(outnum,customername))
                                        y=False
                                        break#if one value was sold ,it prevent continue to check other range element.
                                    p+=1
                            if bool==False or y==False:#if value enter any error condition, loop stop.
                                break   
                            else:
                                rangelist.append(index)
                                rangelist.append(customertype)                            
                        items=rangelist
                                                                     
                    if soldcategories!=[]:
                            if "\n" in items:
                                items=items.replace("\n", "")
                                                                                       
                            j=0    
                            for elements in category_list:
                                if category_list[j]==categorynames:
                                    if soldcategories!=[]:
                                        x=True
                                        n=0
                                        for element in soldcategories:
                                            if categorynames in soldcategories[n]:#it append items to related list in soldcategories.    
                                                    x=False
                                                    if len(items)<4:
                                                        soldcategories[n]+=small
                                                    else:
                                                        soldcategories[n]+=items                                                                                                          
                                                    n+=1             
                                                    break
                                            n+=1                        
                                        if x==True:#After scaning whole soldcategories and still categorynames is not in soldcategories,it creates a new list in soldcategories and append items.
                                            soldcategories.append([categorynames])
                                            for cats in soldcategories:
                                                if categorynames in cats:
                                                    if len(items)<4:
                                                        cats+=small
                                                    else:
                                                        cats+=items                                                                                                
                                j+=1                                                        
                    else:#if soldcategories is empty-list it append.İt is for initial situation.                          
                        soldcategories.append([categorynames])                        
                        if small!=[]:
                            soldcategories[0]+=small                                                        
                        if len(items)>=4:
                            soldcategories[0]+=items 
                    if items!=[]:
                                if len(items)<4:                                    
                                    wf.write("Success:  %s has bought %s at %s.\n"%(customername,items,categorynames))
                                    print("Success:  %s has bought %s at %s.\n"%(customername,items,categorynames))
                                elif len(items)>=4 and outnum!=[]:#outnum is used for checking whether value entered error condition or not.
                                    wf.write("Success:  %s has bought %s at %s.\n"%(customername,outnum,categorynames))
                                    print("Success:  %s has bought %s at %s.\n"%(customername,outnum,categorynames))                                              
                    i+=1

            if command=='CANCELTICKET':
                category_name=content[1] 
                for cancels in content[2:]:
                    if "\n" in cancels:
                        cancels=cancels.replace("\n", "")
                    seatnum=cancels
                    seatnum=seatnum.lstrip(seatnum[0])
                    if int(seatnum)>int(row):
                        wf.write("Error: The category '%s' has less column than the specified index %s!\n"%(category_name,cancels))
                        print("Error: The category '%s' has less column than the specified index %s!\n"%(category_name,cancels))
                        break
                    for sells in soldcategories[:]:
                        if category_name in sells:
                            if cancels in sells:
                                wf.write("Success:  The seat %s at '%s' has been canceled and now ready to sell again.\n"%(cancels,category_name))
                                print("Success:  The seat %s at '%s' has been canceled and now ready to sell again.\n"%(cancels,category_name))
                                break                                
                            else:
                                wf.write("Error: The seat %s at '%s' has already been free! Nothing to cancel.\n"%(cancels,category_name))
                                print("Error: The seat %s at '%s' has already been free! Nothing to cancel.\n"%(cancels,category_name))
                                break    
                                                                
            if command=='BALANCE':
                if "\n" in content[1]:
                    content[1]=content[1].replace("\n", "")
                categorname=content[1]    
                for types in soldcategories:                    
                  if categorname==types[0]:
                        student=types.count('student')
                        full=types.count('full')
                        season=types.count('season')
                        price=(int(student)*10)+(int(full)*20)+(int(season)*250)
                        
                        str="Category report of '%s'\n"%(categorname)
                        wf.write("Category report of '%s'\n"%(categorname))
                        print("Category report of '%s'"%(categorname))

                        i=len(str)
                        while i>1:
                            wf.write("-")
                            print("-",end='') 
                            i-=1
                        wf.write("\nSum of students = %s, Sum of full pay = %s, Sum of season ticket=%s,and Revenues = %s Dollars.\n"%(student,full,season,price))
                        print("\nSum of students = %s, Sum of full pay = %s, Sum of season ticket=%s,and Revenues = %s Dollars.\n"%(student,full,season,price))

            if command=='SHOWCATEGORY':
                if "\n" in content[1]:
                    content[1]=content[1].replace("\n", "")
                showcat=content[1]
                b=rows[showcat]
                u=colums[showcat]
                m=0
                for types in soldcategories:                
                    if showcat==types[0]:
                        print("\n")
                        wf.write("\n")
                        print("Printing category layout of %s"%(showcat))
                        wf.write("Printing category layout of %s"%(showcat))    
                        
                        for i in reversed(range(65,int(b)+65)):
                                print("\n",chr(i), end=" ")
                                wf.write("\n")#it is for design.
                                wf.write(chr(i))

                                for integer in range(0,int(u)):
                                    find=chr(i)+("%d"%(integer))                                      
                                    z=True
                                    it=iter(types[1:])#types[0] is categoryname. 

                                    for x, y in zip(it,it):#in soldcategories items order is fixed as "seatnumber ,customer type",so this loop call 2 item.
                                        if find == x:
                                            z=False
                                            if y=='student':
                                                print("  S",end=" ")
                                                wf.write("  S")                                                
                                            if y=='full':
                                                print("  F",end=" ")
                                                wf.write("  F")                                                 
                                            if y=='season':
                                                print("  T",end=" ")
                                                wf.write("  T")                                                
                                    if z==True:
                                        print("  X",end=" ")
                                        wf.write("  X")

                        print("\n","  ",end="")#it is for design
                        wf.write("\n")#it is for design
                        [print("  %d"%(l), end = ' ') for l in range(10)]
                        [print(" %d"%(l), end = ' ') for l in range(10,int(u))]

                        wf.write(" ")  
                        [wf.write("  %d"%(l)) for l in range(10)]
                        [wf.write(" %d"%(l)) for l in range(10,int(u))]
                        print(" ")#it is for design
                        wf.write("\n") #it is for design 
                
wf.close()   
rf.close()               
                         
                



                
                




