import random 
import multiprocessing

def celsius2fahrenheit(temp):
    return (9/5) * temp + 32

temps_celsius = [random.randint(0,100) for x in range(0,25)]
print(temps_celsius)

cpus = multiprocessing.cpu_count()

with multiprocessing.Pool(processes=cpus) as pool:
    temps_fahrenheit = pool.map(celsius2fahrenheit, temps_celsius)
    
print(temps_fahrenheit)