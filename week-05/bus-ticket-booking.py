class Bus:
    def __init__(self, route, total_seats):
        #Gets the route, total seats and booked passengers name and seat number
        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    def book_seat(self, seat_number, passenger_name):
        if seat_number < 1 or seat_number > self.total_seats:
            print(f"Invalid seat number! Bus has seats number 1 to {self.total_seats}")
        elif seat_number in self.booked:
            print(f"Seat is already booked")
        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        if len(self.booked) == 0:
            print("No bookings yet")
        else:
            print("Booked Seats:")
            for seat_num in sorted(self.booked.keys()):
                print(f"  Seat {seat_num}: {self.booked[seat_num]}")

print("=== SAJHA YATAYAT BUS BOOKING SYSTEM ===")

bus = Bus("Kathmandu - Pokhara", 10)

print(f"\nBus Route: {bus.route}")
print(f"Total Seats: {bus.total_seats}\n")

#Dummy data with duplicates for error checking
bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

print("Processing bookings:")
for seat_num, passenger_name in bookings:
    bus.book_seat(seat_num, passenger_name)

print("\n----------------------------")
print(f"\nAvailable Seats: {bus.available_seats()}")
print(f"Booked Seats: {len(bus.booked)}\n")
bus.passenger_list()
