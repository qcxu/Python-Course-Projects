__author__ = 'QiongchengXu'

tran_fee = 0.02
start_price = float(input("What is the starting price per share in dollars? "))
share = int(input("How many shares do you want to buy? "))
start_value = start_price * share
charge = start_value * (1 + tran_fee)
print("The starting value of this stock is: ")
print start_value
print("You will be charged")
print charge
print("dollars after the commission.")

end_price = float(input("What is the ending price per share in dollars? "))
end_value = end_price * share
receive = end_value * (1 - tran_fee)
profit = receive - charge
increase = profit / charge * 100

print("The ending value of this stock is")
print end_value
print("and you will receive")
print receive
print("dollars after the commission.")
print("Your profit is")
print profit
print("dollars, for a")
print increase
print("percent increase in value")

