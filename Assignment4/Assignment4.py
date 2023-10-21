import sys
shoots1=[]
shoots2=[]#contains total size of player1's sunked ships (which equals =5*1+4*2+3*1+3*1+4*2=27)                 
try:
 with open(sys.argv[1],'r') as p1:
  try:
    with open(sys.argv[2],'r') as p2:
      grid1=[]
      grid2=[]
      movement1=[]
      movement2=[]
      sunk1=[] 
      sunk2=[]             
      def read_input(file,list):
                try:
                    for line in file:
                        content=line.split(";")  
                        content[-1]=content[-1].rstrip()
                        if '\n' in content:
                            content.remove('\n') 
                        n=0   
                        for value in content:
                            if value== '':
                                content[n]=content[n].replace('',"-")   
                            elif value in ["B","C","D","S","P"]:
                                pass
                            else:
                                raise IndexError    
                            n+=1        
                        list.append(content)
                except IndexError:
                    with open("battleships.out",'a') as out:
                      out.write("IndexError:You enter invalid value.You should enter a correct ship type e.g 'C,B,D,S,P'\n")
                      out.close()
      read_input(p1,grid1)#read p1 and append content of p1 to grid1
      read_input(p2,grid2)#read p2 and append content of p2 to grid2 
  except IOError:
    with open("battleship.out",'a') as out:
        out.write("IOError:input file %s is not reachable.\n"%(sys.argv[2]))
        out.close() 
except IOError:
  with open("battleship.out",'a') as out:
    out.write("IOError:input file %s is not reachable.\n"%(sys.argv[1]))
    out.close()         
try:          
  with open(sys.argv[3],'r') as lunge1: 
    try:
      with open(sys.argv[4],'r') as lunge2:
                    movement1=lunge1.readline()
                    movement1=movement1.split(";")
                    movement2=lunge2.readline()
                    movement2=movement2.split(";")
                     
                    def prompt(player,round,rw,cl,move,sunk1,sunk2):
                      with open("battleship.out",'a') as out:  
                        print("\n%s's Move:\n"%(player))
                        print("Round:",round+1,"\t\t\t\t\tGrid size: 10X10\n")
                        out.write("\n%s's Move:\n\n"%(player))
                        out.write("Round:%d\t\t\t\tGrid size: 10X10\n\n"%(round+1))
                        print("player1's Hidden Board\t\t\t\tplayer2's Hidden Board")
                        print("  ",end="")
                        out.write("player's Hidden Board\t\tplayer2's Hidden Board\n")
                        [print(" ",chr(x),end="") for x in range(65,75)]
                        print("\t\t  ",end="")
                        [print(" ",chr(x),end="") for x in range(65,75)]
                        out.write(" ")
                        [out.write(" %s"%(chr(x))) for x in range(65,75)]
                        out.write("\t\t ")
                        [out.write(" %s"%(chr(x))) for x in range(65,75)]
                        for row in range(1,len(grid1)+1):
                          print("\n",row,end=" ")
                          out.write("\n%d"%(row)) 
                          for col in range(len(grid1[row-1])):#printing player1's line
                            if  player=="player2" and row==(rw) and col==(ord(cl)-65)  :                           
                                if grid1[row-1][col]=='-':
                                  print(" O",end=" ")
                                  out.write(" O")
                                else:                                                                                                           
                                  print(" X",end=" ")
                                  out.write(" X")
                            elif grid1[row-1][col]=='O':                               
                                print(" O",end=" ")
                                out.write(" O")
                            elif grid1[row-1][col]=='X':                              
                                print(" X",end=" ") 
                                out.write(" X")                              
                            else:                              
                                print(" -",end=" ") 
                                out.write(" -")                                               
                          print("\t\t",row,end=" ")
                          out.write("\t\t%d"%(row))
                          for col in range(len(grid2[row-1])):#prompt player2's line                                                                                                                                              
                            if  player=="player1" and row==(rw) and col==(ord(cl)-65) :                             
                                if grid2[row-1][col]=='-':                                          
                                  print(" O",end=" ")
                                  out.write(" O")
                                else:                                                  
                                  print(" X",end=" ")
                                  out.write(" X")
                            elif grid2[row-1][col]=='O':                               
                                print(" O",end=" ")
                                out.write(" O")
                            elif grid2[row-1][col]=='X':                              
                                print(" X",end=" ") 
                                out.write(" X")                              
                            else:                              
                                print(" -",end=" ") 
                                out.write(" -")                        
                        carrier1=shoots1.count("C")
                        carrier2=shoots2.count("C")
                        if carrier1==5 :
                          print("\ncarrier \tX",end="")
                          out.write("\ncarrier \tX")
                        else:
                          print("\ncarrier\t\t-",end="")
                          out.write("\ncarrier \t-")
                        if carrier2==5:
                          print("\t\t\t\tcarier\t\tX")  
                          out.write("\t\t\tcarrier\t\t  X\n")  
                        else:
                          print("\t\t\t\tcarrier\t\t-")
                          out.write("\t\t\tcarrier\t-\n")
                        battleship1=shoots1.count("B")                      
                        battleship2=shoots2.count("B")
                        if battleship1>4 and battleship1<8:
                          print("Battleship	  X -",end="")
                          out.write("Battleship	  X -")
                        elif battleship1==8:
                          print("Battleship	   X X",end="")
                          out.write("Battleship    X X")
                        else:
                          print("Battleship    - -",end="")                
                          out.write("Battleship  - -")                
                        if battleship2>4 and battleship2<8:
                          print("\t\t\t\tBattleship	    X -")
                          out.write("\t\t\tBattleship  X -\n")
                        elif battleship2==8:
                          print("\t\t\tBattleship	X X")
                          out.write("\t\tBattleship  X X\n")
                        else:
                          print("\t\t\t\tBattleship	- -")                
                          out.write("\t\t\tBattleship - -\n")     
                        Destroyer1=shoots1.count("D") 
                        Destroyer2=shoots2.count("D")
                        if Destroyer1==3:
                           print("Destroyer	X",end="")
                           out.write("Destroyer	X")
                        else:
                          print("Destroyer	-",end="")
                          out.write("Destroyer	-")
                        if Destroyer2==3:
                           print("\t\t\t\tDestroyer	X")
                           out.write("\t\t\tDestroyer	X\n")
                        else:
                          print("\t\t\t\tDestroyer	-")
                          out.write("\t\t\tDestroyer	-\n")
                        submarıne1=shoots1.count("S")
                        submarıne2=shoots2.count("S")
                        if submarıne1==3:
                          print("Submarine	X",end="")
                          out.write("Submarine	X")
                        else:
                            print("Submarine	-",end="")
                            out.write("Submarine	-")
                        if submarıne2==3:
                          print("\t\t\t\tSubmarine	X")
                          out.write("\t\t\tSubmarine	X\n")
                        else:
                            print("\t\t\t\tSubmarine	-")
                            out.write("\t\t\tSubmarine	-\n")                                   
                        p=sunk1.count("P")
                        if p ==2:
                          print("Patroal Boat    X - - - ",end="")
                          out.write("Patroal Boat    X - - - ")
                        elif p==4:
                          print("Patroal Boat    X X - - ",end="")
                          out.write("Patroal Boat    X X - - ")
                        elif p==6:
                          print("Patroal Boat    X X X - ",end="")
                          out.write("Patroal Boat    X X X - ")
                        elif p==8:
                          print("Patroal Boat    X X X X ",end="")    
                          out.write("Patroal Boat    X X X X ")
                        else:  
                          print("Patroal Boat    - - - - ",end="")
                          out.write("Patroal Boat - - - - ")
                        P=sunk2.count("P")
                        if p ==2:
                          print("\t\t\tPatroal Boat    X - - - ")
                          out.write("\t\tPatroal Boat X - - - \n")
                        elif p==4:
                          print("\t\t\tPatroal Boat    X X - - ")
                          out.write("\t\tPatroal Boat X X - - \n")
                        elif p==6:
                          print("\t\t\tPatroal Boat    X X X - ")
                          out.write("\t\tPatroal Boat X X X - \n")
                        elif p==8:
                          print("\t\t\tPatroal Boat    X X X X ")    
                          out.write("\t\tPatroal Boat X X X X \n") 
                        else:
                          print("\t\t\tPatroal Boat    - - - - ")
                          out.write("\t\tPatroal Boat - - - - \n")     
                        print("\nEnter your move: %s"%(move))                                 
                        out.write("\nEnter your move: %s\n"%(move))  
                        out.close()                               
                    def move1(round,player):
          
                        try:
                            for row in range(1,len(grid2)+1): 
                                index=movement1[round]
                                if len(index)<3:
                                  raise IndexError                            
                                index=index.split(",")    
                                try:                                                
                                  rw=int(index[0]) 
                                except ValueError:
                                  out.write("Value Error: Your moves has not valid row number.Please enter a row number between  1-10.")
                                  out.close()
                                  pass
                                try:
                                  cl= index[1]
                                except ValueError:
                                  out.write("Value Error: Your moves has not valid column.Please enter a column  between  A-J.")
                                  out.close()
                                  pass   
                                if player=="player1"  and row==1:# to condition do not repeat itself row is assigned to 1.
                                    
                                  prompt(player,round,rw,cl,movement1[round],sunk1,sunk2) 
                                                                                                                        
                                if player=="player1" :                                       
                                  for col in range(len(grid2[row-1])):#prompt player2's line
                                        if ord(cl) in range(65,76) and int(rw) in range(11):                                                                                   
                                            if row==rw and col==(ord(cl)-65) :
                                                if grid2[row-1][col]=='-':                                                                                            
                                                  grid2[row-1][col]=grid2[row-1][col].replace('-','O')    
                                                else:                                                                                                 
                                                  w=grid2[row-1][col]
                                                  try:
                                                    w2=grid2[row-1][col+1]#check left side
                                                    w3=grid2[row][col]#check downward
                                                    if w=="P"and w==w2 and w2==w3:#if there is another "P" on leftward or d0wnward petroal boat sunked.
                                                      sunk2.append("P")
                                                  except IndexError:
                                                      pass
                                                  grid2[row-1][col]=grid2[row-1][col].replace(w,'X')
                                                  if player=='player1':
                                                    shoots2.append(w)                                                                                                                                           
                                        else:
                                            raise AssertionError        
                            for row in range(1,len(grid1)+1):                              
                              index=movement2[round]
                              index=index.split(",")                              
                              try:                                                
                                rw=int(index[0]) 
                              except ValueError:
                                out.write("Value Error: Your moves has not valid row number.Please enter a row number between  1-10.")
                                out.close()
                                pass
                              try:
                                cl= index[1]
                              except ValueError:
                                out.write("Value Error: Your moves has not valid column.Please enter a column  between  A-J.")
                                out.close()
                                pass
                              if player=="player2" and row==1:
                                prompt(player,round,rw,cl,movement2[round],sunk1,sunk2)                           
                              if player=="player2" :                                                           
                                for col in range(len(grid1[row-1])):#prompt player1's line 
                                  if ord(cl) in range(65,76) and int(rw) in range(11) :                                                                                                                              
                                      if row==rw and col==(ord(cl)-65)  :
                                          if grid1[row-1][col]=='-':                                                      
                                            grid1[row-1][col]=grid1[row-1][col].replace('-','O')    
                                          else:                                                                                                                                                                  
                                            w=grid1[row-1][col]
                                            try:                                            
                                              w2=grid1[row-1][col+1]#check rightward
                                              w3=grid1[row][col]#check downward                                              
                                              if(w=="P"and w2=="P"):#if there is another "P" on rightward 
                                                  sunk2.append("P")
                                              elif(w=="P"and  w3=="P"):#if there is another d0wnward ,petroal boat sunked.
                                                sunk2.append("P")
                                            except IndexError:
                                              pass
                                            grid1[row-1][col]=grid1[row-1][col].replace(w,'X')
                                            if player=='player2':
                                                shoots1.append(w)
                                  else:
                                      raise AssertionError  
                                                                                                    
                        except IndexError:
                          out.write("Index Error: Your move is unfinished.Please enter a valid row and column.")
                          out.close()
                          pass
                        except AssertionError:
                            out.write(" AssertionError: Invalid Operation.")
                            out.close()
                            pass                                  
                    with open("battleship.out",'a') as out:                 
                        out.write("Battle of Ships Game\n\n")
                        print("Battle of Ships Game\n")
                        round=0
                    while len(shoots1)<27:#contains total size of ships (which equals =5*1+4*2+3*1+3*1+4*2=27)                            
                              move1(round,"player1")
                              move1(round,"player2")                        
                              if len(shoots1)==27:
                                with open("battleship.out",'a') as out:   
                                  out.write("Player2 wins!") 
                                  break
                              elif len(shoots2)==27:
                                with open("battleship.out",'a') as out:   
                                 out.write("Player1 wins!") 
                                break
                              round+=1
    except IOError:
      with open("battleship.out",'a') as out:
        out.write("IOError:input file %s is not reachable.\n"%(sys.argv[4]))
        out.close()                           
except IOError:
  with open("battleship.out",'a') as out:
        out.write("IOError:input file %s is not reachable.\n"%(sys.argv[3])) 
        out.close()   
