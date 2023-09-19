import csv
import math
import numpy as np
import os
import random
import pandas as pd

ARGS_COUNT = 6
GENERATION_COUNT = 1000

MORNING_BUSY_HOUR_START = 7
MORNING_BUSY_HOUR_END = 10

EVENING_BUSY_HOUR_START = 17
EVENING_BUSY_HOUR_END = 19
        
def generate_auto_business(time: int) -> int:
    if (MORNING_BUSY_HOUR_START <=  time <= MORNING_BUSY_HOUR_END) or (EVENING_BUSY_HOUR_START <=  time <= EVENING_BUSY_HOUR_END):
        return random.randint(6,10)
    else:
        return random.randint(1,5)

def time_function(x: int) -> float:
    k = (-abs( (0.6*x + 8)**2 - 20*x)) + 12
    return k if k >= 0 else 0.1

def day_of_week_function(x: int) -> float:
    return abs(-math.tanh(x-6.2))

def generate_k(day_of_week_number: int, time: int) -> float:
    return time_function(time) * day_of_week_function(day_of_week_number)

def generate_transport_time():
    # сколько видов транспорта будет
    # transport_counter = random.randint(1,4)
    
    auto = random.randint(0,180) * ( random.randint(0,1) & random.randint(0,1) )
    walk = random.randint(0,80) * ( random.randint(0,1) & random.randint(0,1) )
    underground = random.randint(0,100) * ( random.randint(0,1) & random.randint(0,1) )
    trol = random.randint(0,100) * ( random.randint(0,1) & random.randint(0,1) )
    
    return auto, walk, underground, trol

x_dataset = np.zeros((GENERATION_COUNT, ARGS_COUNT), dtype=int)
y_dataset = np.zeros((GENERATION_COUNT, 1), dtype=int)

for i in range(GENERATION_COUNT):
    time = random.randint(0,23)
    day = random.randint(1,7)
    a,w,u,t = generate_transport_time()
    x_dataset[i] = np.array([generate_k(day, time), a, w, u, t, generate_auto_business(time)])

table = pd.DataFrame(x_dataset, columns=['K', 'Auto(m)', 'Walk(m)', 'Underground(m)', 'Troleybus(m)', 'Road business'])
print(table)
# print(np.average( table["Auto(m)"]))