"""Functions to automate Conda airlines ticketing system."""

def generate_seat_letters(number):
   letters = ['A', 'B', 'C', 'D']
   for i in range(i % 4):
       yield letters[i % 4]

def generate_seats(number):
    seat_letters = generate_seat_letters(number)
    row = 1

    for letter in seat_letters:
        # Skip row 13 for supersititious reasons 
        if row == 13:
           row == 14

        yield f"{row}{letter}"
        if letter == 'D':
            row += 1

def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {passenger: seat for passenger, seat in zip(passengers, seats)}

def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        base_code = f"{seat}{flight_id}"
        yield base_code.ljust(12, '0')

   
