__author__ = 'QiongchengXu'

B_BASE_CHARGE = 40
B_MILEAGE_CHARGE = 0.25
D_BASE_CHARGE = 60
D_MILEAGE_CHARGE = 0.25


def main():
    code = raw_input("Please enter the customer's classification code: ")
    rent_days = int(input("Please enter the number of days the vehicle was rented: "))
    begin_odometer = int(input("Please enter the beginning odometer reading: "))
    end_odometer = int(input("Please enter the ending odometer reading: "))
    miles = end_odometer - begin_odometer
    amount = bill(code, rent_days, miles)
    print "The classification code is:", code
    print "The number of days the vehicle was rented is:", rent_days
    print "The vehicle's odometer reading at the start of the rental period:", begin_odometer
    print "The vehicle's odometer reading at the end of the rental period:", end_odometer
    print "Number of miles driven during rental period:", miles
    print "Amount billed to customer: $", format(amount, ".2f") + "."


def bill(code, rent_days, miles):
    if code == "B":
        base = B_BASE_CHARGE * rent_days
        mileage_charge = B_MILEAGE_CHARGE * miles
        charge = base + mileage_charge
    if code == "D":
        base = D_BASE_CHARGE * rent_days
        average_mile_per_day = miles / rent_days
        if average_mile_per_day > 10:
            mile_to_charge = miles - 10 * rent_days
            mileage_charge = B_MILEAGE_CHARGE * mile_to_charge
            charge = base + mileage_charge
    return charge

main()