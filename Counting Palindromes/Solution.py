from datetime import datetime
from datetime import timedelta

# code to take input durinng runtime could be added later here
n1=1
n2=2

def check_palindrome(string):# returns true if string is palindrome
    reversed_string = string[::-1]
    #status=1
    if(string==reversed_string):
        return True
    else:
        return False
      
def next_time(prev_time):
        time_prev = datetime.strptime(prev_time,"%H%M%S")#given string in format hhmmss is converted to time(type)
        time_new = time_prev + timedelta(0,1)#time is incremented by one second
        time_new_string=time_new.strftime("%H%M%S")# time is converted to string
        return (time_new_string)# string is returned
      
def count_palindromes(n1,n2):
    pal_count=0 #variable to count number of palindrome
    time_in='235959' # time initilized in format hhmmss .Taking the last second of the day (235959) and addinng one seconnd gives 000000.
    #thus the while loops checks for palinndroemm from 000000. 
    time_thing=time_in # time is
    #variables for while loop
    count=n1
    count_till=n2+1#checking the condition of whil emight help you understand why a day greater than n2 is taken
    #The input n1 and n2 are days.. the while loops until a day greater than n2 is reached
    while(count<count_till):# we coud also use the condition(a<=b) and increment a below
        time_thing=next_time(time_thing)#get next second in hhmmss format
        if(check_palindrome(str(count)+time_thing)==True):#Adds the day counter to the hhmmss and check for palindrome
            #print(str(count)+time_thing)
            #commment out the above line to print all the possible palindromes
            pal_count+=1
        if(time_thing=='235959'):#checks if time has looped through every second of the day
            count+=1  #If the condition evaluates
    print(pal_count)

count_palindromes(n1,n2)
