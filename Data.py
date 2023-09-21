import csv
import math
import numpy as np
import os
import random
import pandas as pd
import sklearn.cluster as clus

SAVE_PATH = 'path :)'

ARGS_COUNT = 5
GENERATION_COUNT = 1000

MORNING_BUSY_HOUR_START = 7
MORNING_BUSY_HOUR_END = 10

EVENING_BUSY_HOUR_START = 17
EVENING_BUSY_HOUR_END = 19 

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
    
    auto = random.randint(0,120) * random.randint(0,1)
    walk = random.randint(0,80) * random.randint(0,1)
    underground = random.randint(0,100) * ( random.randint(0,1) & random.randint(0,1) )
    trol = random.randint(0,100) * ( random.randint(0,1) & random.randint(0,1) )
    if auto == 0 and walk == 0 and underground == 0 and trol == 0:
        walk = 5
    return auto, walk, underground, trol

def main():
    x_dataset = np.zeros((GENERATION_COUNT, ARGS_COUNT), dtype=int)
    y_dataset = np.zeros((GENERATION_COUNT, 1), dtype=int)
    
    for i in range(GENERATION_COUNT):
        time = random.randint(0,23)
        day = random.randint(1,7)
        a,w,u,t = generate_transport_time()
        x_dataset[i] = np.array([generate_k(day, time), a, w, u, t])
    x_dataset[:, 0] *= 100
    x_table = pd.DataFrame(x_dataset, columns=['K', 'Auto(m)', 'Walk(m)', 'Underground(m)', 'Troleybus(m)'], dtype=float)
    print(x_table["K"].mean(), x_table["Auto(m)"].mean(), x_table["Walk(m)"].mean())
    
    means = clus.MiniBatchKMeans(5, n_init=10, random_state=0).fit(x_table)
    for i in range(GENERATION_COUNT):
        y_dataset[i] = means.predict([x_dataset[i]])
     
    y_table = pd.DataFrame(y_dataset, columns=["Answer"])
    main_p = pd.concat([x_table, y_table], axis=1)
    
    print(main_p[:50])
    
    main_p.to_csv(SAVE_PATH)

    

if __name__ == "__main__":
    main()