
with open('doctors_aid.inputs .txt','r') as rf:#open and read input files
   
    with open ('doctors_aid.outputs1.txt','w') as wf:#open the output files for writing
       
        
          
        def table():
                header=["Patient Name","Diagnosis Accuracy", "Disease Name","Disease Incidence","Treatment Name","Treatment Risk"]  
                with open('doctors_aid.inputs .txt','r') as rf:#open and read input files
                    
                        i=0
                        n=6
                        while n>0:
                         
                            wf.write(header[i].ljust(20," "))#write the items in header to output file by puting 20 spaces betveen every item.
                            i+=1 
                            n-=1
                        wf.write("\n")  
                        for line in rf:
                            line_name= line.split(",")
                            
                            if len(line_name)>5:
                                get_name=line_name[0].split(" ")#
                                
                                name=get_name[1] 
                                line_name[0]=name

                                i=0
                                while i<6:
                                    wf.write(line_name[i].ljust(20,' '))
                                    i+=1
    
        for line in rf:#ı create a loop for reading text file line by line.
            line_name= line.split(",")#seperate the items where comma iis used.
           

            if len(line_name)>5:#ı create this condition to achive the lines which start with create
                
                get_name=line_name[0].split(" ")#
                name=get_name[1]                # ı used this assigment to call names in lines. 
                diseasename=line_name[2]
                
           
                   
            
                    
            def probability():
                    with open('doctors_aid.inputs .txt','r') as rf:    
                     for line in rf:
                        line_name= line.split(",")
                        if len(line_name)>5:

                           
                            accuracy=(line_name[1])
                            accuracy=round(float(accuracy.strip('%')),4)
                            incidence_list=line_name[3]
                 
                            value_incidence=incidence_list.split("/")
                            X=float(value_incidence[0])/float(value_incidence[1])
                            a=round(1-(accuracy/100),4) 
                            sum= a + float(X)
                            prob=float(X)/sum
                            if float(prob*100)==int(prob*100):
                                prob="{: .0%}".format(float(prob))
                            else:
                                prob="{: .2%}".format(float(prob))
                            global prob_value
                            prob_value=prob.strip('%')    
                            wf.write("patient %s has a probability of %s of having %s .\n"%(name,(prob),diseasename))
                            return get_order
                            
                   
                    
                   
            
            get_order=line_name[0].split(" ")#İt is for understanding commands in lines.
            
           
            if get_order[0]=='create':                     #
                wf.write("Patient %s is recorded.\n"%(name))# 
                                                           #
                                                           #
            if get_order[0]=='remove':                     #this conditions understands the command and call the functions or directly write a sentences to output file.
                
                wf.write("Patient %s is removed.\n"%(name))#
                                                           # 
            if get_order[0]=='probability':                # 
                 probability() 
                                                           # 
            if get_order[0]=='list\n':
                table()


            
        
    
        
   
                    
            
            

                
            
            
            
              
            
                
      

