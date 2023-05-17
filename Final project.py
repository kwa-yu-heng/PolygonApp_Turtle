#Kwa Yu Heng MA9
#add keyboard shortcuts to analytics as code is built
import turtle
import math

t = turtle
s = turtle.Screen()
p = []   # single polygon, initialise
poly_list=[] #list of polygons
t.speed(0) #no time delay when drawing
option=0 #initialise option

#set len>3
#iterate to len(p)-2
#calculate s and t; s+r() --> dir x1-x2 y1-y2
#2 vectors
#a=ct=e+sg
#b+dt=f+sh
#equate 2 vectors
#find t and s
#e.g. 1+3t = 6+8s
#2 eqns; top and bottom
#catch zerodivisonerror
#s and t between 0 and 1 --> intersection

def self_intersect(p): #blocking self intersects
    #print('self intersect p',p)
    count=0
    if len(p)>3:
        for i in range(len(p)-2):
            try:  
                ###iterated vector###
                a=float(p[i][0]) 
                b=float(p[i][1])
                c=float(p[i+1][0]-p[i][0])
                d=float(p[i+1][1]-p[i][1])
                ###--------------###
               
               ###vector from last 2 points####
                e=float(p[-2][0])
                f=float(p[-2][1])
                g=float(p[-1][0]-p[-2][0])
                h=float(p[-1][1]-p[-2][1])
                ###-----------------######

                S= ( e-a-c*(f-b)/d )/ ((c*h/d)-g) 
                T= (f-b+S*h)/d

            except ZeroDivisionError:
                S=2
                T=2
                pass

            if 0<S<1 and 0<T<1:
                count=1
                break

        if count==1:
            return 'self intersect'

 

def deleter(p): #"erases" old polygon
    t.fillcolor('white')
    t.pencolor('white')
    t.begin_fill()
    t.pu()
    for coord in p: 
        t.goto(coord[0],coord[1])
        t.pd()
        t.write(str(coord)) # write the cursor point coordinate
    t.end_fill()

def redrawer(p): #draws back modified polygon
    t.fillcolor(col)
    t.pencolor(pencol)
    t.begin_fill()
    t.pu()
    for coord in p: #rebuilding modified polygon
        t.goto(coord[0],coord[1])
        t.pd()
        t.write(str(coord)) # write the cursor point coordinate
    t.end_fill()

def analytics():
    analyse=t.textinput("Polygon built","Enter shortcut keys(n to skip)") #to directly analyse
    while True: 
        if analyse=='n':
            return 'pass'
        elif analyse=='c':
            change_vertices()
            break
        elif analyse=='p':
            peri()
            break
        elif analyse=='a':
            area()
            break
        elif analyse=='m':
            mover()
            break
        elif analyse=='s':
            scaler()
            break
        elif analyse=='i':
            file_input()
            break
        elif analyse=='q':
            quitter()
            break
        elif analyse=='r':
            rotator()
            break
        elif analyse=='t':
            pt_inclusion_test()
            break
        elif analyse=='x':
            polygon_selector()
            break
        elif analyse=='d':
            duplicator()
            break
        elif analyse=='u':
            user_menu()
            break
        elif analyse=='f':
            file_input()
            break
        else:
            analyse=t.textinput("Wrong shortcut!","Enter shortcut keys(n to skip)") #to directly analyse


def colours(): #choosing colours
    global col
    global pencol
    pencol=t.textinput("Pen colour","Input pen colour:")
    if pencol=='':
        pencol='black'
    while True: #pen colours
        try:
            t.pencolor(pencol)
            break
        except t.TurtleGraphicsError:
            pencol=t.textinput("Pen colour","Try Again \nInput pen colour:")
            if pencol=='':
                pencol='black'
    col=t.textinput("Fill colour","Input fill colour:") 
    while True: #fill colours
        try:
            t.fillcolor(col)
            break
        except t.TurtleGraphicsError:
            col=t.textinput("Fill colour","Try Again \nInput fill colour:")

def read_file(): #reading in file
    while True:
        file_name=t.textinput("Input file",'Enter input file name:')
        try:
            InFile=open(file_name,'r')
            break
        except FileNotFoundError:
            t.textinput("Enter to acknowledge",'File does not exist! Please reenter file.')
    return InFile

def file_input():
    global p
    global option
    t.pu()
    reader=t.textinput('Read in file?',"Enter 'y' or 'n':")
    while True: # if user wants to input file
        if reader=='y':
            InFile=read_file()
            for L in InFile:
                data=L.strip('[]\n')
                coord=data.split(',')
                if coord[0]=='N':
                    redrawer(p)
                    t.pu()
                    option=1
                    analytics()
                    colours()
                    poly_list.append(p)
                    p=[]
                    option=0
                else:
                    p.append([float(coord[0]),float(coord[1])])
            break
        elif reader=='n':
            break
        else:
            reader=t.textinput('Read in file?',"Enter correct key!\nEnter 'y' or 'n':")

def join_back():   # when button clicked, join back
    global option
    global p
    p.append([p[0][0], p[0][1]]) #add back origin for rebuilding
    if self_intersect(p)=='self intersect':
        t.textinput('Enter to acknowledge','Error! Self intersecting!')
        p.pop()
    else:
        t.goto(p[0][0], p[0][1])
        t.end_fill() #when joining to origin, stop filling colour
        option=1
        t.pu()
        analytics()
    
def change_vertices(ind=-1): 
    global p
    if option!=1:
        t.textinput("Enter to acknowledge","Build polygon first!")
    elif option==1: #only works when polygon drawn
        way=t.numinput("Change/Add vertice","Key '1' for changing vertice,'2' for inserting a new one, '3' for deleting:")
        while True:
            if way==1 or way==2 or way==3:
                break
            else:
                way=t.numinput("Input","Key '1' for changing vertice and '2' for inserting a new one, '3' for deleting: ")

        if way==1: #changing vertice
            number=0 #initialising switch
            vertice_changed=t.numinput('Changing vertice',"Input index of vertice you wanna change")
            while True:  
                if vertice_changed>=(len(p)-1) or vertice_changed<=0: #out of range
                    vertice_changed=t.numinput('Changing vertice',"Error: out of range\nInput index of vertice you wanna change")
                else:
                    x=t.numinput(f"Vertice of index {int(vertice_changed)}","Change x to:")
                    y=t.numinput(f"Vertice of index {int(vertice_changed)}","Change y to:")
                    pe=[]
                    pe.extend(p) #new list storing old p
                    pe[int(vertice_changed)]=[x,y] #adding changed vertex to pe
                    #print('pe',pe)
                    pe1=[] #new list for iteration of pe
                    for item in pe: #iterating through pe
                        pe1.append(item)
                        if self_intersect(pe1)=='self intersect':
                            t.textinput('Enter to acknowledge','Error! Self intersecting!')
                            number=1
                            break
                    if number==0:
                        #print('old p',p)
                        deleter(p)
                        p=pe
                        #print('new p',p)
                        redrawer(p)
                        poly_list[ind]=p
                        #print(poly_list)
                    analytics()
                    break
        elif way==2: #adding new vertex
            number=0
            x=t.numinput("Adding new vertice","Input x")
            y=t.numinput("Adding new vertice","Input y")
            pe=[]
            pe.extend(p) #new list storing old p
            pe.insert(-1,[x,y]) #adding changed vertex to pe
            #print('pe',pe)
            pe1=[] #new list for iteration of pe
            for item in pe: #iterating through pe
                pe1.append(item)
                if self_intersect(pe1)=='self intersect':
                    t.textinput('Enter to acknowledge','Error! Self intersecting!')
                    number=1
                    break
            if number==0:
                deleter(p)
                p=pe
                redrawer(p)
                poly_list[ind]=p
                #print(poly_list)
            analytics()
        elif way==3: #deleting vertex
            number=0
            if len(p)<=4: #if already triangle, deleting will destroy polygon
                t.textinput("Enter to acknowledge","Deleting vertices will destroy polygon!")
                analytics()
            else:
                vertice_changed=t.numinput('Deleting vertice',"Input index of vertice you wanna delete")            
                while True:  
                    if vertice_changed>=(len(p)-1): #out of range
                        vertice_changed=t.numinput('Changing vertice',"Error: out of range\nInput index of vertice you wanna delete")
                    else:
                        pe=[]
                        pe.extend(p) #new list storing old p
                        pe.pop(int(vertice_changed)) #adding changed vertex to pe
                        #print('pe',pe)
                        pe1=[] #new list for iteration of pe
                        for item in pe: #iterating through pe
                            pe1.append(item)
                            if self_intersect(pe1)=='self intersect':
                                t.textinput('Enter to acknowledge','Error! Self intersecting!')
                                number=1
                                break
                        if number==0:
                            deleter(p)
                            p=pe
                            redrawer(p)
                            poly_list[ind]=p
                            #print(poly_list)
                        break
                analytics()
        
def mover():
    global p
    if option!=1:
        t.textinput("Enter to acknowledge","Build polygon first!")
    elif option==1: #only works when polygon completed
        x_dist=t.numinput("X input","Input distance moved in x direction")
        y_dist=t.numinput("Y input","Input distance moved in y direction")
        deleter(p)
        for coord in p:
            coord[0]+=x_dist
            coord[1]+=y_dist
        redrawer(p)
        analytics()
    
def scaler():
    global p
    if option!=1:
        t.textinput("Enter to acknowledge","Build polygon first!")
    elif option==1: #only works when polygon completed
        scale=t.numinput("Scale input","Input scale you wanna modify polygon by")
        deleter(p)
        for coord in p:
            coord[0]*=scale
            coord[1]*=scale
        redrawer(p)
        analytics()

def peri():
    perimeter=0 #initialise perimeter
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first")
    elif option==1:
        for i in range(1,len(p)): #run through coordinates in p 
            length=math.sqrt( (p[i][0]-p[(i-1)][0])**2 + (p[i][1]-p[(i-1)][1])**2 ) 
            perimeter+=length   #add up individual lengths
        t.textinput('Enter to acknowledge',f"perimeter = {perimeter:<10.5f}")
        analytics()

def area():
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first") 
    elif option==1:
        a1,a2,area=0,0,0 #initialise parameters
        for i in range(0,len(p)-1):
            a1+=(p[i][0])*(p[i+1][1])
            a2+=(p[i][1])*(p[i+1][0])
        area=abs((a1-a2)/2)
        t.textinput('Enter to ackowledge',f"area = {area:<10.5f}")
        analytics()

def line(x, y):   # functin that draws a line to the cursor click #If option 1...
    global p
    global option
    if option==0: #by default: line drawn b clicking
        p.append([x, y])  # add the point to the polygon list data as a list
        if self_intersect(p)=='self intersect':
            t.textinput('Enter to acknowledge','Error! Self intersecting!')
            p.pop()
        else:
            t.goto(x,y)
            t.pd()
            t.write(str(x) + ", " + str(y)) # write the cursor point coordinate
    elif option==1: #when join_back called
        poly_list.append(p) #add first polygon to list
        #print(poly_list)
        p=[] #initialise single polygon again
        option=0
        t.pu()
        colours()
        t.begin_fill() #start filling colour again

def key_coord(x,y):  #manually enter coordinates
    x=t.numinput("Input value","Input x")
    y=t.numinput("Input value","Input y")
    line(x,y) #after inputting x and y, draw lines

def quitter(): #to quit the program and store data in file
    while True:
        file_name=t.textinput('Input file','Enter output file name:')
        try:
            OutFile=open(file_name,'w')
            break
        except OSError:
            t.textinput("Enter to acknowledge",'Problem with naming!')
    for item in poly_list: #iterate through list of polygons and print each list on a new line
        if item!=[]: #only adding non blank lists
            for j in item: #iterate through vertices of polygon
                print(j,file=OutFile)
            print("N",file=OutFile)
    OutFile.close()
    t.bye()

def rotator():
    global p
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first") 
    elif option==1:
        angle=t.numinput("Input Angle",'Input Angle in degrees')
        theta=math.radians(angle) #by default, python takes in radians
        x0=t.numinput('X point','Enter x coordinate of point to rotate about')
        y0=t.numinput('Y point', 'Enter y coordinate of point to rotate about')
        
        deleter(p) #erase old polygon

        matrix1=[[math.cos(theta),math.sin(theta)],
                [-(math.sin(theta)),math.cos(theta)]]

        #intialising variables
        result=[[0],
                [0]]
        final=[[0],
                [0]]
        point=[[x0],
                [y0]]
        count=0

        for item in p:
            coord_matrix=[ [item[0]-x0] , 
                            [item[1]-y0] ]

            for i in range(len(matrix1)): #through rows of matrix1
                for j in range(len(coord_matrix[0])): #iterating through columns
                    for k in range(len(coord_matrix)): #iterating through rows
                        result[i][j]+=matrix1[i][k]*coord_matrix[k][j]

            for l in range(len(result)): #iterating through rows
                for m in range(len(result[0])): #iterating through columns
                    final[l][m]=result[l][m]+point[l][m]

            result=[[0],
                    [0]] #resetting result when analysing new coordinate

            x1=final[0]
            for num in x1:
                x=round(num,1)
            y1=final[1]
            for num in y1:
                y=round(num,1)
            p[count]=[x,y]
            count+=1

        redrawer(p) #draw back polygon

def isBetween(a, b, c): ##checking boundary points
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])

    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > 10**-9:
        return False

    dotproduct = (c[0] - a[0]) * (b[0]- a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True

def pt_inclusion_test(): #point on polygon function
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first") 
    elif option==1:    
        global p
        w=[]
        w.extend(p)
        w.pop(-1) #removing origin point

        while True:
            try:
                x = t.numinput('X input',"Please enter a x coordinate: ")
                break
            except ValueError:
                x=t.textinput("Enter to acknowledge",'Error with naming!')
        while True:
            try:
                y = t.numinput('Y input',"Please enter a y coordinate: ")
                break
            except ValueError:
                t.textinput("Enter to acknowledge","Error with naming!")

        xy = [x,y]
        
        counter1 = 0 #initialise counters   
    
        for i in w:
            if w.index(i) == len(w)-1:
                pass

            else:
                sideptA = (i[0],i[1])
                sideptB = (p[p.index(i)+1][0],p[p.index(i)+1][1])
                x1 = sideptA[0]
                x2 = sideptB[0]
                y1 = sideptA[1]
                y2 = sideptB[1]
                if ((y<y1)!=(y<y2)) and (x<((((x2-x1)*(y-y1))/(y2-y1))+x1)):
                    counter1 +=1
                else:
                    pass
                
        if counter1 %2 == 0:
            counter2=0
            ind=0 #index producer
            for i in w:
                if w.index(i) == len(w)-1:
                    pass

                else:
                    sideptA = (i[0],i[1])
                    sideptB = ([w.index(i)+1][0],w[w.index(i)+1][1])
                    x1 = sideptA[0]
                    x2 = sideptB[0]
                    y1 = sideptA[1]
                    y2 = sideptB[1]
                    print(i)
                    print([w[ind+1]])
                    print([[x],[y]])
                    if isBetween(i,w[ind+1],[x,y]): 
                        counter2 =1
                    else:
                        pass
            ind+=1
            for item in p:  #forcing boundary points to be on boundary of polygon
                if [x,y]==item:
                    counter2=1
            if counter2==1:    
                t.textinput('Enter to acknowledge',f"Coordinate {xy} is inside the polygon.")

            else:    
                t.textinput('Enter to acknowledge',f"Coordinate {xy} is outside the polygon.")

        else:
            t.textinput('Enter to acknowledge',f"Coordinate {xy} is inside the polygon.")
        analytics()

def polygon_selector(): #key x
    count=0 #intialise switch
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first") 
    elif option==1:    
        global p
        while True:
            x=t.numinput('X input','Enter x coordinate of point on chosen polygon')
            y=t.numinput('Y input','Enter y coordinate of point on chosen polygon')
            ind=0 #initialise           
            for polygon in poly_list:
                if [x,y] in polygon: #checking if x,y valid
                    poly_list.append(p) #add current polygon to poly_list
                    poly_list.pop(ind) #removing old polygon from list
                    print('befre',poly_list)
                    p=polygon
                    poly_list.append(p) #add chosen polygon back to list
                    print('after',poly_list)
                    count=1
                    break
                ind+=1

            if count==1:
                break
        analytics()    

def rotator_for_duplication(x0,y0,angle,copies,p,scale): #x0,y0 point to rotate about
    global poly_list
    theta=math.radians(angle*copies) #by default, python takes in radians #increase angle with each copy

    matrix1=[[math.cos(theta),math.sin(theta)],
            [-(math.sin(theta)),math.cos(theta)]]

    #intialising variables
    result=[[0],
            [0]]
    final=[[0],
            [0]]
    point=[[x0],
            [y0]]
    count=0

    for item in p:
        coord_matrix=[ [item[0]-x0] , 
                        [item[1]-y0] ]

        for i in range(len(matrix1)): #through rows of matrix1
            for j in range(len(coord_matrix[0])): #iterating through columns
                for k in range(len(coord_matrix)): #iterating through rows
                    result[i][j]+=matrix1[i][k]*coord_matrix[k][j]

        for l in range(len(result)): #iterating through rows
            for m in range(len(result[0])): #iterating through columns
                final[l][m]=result[l][m]+point[l][m]

        result=[[0],
                [0]] #resetting result when analysing new coordinate

        x1=final[0]
        for num in x1:
            x=round(num,1)
        y1=final[1]
        for num in y1:
            y=round(num,1)
        p[count]=[x*scale,y*scale]
        count+=1
    print(p)
    pe=[]
    pe.extend(p)
    poly_list.append(pe)
    print(poly_list)
    redrawer(p) #draw back polygon 


def duplicator():
    global p
    print(poly_list)
    if option==0: #warn users when polygon not built
        t.textinput('Enter to acknowledge',"Build polygon first") 
    elif option==1:    
        copies=int(t.numinput('Enter input','Input number of copies'))
        while True:
            if copies>=1:
                break
            else:
                copies=int(t.numinput('Error in input!','Input number of copies')) 
        
        way=t.numinput('Enter input',"Enter '1' for linear duplication\nand '2' for rotating duplication")               
        while True: #checking if duplicate linearly or by rotation
            if way==1 or way==2:
                break
            else:
                way=t.numinput('Enter correct input!',"Enter '1' for linear duplication\nand '2' for rotating duplication")               
        if way==1:
            x_dist=t.numinput('X dist','Input distance of copies from each other in x direction')
            y_dist=t.numinput('Y dist','Input distance of copies from each other in y direction')
            p_new=[]
            t.pu()
            poly_list.append(p)   #to store original value in list of polygons            
            for i in range(1,copies+1): 
                for coord in p: #iterating through coordinates
                    p_new.append([coord[0]+x_dist*i,coord[1]+y_dist*i]) #creating new p list
                t.pu()
                t.begin_fill()
                scale=t.numinput("Scale input?","Input scale you wanna modify polygon by\n(1 if don't want)")
                for coord in p_new: #scaling p_new
                    coord[0]=coord[0]*scale #attempting to make the polygons closer to each other?
                    coord[1]=coord[1]*scale
                    t.goto([coord[0]+x_dist*i,coord[1]+y_dist*i])
                    t.write(str(coord[0]) + ", " + str(coord[1])) # write the cursor point coordinate
                    t.pd() #begin writing after going to first point
                t.end_fill()
                poly_list.append(p_new)
                p_new=[] #initialising before next copy
                print(poly_list)
                t.pu()
            p=[]
                
        elif way==2:
            poly_list.append(p)
            angle=t.numinput('Enter Angle','Enter angle in degrees to rotate each copy')
            x0=t.numinput('X point','Enter x value to rotate about')
            y0=t.numinput('Y point','Enter y value to rotate about')
            for i in range(1,copies+1):
                scale=t.numinput("Scale input?","Input scale you wanna modify polygon by\n(1 if don't want)")
                rotator_for_duplication(x0,y0,angle,copies,p,scale)
            p=[]

    analytics()

def user_menu():
    t.textinput("User Menu",
        """ 
Left click: Draw the lines from point to point.   

Right click: To input coordinates with your keyboard.   

Spacebar: Will complete polygon by returning to the origin.  

p: Will print perimeter (in text box). If pressed before polygon complete, will prompt error. 

c: Change vertices. Follow steps afterwards.  

m: To move polygon 

i: Input file containing polygon data 

r: Rotate polygon a certain amount of degrees 

t: Point inclusion test to check if point lies in polygon 

q: Quit the program 

x: Select polygon by specifying a vertex corresponding to polygon of choice 

d: Duplicates the polygon 

f: Read in file


Enter to acknowledge
"""
    )

###--------------------------------------Main Code ----------------------------------------------###
t.pu()
t.pencolor('black')
t.setposition(-250,250)
t.pd()
t.write("Press 'u' for user menu") #for access to shortcuts
t.pu()

colours()
file_input()
t.pu()

t.begin_fill()  #begin tracing shape to fill colour
s.onclick(line) # onclick calls line() when left mouse button clicked.
                # left mouse button is default, need specify second parameter
                # if right mouse button used.

                #option 1 for..2 for...

#-----buttons pressed on main screen---#
s.onclick(key_coord,3) #calls key_coord on right mouse button
s.onkeypress(join_back,'space') #press spacebar join back to origin
                                #But not working after right click
s.onkeypress(change_vertices,"c") #press c to change vertices 
s.onkeypress(peri,"p") #press p to calculate perimeter
s.onkeypress(area,'a')
s.onkeypress(mover,'m')
s.onkeypress(scaler,'s')
s.onkeypress(read_file,'i')
s.onkeypress(quitter,'q')
s.onkeypress(rotator,'r')
s.onkeypress(pt_inclusion_test,'t')
s.onkeypress(polygon_selector,'x')
s.onkeypress(duplicator,'d')
s.onkeypress(user_menu,'u')

s.listen()
t.done()

#create new list to store polygons; recognise by index #Y
#still in line function: keep drawing #Y
#upon clicking right mouse button, change choice option #Y
#then change to 0 #Y
#option 2 find area



