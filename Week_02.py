TicketCost = 25.00

TrainUpTime = [9, 11, 13, 15]
TrainUpTickets = [480, 480, 480, 480]
TrainUpMoney = [0.0, 0.0, 0.0, 0.0]

TrainDownTime = [10, 12, 14, 16]
TrainDownTickets = [480, 480, 480, 480]
TrainDownMoney = [0.0, 0.0, 0.0, 0.0]

print("Train Time\t Tickets \t Tickets Available")
for count in range(4):
    print(f"{TrainUpTime[count]}\t\t\t{TrainUpTickets[count]}\t\t\t{TrainUpMoney[count]}")
    print(f"{TrainDownTime[count]}\t\t\t{TrainDownTickets[count]}\t\t\t{TrainDownMoney[count]}")

selling_tickets = "yes"
while selling_tickets.lower() == "yes":
    time_up = int(input("What time would you like to go up the mountain? 9, 11, 13, 15: "))
    while time_up not in TrainUpTime:
        time_up = int(input("Error. What time would you like to go up the mountain? 9, 11, 13, 15: "))

    index_up = TrainUpTime.index(time_up)

    time_down = int(input("What time would you like to go down the mountain? 10, 12, 14, 16: "))
    while time_down not in TrainDownTime or time_down < time_up:
        time_down = int(input("Error. What time would you like to go down the mountain? 10, 12, 14, 16: "))

    index_down = TrainDownTime.index(time_down)

    num_tickets = int(input("How many tickets will you buy? 10th ticket is free. "))
    while num_tickets > min(TrainUpTickets[index_up], TrainDownTickets[index_down]):
        num_tickets = int(input("Error. Check availability. How many tickets will you buy? 10th ticket is free: "))

    TrainUpTickets[index_up] -= num_tickets
    TrainDownTickets[index_down] -= num_tickets

    if TrainUpTickets[index_up] == 0:
        TrainUpTickets[index_up] = "Closed"
    if TrainDownTickets[index_down] == 0:
        TrainDownTickets[index_down] = "Closed"

    trip_cost = TicketCost * (num_tickets - int(num_tickets / 10))
    TrainUpMoney[index_up] = trip_cost
    TrainDownMoney[index_down] = trip_cost

    print("Your trip cost (one way) is:", trip_cost)
    print("You need to pay for both ways this amount (including the discount for more than 9 tickets):", trip_cost * 2)

    print("\nTrain Time\t\t Available Tickets\n")
    for count in range(4):
        print(f"{TrainUpTime[count]}\t\t\t{TrainUpTickets[count]}\t\t")
        print(f"{TrainDownTime[count]}\t\t\t{TrainDownTickets[count]}\t\t")

    selling_tickets = input("Buy Tickets? (yes or no): ")

for count in range(4):
    if TrainUpTickets[count] == "Closed":
        TrainUpTickets[count] = 0
    if TrainDownTickets[count] == "Closed":
        TrainDownTickets[count] = 0

passenger_up = [0] * 4
passenger_down = [0] * 4
total_passenger = 0
for count in range(3):
    passenger_up[count] = 480 - TrainUpTickets[count]
    print(f"Trip time: {TrainUpTime[count]}, had this number of passengers: {passenger_up[count]}")
    total_passenger += passenger_up[count]

    passenger_down[count] = 480 - TrainDownTickets[count]
    print(f"Trip time: {TrainDownTime[count]}, had this number of passengers: {passenger_down[count]}")
    total_passenger += passenger_down[count]

passenger_up[3] = 480 - TrainUpTickets[3]
print(f"Trip time: {TrainUpTime[3]}, had this number of passengers: {passenger_up[3]}")
total_passenger += passenger_up[3]

passenger_down[3] = 480 - TrainDownTickets[3]
print(f"Trip time: {TrainDownTime[3]}, had this number of passengers: {passenger_down[3]}")
total_passenger += passenger_down[3]

print(f"Total passengers today: {total_passenger}")

total_money_taken = 0.0
for count in range(4):
    total_money_taken += TrainUpMoney[count]
    total_money_taken += TrainDownMoney[count]

print("Total Money collected:", total_money_taken)
