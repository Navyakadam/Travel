#!/usr/bin/env python
# coding: utf-8

# In[1]:


import webbrowser


countries = ["Australia","England","France","India","Italy","Switzerland","Germany","Spain","USA"]

my_dict = {"Australia":["Sydney","Melbourne","Canberra","Perth","Brisbane","Adelaide","Hobart","Gold Coast","Darwin","Alice Springs"],
          "England":["London","Southampton","leicester","Liverpool","Manchester","Bristol","Durham","Birmingham","York","Leeds","Sheffield","Newcastle"],
          "France":["Paris","Cannes","Lyon","Marseille","Nice","Bordeaux","Starsbourg","Toulouse","Lille","Avignon","Rennes","Dijon","Rouen","Annecy"],
          "India":["Mysore","Banglore","Mumbai","NewDelhi","Udaipur","chandigarh","Dehradun","cochin","Munnar","Ooty","Coorg","Kanyakumari","Chennai","Rameshwaram","Mussoorie","Dwarka","Rishikesh","kedarnath","Manali"],
          "Italy":["Rome","Venice","Florence","Pisa","Naples","Milan","Pisa","Naples","Bologna","Turin","Genoa","Verona","Catania","San Marino","Amalfi"],
          "Switzerland":["Zurich","Geneva","Basel","Lugano","Bern","St. Gallen","Chur","Thun","Biel/Bienne"],
          "Germany":["Berlin","Hamburg","Munich","Frankfurt","Stuttgart","Dortmund","Essen","Düsseldorf","Cologne","Hanover","Leipzig","Wolfsburg","Nuremberg","Bremen","Dresden"],
          "Spain":["Madrid","Barcelona","Bilbao","Jerez De La Frontera","Valencia","Malaga","Seville","Granada","Cuenca","Ronda","Galera"],
          "USA":["New York","Los Angeles","Chicago","Washington","Austin","Nashville","Phoenix","San Francisco","Indianapolis","Boston","Las Vegas","California"]
          }

print("***************************")
print("**Welcome to trip planner**")
print("*************************\n")


name = input("Hello there! What is your name?")
print("\nOh hey, "+name+"! \nNice to meet you")


print("\nOur services extend to various countries.Right now,we can offer you a quality time in one of the following:\n")

i = 1
for c in my_dict.keys():
    print(str(i)+"."+str(c))
    i+=1
print()  


country = int(input("Which country you are interested in to spend your trip/vacation? Please type in the index number:"))
my_country = countries[country-1]
print()
print(my_country+" is an amazing choice indeed! In "+my_country+" we offer a tour in one of the following cities:\n")
i = 1
for v in my_dict[my_country]:
    print(str(i)+"."+str(v))
    i+=1
print()    


city = int(input("So tell us! Which place do you want to go on a vacation/tour? Enter its index number:"))
my_city = my_dict[my_country][city-1]
print()
print("So you want to go to "+my_city+"? That is an awesome choice!")


info = input("Do yoy want to explore "+my_city+"? (Y/N)")
if(info=='Y' or info=='y'):
    url_city = "https://en.wikipedia.org/wiki/"+my_city
    webbrowser.open_new_tab(url_city)
elif(info=='N' or info=='n'):
    print("Cool! it seems you already know about the "+my_city+" Thats awesome")
 

nop = int(input("\nSo,"+name+".You must be bringing along a few people atleast, right?To help us plan your trip better, please tell us how many people you're bringing with you:"))    
if(nop==0):
    print("\nOh! its more like a solo trip!")
elif(nop==1):
    print("\nOh so its "+str(nop+1)+" going together! So we hope both of you have a great and memorable tour/vacation together!")
else:
    print("\nOh so its "+str(nop+1)+" going together! So we hope all of you have a great and memorable tour/vacation together!")
  

days = int(input("For how many days are you planning to stay in "+my_city+"?"))
budget = int(input("\nHow much currency in INR are you planning to carry?"))

if(country==1):
    factor=0.019
elif(country==2):
    factor=0.011
elif(country==3):
    factor=0.012    
elif(country==4):
    factor=1
elif(country==5):
    factor=0.012
elif(country==6):
    factor=0.012
elif(country==7):
    factor=0.012    
elif(country==8):
    factor=0.012
elif(country==9):
    factor=0.013
#elif(country==5):
    factor=0.012    
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012
#elif(country==5):
    factor=0.012 

    
print(str(budget)+" INR is around "+str(int(budget*factor))+" in "+my_country+"'s native currency")  
if(budget<500000):
    print("\nThis much money is sufficient! You'll spend around "+str(int(budget*factor/days))+" per day on average.")
else:
    print("\nThis much money is more than enough for you to enjoy this trip to the fullest! and You'll spend around "+str(int(budget*factor/days))+" per day on average.")


hotelbooked = False
print("\nNow lets see the hotel's where you could be staying for the trip")
choice = input("Shall we?(Y/N)")
def book_hotel(choice):
    if(choice=='N' or choice=='n'):
        print("\nOkay then we'll come back to this later on!")
    elif(choice=='Y' or choice=='y'):
        urlh = "https://www.trivago.in/"
        webbrowser.open_new_tab(urlh)
        hotelbooked = True
        
        
book_hotel(choice)   


print("\nNow lets go ahead and book the tickets.")
flightbooked = False
def book_flight():
    print("\nWhich of the following websites do you prefer?")
    site = int(input("1.Clear Trip\n2.Goibibo\n3.Yatra.com\n4.MakeMyTrip\nchoice:"))
    if(site==1):
        url = 'https://www.cleartrip.com/'
    elif(site==2):
        url = 'https://www.goibibo.com/'
    elif(site==3):
        url = 'https://www.yatra.com/'
    elif(site==4):
        url = 'https://www.makemytrip.com/'
    info2 = input("Proceed to website?(Y/N)")
    if(info2=='Y' or info2=='y'):
        webbrowser.open_new_tab(url)
        book = input("\nDid you find your desired seat? (Y/N):")
        if(book=='N' or book=='n'):
            book_flight()
        else:
            flightbooked = True
            print("\nOkay that's great!")
    else:
        print("\nOkay we'll do that later")
        

book_flight()   


if(hotelbooked==False):
    choice = input("\n Would you like to book the hotel room now? (Y/N):")
    if(choice=='Y' or choice=='y'):
        print("\nOkay lets go!")
        book_hotel(choice)
    else:
        print("Alright then!")

        
if(flightbooked==False):
    choice = input("\nWould you like to book the tickets now?(Y/N):")
    if(choice=='Y' or choice=='y'):
        print("\nOkay lets go!")
        book_flight()
    else:
        print("Alright then!")
print("We genuinely hope you have an amazing trip and return home with plenty of unforgettable moments! Hope you'll think of us next time when you wish to travel once again. See you later\nTake care, "+name+"!") 
print("************************")

#end of program


# In[ ]:





# In[ ]:




