#This is a program calculating a user's holiday cost
#including plane, hotel and car rental cost
#define variables
flight_valid = False
hotel_valid = False
car_valid = False

#prompt for user of the options of city
print(
    '''
    Hello, you can fly
    (City: flight cost)
    Amsterdam: £100
    Bristol: £20
    Copenhagen: £300
    Dubai: £4000
    '''
    )

#ask user for location, number of nights and day of rental and validate input
while flight_valid == False: #validate the city of flight
    city_flight = str(input("Which city would you like to fly to?"))
    city_flight = city_flight.lower()
    if (city_flight == "amsterdam") or (city_flight == "bristol") or (city_flight == "copenhagen") or (city_flight == "dubai"):
        flight_valid = True
    else:
        print("invalid city, please try again! (try enter amsterdam or bristol or copenhagen or dubai)")
        continue

while hotel_valid == False: #validate the length of stay in hotel
    try:
        num_nights = float(input("How many nights will you be staying at a hotel?"))
        if num_nights < 0:
            print("You cannot have negative number of nights at a hotel!")
            continue
        elif (int(num_nights)-num_nights==0):
            num_nights = int(num_nights)
            hotel_valid = True
        else:
            print("please enter a whole number")
            continue
    except:
        print("Please enter a number!")
        continue

while car_valid == False: # validate the days of car rental
    try:
        rental_days = float(input("How many days will you be hiring a car for?"))
        if rental_days < 0:
            print("You cannot have negative day of car rental!")
            continue
        elif (int(rental_days)-rental_days==0):
            rental_days = int(rental_days)
            car_valid = True
        else:
            print("please enter a whole number")
            continue
    except:
        print("Please enter a number!")
        continue

#define the function for hotel, plane, car and total cost 
def hotel_cost(num_nights,price_per_night=100):
    hotel_cost = num_nights * price_per_night
    return hotel_cost

def plane_cost(city_flight):
    if city_flight == "amsterdam":
        plane_cost = 100
    elif city_flight == "bristol":
        plane_cost = 20 
    elif city_flight == "copenhagen":
        plane_cost = 300
    elif city_flight == "dubai":
        plane_cost = 4000
    else:
        print("Error in plane cost")
    return plane_cost

def car_rental(rental_days,daily_rental_cost=50):
    car_rental = rental_days * daily_rental_cost
    return car_rental

def holiday_cost(num_nights, city_flight, rental_days):
    hotel_money = hotel_cost(num_nights)
    plane_money = plane_cost(city_flight)
    car_rental_money = car_rental(rental_days)
    holiday_cost = hotel_money + plane_money + car_rental_money
    return holiday_cost

#run the program to display details
hotel_money = hotel_cost(num_nights)
plane_money = plane_cost(city_flight)
car_money = car_rental(rental_days)
holiday_money = holiday_cost(num_nights, city_flight, rental_days)

print(f'''
You are staying for {num_nights} nights
Hotel costs £{hotel_money}

You are flying to {city_flight}
Flight costs £{plane_money}

You are renting the car for {rental_days} days
Car rental costs £{car_money}

The total cost of your holiday is £{holiday_money}''')

#End of program