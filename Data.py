import csv
import numpy as np
import os
import random

MORNING_BUSY_HOUR_START = 7
MORNING_BUSY_HOUR_END = 10

EVENING_BUSY_HOUR_START = 17
EVENING_BUSY_HOUR_END = 19

def generate_time() -> int:
    is_busy: bool = bool(random.randint(0,1))
    day_time: bool = bool(random.randint(0,1)) # True - утро; False - вечер
    if is_busy and day_time:
        return random.randint(MORNING_BUSY_HOUR_START, MORNING_BUSY_HOUR_END)
    elif is_busy and not day_time:
        return random.randint(EVENING_BUSY_HOUR_START, EVENING_BUSY_HOUR_END)
    else:
        return random.randint(11, 16)
        
def generate_k():
    with open('C:\\Users\\Dmitry\\Desktop\\Комфорт\\pass_cvs.csv') as file:
        reader = csv.reader(file, delimiter=';')
        for i in reader:
            print(i)

x_dataset = np.zeros((1000, 9), dtype=int)
y_dataset = np.zeros((1000, 1), dtype=int)

generate_k()

# for i,el in enumerate(x_dataset):
#     print("Start")

