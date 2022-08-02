from geopy.geocoders import Nominatim 
#create a locations.txt in the folder and put on it the addres 
with open('locations.txt') as fh:
   locations = fh.readlines()
lst=[]
for location in locations:
   
   lst.append(location)
  
print(lst)

loc = Nominatim(user_agent="GetLoc")
for location in lst:
    try :
        print("/////////////////")
        getLoc = loc.geocode(location)
            
            
        print(getLoc.address)
            
            
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
        print(location)
        print("/////////////////")
    except :
        print("you did not enter a correct location")


