# read a line at a time from the file as a string
file = open("data.txt", "r")
Lines = file.readlines()


#set
uniqueOutputs = set()

#while not end of the string
for line in Lines:
    
    #initial values for shared variables
    y = 3
    x = 0
    #each thread has its own set of registers
    R1 = 0
    R2 = 0
    for ch in line:
        if( ch == "1" or ch == "4"):
            R1 = y
        elif(ch == "2"):
            R1 += 1
        elif(ch == "3"):
            y = R1
        elif(ch == "5"):
            x = R1
        elif(ch == "6"):
            R2 = y
        elif(ch == "7"):
            R2 *= 2
        elif(ch == "8"):
            y = R2

    uniqueOutputs.add(str(x) + str(y))  
    if(str(x) + str(y) in uniqueOutputs):
        print(str(x) + str(y) + "_" + line + "\n")


#print set elements
for element in uniqueOutputs:
    print(element)



"""
Original program

int y = 3;  x = 0;
void foo () {
	y = y + 1;
	x = y;
}
void bar () {
	y = y * 2;
}
main () {
	Thread t1 = createThread (foo);
	Thread t2 = createThread(bar);
	WaitForAllDone(); 
	cout << x  << y <<endl;
}

"""