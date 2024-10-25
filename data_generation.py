import pandas as pd
import numpy as np
import random

def random_dates(start, end, n=10):
    start_u = start.value // 10**9
    end_u = end.value // 10**9
    return [pd.to_datetime(np.random.randint(start_u, end_u), unit='s').strftime('%d/%m/%Y') for _ in range(n)]

def format_phone_number():
    return f'{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'