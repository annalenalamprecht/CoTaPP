import time

# function mimicking the standard process at a coffeehouse table
def table(number):
print(f"Table {number}: Guests arrive.")
time.sleep(2)
print(f"Table {number}: Guests study menu.")
time.sleep(3)
print(f"Table {number}: Guests order drinks.")
time.sleep(5)
print(f"Table {number}: Guests receive drinks.")
time.sleep(1)
print(f"Table {number}: Guests order food.")
time.sleep(10)
print(f"Table {number}: Guests receive food.")
time.sleep(1)
print(f"Table {number}: Guests consume.")
time.sleep(15)
print(f"Table {number}: Guests pay.")
time.sleep(1)
print(f"Table {number}: Guests leave.")

# main program
starttime = time.time()
table(1)
time.sleep(random.randint(0,5))
table(2)
time.sleep(random.randint(0,5))
table(3)
endtime = time.time()
print(f"Total time elapsed: {endtime-starttime} seconds.")