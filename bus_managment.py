import os

def available_bus(fr, to):
    with open('destination.txt', 'r') as file:
        content = file.readlines()
        available_bus = []
        found = False
        for record in content:
            data = record.rstrip('\n').split('#')
            if data[0:2] == [fr, to]:
                found = True
                available_bus.append(data)

    if found:

        print('-'*34)
        print("|{:^10s}|{:^10s}|{:^10s}|".format("From: ", "To: ", "Time: "))
        print('-'*34)

        for bus in available_bus:
            print("|{:^10s}|{:^10s}|{:^10s}|".format(fr, to, bus[2]))
        print('-'*34)

        return True, available_bus

    else:

        print("No Buses Found!")

        return False, None


def book(bus, number):
    name = input("Enter Your Name: ")
    phonen = input("Enter Your Phone Number: ")
    gender = input("Enter YOur Gender: ")
    amount = int(bus[4]) * number
    detail = open("detail.txt", 'a')

    detail.write(name + '#' + phonen + '#' + gender + '\n')

    detail.close()

    with open("destination.txt", 'r') as file:
        new = open("new.txt", 'w')
        content = file.readlines()
        for record in content:
            data = record.rstrip('\n').split('#')
            if data == bus:
                data[3] = str(int(data[3]) + number)
                new.write('#'.join(data) + '\n')
            else:
                new.write(record)
        new.close()
    os.remove("destination.txt")
    os.rename("new.txt", "destination.txt")
    ans = input("Do you want to print the bill? (y/n): ")
    if ans == 'y':
        print('-'*30)
        print("{:^30s}".format("Ticket Bill"))
        print('-'*30)
        print("{:^15s}{:^15s}".format("Ticket Num:", "Price: "))
        print("{:^15d}{:^15s}".format(number, bus[4]))
        print("{:^15s}{:^15d}".format("Total", amount))
        print('-'*30)
def main():
    fr = input("From: ")
    to = input("To: ")
    con, bus_list = available_bus(fr, to)
    if con:
        found = False
        t = input("Enter Time: ")
        for i in bus_list:
            if t in i:
                found = True
                bus = i
        if found:
            number = int(input("Enter Number Of Tickets: "))
            if number + int(bus[3]) <= 50:
                ans = input("Seats Available. Do you want to book? (y/n) ")
                if ans == 'y':
                    book(bus, number)
            else:
                print("No Seats Available!")
        else:
            print("Wrong Time! ")
    else:
        print("No Busses Found!")
main()