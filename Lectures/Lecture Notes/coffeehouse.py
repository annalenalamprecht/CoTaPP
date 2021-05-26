import time
import random
import threading
import multiprocessing

# function mimicking the standard process at a coffeehouse table
def table(number):
    print(f"Table {number}: Guests arrive.")
#    time.sleep(2)
    print(f"Table {number}: Guests study menu.")
 #   time.sleep(3)
    print(f"Table {number}: Guests order drinks.")
  #  time.sleep(5)
    print(f"Table {number}: Guests receive drinks.")
   # time.sleep(1)
    print(f"Table {number}: Guests order food.")
   # time.sleep(10)
    print(f"Table {number}: Guests receive food.")
  #  time.sleep(1)
    print(f"Table {number}: Guests consume.")
  #  time.sleep(15)
    print(f"Table {number}: Guests pay.")
   # time.sleep(1)
    print(f"Table {number}: Guests leave.")

# main program

tables = [x for x in range(1,21)]

cpus = multiprocessing.cpu_count()

with multiprocessing.Pool(processes=cpus) as pool:
    pool.map(table, tables)




# starttime = time.time()
# table(1)
# time.sleep(random.randint(0,5))
# table(2)
# time.sleep(random.randint(0,5))
# table(3)
# endtime = time.time()
# print(f"Total time elapsed: {endtime-starttime} seconds.")
# print()

# # concurrent version
# starttime = time.time()
# table1 = threading.Thread(target=table, args=(1,))
# table2 = threading.Thread(target=table, args=(2,))
# table3 = threading.Thread(target=table, args=(3,))

# table1.start()
# time.sleep(random.randint(0,5))
# table2.start()
# time.sleep(random.randint(0,5))
# table3.start()

# table1.join()
# table2.join()
# table3.join()

# endtime = time.time()
# print(f"Total time elapsed: {endtime-starttime} seconds.")

# # parallel version
# starttime = time.time()
# table1 = multiprocessing.Process(target=table, args=(1,))
# table2 = multiprocessing.Process(target=table, args=(2,))
# table3 = multiprocessing.Process(target=table, args=(3,))

# table1.start()
# time.sleep(random.randint(0,5))
# table2.start()
# time.sleep(random.randint(0,5))
# table3.start()

# table1.join()
# table2.join()
# table3.join()

# endtime = time.time()
# print(f"Total time elapsed: {endtime-starttime} seconds.")


