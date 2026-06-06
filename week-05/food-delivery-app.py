#Parent class
class DeliveryPartner:
    def __init__(self, name, partner_id, deliveries):
        #Gets partners name, id and deliveries
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        pass

    def display(self):
        earning = self.total_earning()
        print(f"Name: {self.name}")
        print(f"Partner ID: {self.partner_id}")
        print(f"Deliveries: {self.deliveries}")
        print(f"Total Earning: NPR {earning}")
        print("----------------------------")


class BikeRider(DeliveryPartner):
    #Gets partners name, id and deliveries plus km travelled
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

    def total_earning(self):
        #Bike rider delivery partner, earns 80 per delivery + 5 per km
        return (self.deliveries * 80) + (self.km_travelled * 5)


class Walker(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, rainy_deliveries):
        #Gets partners name, id and deliveries plus any rainy-deliveries they did
        super().__init__(name, partner_id, deliveries)
        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):
        #Walker delivery partner, earns 60 per delivery + 50 per rainy delivery
        return (self.deliveries * 60) + (self.rainy_deliveries * 50)


class CarDriver(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, fuel_cost):
        #Gets partners name, id and deliveries plus the fuel_cost
        super().__init__(name, partner_id, deliveries)
        self.fuel_cost = fuel_cost

    def total_earning(self):
        #Car driver delivery partner, earns 120 per delivery - fuel cost
        return (self.deliveries * 120) - self.fuel_cost

#Dummy data
partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]

print("=== FOOD DELIVERY PARTNER EARNINGS ===")
#Display all partners
for partner in partners:
    partner.display()

#Displaying partner with the highest earning
highest_earner = max(partners, key=lambda p: p.total_earning())
print(f"Highest Earner: {highest_earner.name} (NPR {highest_earner.total_earning()})")
