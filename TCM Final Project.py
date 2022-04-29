
#Think Code Make Final Project
#Rebecca Hirata and Juan Jose De Mendiola
import time
import datetime
import random as r
import emoji


hours = int( input("How long, in hours, would you like to run the simulation for? (Suggested 3-8) \n -> ") )
speed = int( input("At what speed would you like to run the simulation? (Suggested 200-600) \n -> ") )

cashiers = int( input("Choose the number of cashiers available -> ") )
distribution_cashier = input("Choose the type of distribution for cashier's attention time \n A) Uniform \n B) Normal  \n -> ").upper()
if distribution_cashier == "A":
    lim_min_cashier = float( input("Choose the minimum amount of time a client could be at the cashier's window (in minutes) -> ") )
    lim_min_cashier = lim_min_cashier * 60
    lim_max_cashier = float( input("Choose the maximum amount of time a client could be at the cashier's window (in minutes) -> ") )
    lim_max_cashier = lim_max_cashier * 60
if distribution_cashier == "B":
    median_cashier = float( input("Choose the median of attention time in the cashier (in minutes) -> ") )
    median_cashier = median_cashier * 60
    desv_std_cashier = float( input("Choose the standard deviation of the attention time in each cashier (in minutes) -> ") )
    desv_std_cashier = desv_std_cashier * 60

distribution_client = input("Choose the type of distrubition of each client's arrival \n A) Uniform \n B) Normal  \n -> ").upper()
if distribution_client == "A":
    lim_min_client = float( input("Choose the minimum amount of time a client could take to arrive (in minutes) -> ") )
    lim_min_client = lim_min_client * 60
    lim_max_client = float( input("Choose the maximum amount of time a client could take to arrive (in minutes) -> ") )
    lim_max_client = lim_max_client * 60
if distribution_client == "B":
    median_client = float( input("Choose the median time for the arrival of the clients  (in minutes) -> ") )
    median_client = median_client * 60
    desv_std_client = float( input("Choose the standard deviation for the arrival time of each client (in minutes) -> ") )
    desv_std_client = desv_std_client * 60

seats = int( input("Choose the number of seats (to wait) in each cashier -> ") )
t_wait = float( input("Choose the time until a client is upset by the waiting time and leaves (in minutes) -> ") )
t_wait = t_wait * 60

max_secs = 3600 * hours
secs = 0
c = 0
e = 0
attended = 0
not_attended = 0

b = [["_" for i in range(seats)] for i in range(cashiers)]
m = [["_" for i in range(seats)] for i in range(cashiers)]
x = [[] for i in range(cashiers)]
v = []
t_attention = []
t = []


while secs <= max_secs:
   #Attention to clients#     
   f = 0
   while f < cashiers:
       if b[f][seats - 1] != "_":
           
           #Take attention time of each client#
           if len(x[f]) == 0:
               if distribution_cashier == "A":
                   u = r.randint(lim_min_cashier, lim_max_cashier)
        
               elif distribution_cashier == "B":
                   u = int(r.gauss(median_cashier, desv_std_cashier))
                   while u <= 0:
                       u = int(r.gauss(median_cashier, desv_std_cashier))
               t_attention.append(u)
               u += secs
               x[f].insert(0, u)
        
           attention = u
           #Attend each client#
           if attention == secs:
               wait = u - b[f][seats - 1]
               t.append(wait)
               
               m[f].pop(seats - 1) 
               m[f].insert(0, "_")
               b[f].pop(seats - 1)
               b[f].insert(0, "_")
               print(str(datetime.timedelta(seconds=secs)), end=" ")
               print( "A client was attended at a cashier", f)
               
               x[f].pop(0)
               attended += 1
               
               for i in m:
                   for j in i:
                       print(j, end=" ")
                   print("T")
               print()    
       f +=1
       
   
   #Find arrival time of each client#
   if c >= len(v):
       if distribution_client == "A":
           a = r.randint(lim_min_client, lim_max_client)
       elif distribution_client == "B":
           a = int(r.gauss(median_client, desv_std_client))
           while a <= 0:
               a = int(r.gauss(median_client, desv_std_client))
       a = secs + a
       v.append(a)    
       
   if secs == a:
       #Find cashier with the most seats available#
       p,k = 0,0
       q = []
       
       #Find maximum amout of seats available#    
       while p < cashiers:
           h = m[p].count("_")
           q.append(h)
           p += 1
       
       w = max(q)
       
       while k < cashiers:
           n = m[k].count("_")
           if n == w and n != 0:
               break
           k += 1   
       
       #Entrance of clients into the bank and lines#  
       c += 1
       if w == 0:
           print(str(datetime.timedelta(seconds=secs)), end=" ")
           print( "A client came in, but there wasn't enough space at the bank \n" ) 
           not_attended += 1
           
       if w != 0:
           print(str(datetime.timedelta(seconds=secs)), end=" ")
           print( "A client formed in the line " + str(k) )
           m[k].insert(w, "\U0001f600")
           m[k].pop(0)
           b[k].insert(w, a)
           b[k].pop(0)
           
           for i in m:
               for j in i:
                   print(j, end=" ")
               print("T")
           print()
        
   #Making a client upset#
   z = 0
   for i in b:
       g = 0
       for j in i:
           if j != "_":
               upset = j + t_wait
               
               if upset == secs:
                   if g != (seats - 1):
                       print(str(datetime.timedelta(seconds=secs)), end=" ")
                       print( "A client got upset in the line", z)
                       e += 1
                       m[z].pop(g)
                       m[z].insert(g, "\U0001F92C")
                       
                       for i in m:
                           for j in i:
                               print(j, end=" ")
                           print("T")
                       print()       
           g += 1
       z += 1
      
   time.sleep(1/speed)
   secs += 1


print("End of the simulation. \n")

#Questions at the End#
print("Statistics: \n")
time.sleep(1)

#How many people came into the bank?#
print("• Arrived ", str(c), "people in total. \n")
time.sleep(1)   

#How many people left the bank?#
print("•", str(not_attended), "people left due to low capacity at the bank. \n")
time.sleep(1)

#How many people were seen by a cashier?#
print("•", str(attended), "people were seen by a cashier. \n")   
time.sleep(1)

#What was the average attention time?#
print("• The average attention time was", datetime.timedelta(seconds=(sum(t_attention)/len(t_attention))), "minutes. \n")
time.sleep(1)

#How many people got upset and left?#
print("•", str(e), "people got upset and left due to the waiting time. \n")
time.sleep(1)
   
#What was the maximum attention time?#
print("• The maximum wait time was", datetime.timedelta(seconds=max(t)), "minutes.")
time.sleep(1)

