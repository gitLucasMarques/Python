from random import randint, random, choice
from typing import List
from datetime import datetime
from time import sleep
from enum import Enum

TAX_BASE = 3

class typeService(Enum):
    UBER_X = 1
    UBER_XL = 2
    UBER_BLACK = 3
    
class typeLocation(Enum):
    POPULAR = 1
    AVERAGE = 2
    HIGH = 3
    LUXURY = 4

class Location():
    def __init__(self, name: str, local: typeLocation):
        self.name = name
        self.local = local

class Driver():
    def __init__(self, name: str, car: str):
        self.name = name
        self.car = car
        self.travels = []
        self.wallet = 0.0

class Passenger():
    def __init__(self, name: str, localInitial: Location):
        self.name = name
        self.localInitial = localInitial

class Trip():
    def __init__(self, typeS: typeService, driver: Driver, passenger: Passenger, distance: float, market: float, timeInitial: int):
        self.typeS = typeS
        self.driver = driver
        self.passenger = passenger
        self.travelDistance = distance
        self.market = market
        self.timeInitial = timeInitial
        self.timeEstimated = randint(1, 60)
        self.timeFinal = 0
        self.priceTrip = 0.0
    
    def departure(self, timeI: int):
        self.timeInitial = timeI
        return self
        
    def arrival(self, timeF: int):
        self.timeFinal = timeF
        return self
        
    def calculate_trip(self):
        payment = Payment(self)
        self.priceTrip = payment.baseRate()
        self.priceTrip = payment.kilometerRate(self.market)
        self.priceTrip = payment.minuteRate()
        self.priceTrip = payment.surgePricing()
        return self.priceTrip

class Payment():
    def __init__(self, trip: Trip):
        self.trip = trip
        self.value = TAX_BASE
    
    def baseRate(self):
        self.value += (TAX_BASE * self.trip.typeS.value) + (2 * self.trip.passenger.localInitial.local.value)
        return self.value
            
    def kilometerRate(self, proportional: float):
        if self.trip.market <= 0.2: proportional = 0.15
        elif self.trip.market <= 0.4: proportional = 0.2
        elif self.trip.market > 0.5 and self.trip.market < 1: proportional = 0.3
    
        self.value += (proportional * (self.trip.travelDistance / 10) * self.trip.typeS.value * self.trip.passenger.localInitial.local.value * self.trip.market)
        return self.value
            
    def minuteRate(self):
        if self.trip.timeInitial - self.trip.timeFinal > self.trip.timeEstimated:
            self.value += (self.trip.timeInitial - self.trip.timeFinal) * 1.2
        return self.value
    
    def surgePricing(self):
        if self.trip.market > 1:
            self.value += (self.trip.travelDistance / 5) * self.trip.typeS.value * self.trip.passenger.localInitial.local.value * self.trip.market
        return self.value

def simulate_cancellation():
    return random() < 0.3

def generate_market_factor():
    return round(random() * 2, 2)

def apply_extra_promotion(driver: Driver):
    if random() < 0.2:
        bonus = randint(10, 50)
        driver.wallet += bonus
        print(f"Promoção extra! Bônus de R${bonus} aplicado.")

class UberDriver():
    def __init__(self):
        self.collaborators: List[Driver] = []
    
    def add_collaborator(self, driver: Driver):
        self.collaborators.append(driver)
    
    def show_wallet_driver(self, driver: Driver):
        print(f"\n//--------WALLET--------//\n")
        print(f"Saldo do motorista {driver.name}: R${driver.wallet:.2f}")

def main():
    location_uber = Location("Centro", typeLocation.POPULAR)
    driver1 = Driver("João", "Fiat Uno")
    passenger1 = Passenger("Lucas", location_uber)

    total_viagens = 10
    for viagem_num in range(1, total_viagens + 1):
        print(f"\n//--------Viagem {viagem_num}--------//\n")

        distance = randint(5, 20)
        time_initial = randint(1, 30)
        market_factor = generate_market_factor()
        
        trip = Trip(typeService.UBER_X, driver1, passenger1, distance, market_factor, time_initial)
        trip.departure(time_initial)
        
        if simulate_cancellation():
            print(f"A viagem foi CANCELADA pelo passageiro!")
            continue

        time_final = time_initial + randint(15, 45)
        trip.arrival(time_final)

        driver1.wallet += trip.calculate_trip()
        driver1.travels.append(trip)
        
        print(f"Pagamento da Viagem {viagem_num}: R${trip.priceTrip:.2f}")
        print(f"Saldo do motorista após viagem {viagem_num}: R${driver1.wallet:.2f}")

        apply_extra_promotion(driver1)

        print(f"Saldo do motorista (após bônus): R${driver1.wallet:.2f}")

        sleep(1)

    uber_driver = UberDriver()
    uber_driver.add_collaborator(driver1)
    uber_driver.show_wallet_driver(driver1)

    tip = 15.0
    driver1.wallet += tip
    print(f"\nGorjeta de R${tip:.2f} aplicada!")
    uber_driver.show_wallet_driver(driver1)

if __name__ == "__main__":
    main()
