import pandas as pd
import numpy as np
import statsmodels.stats.weightstats


chat_id = 964993301 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return 1-statsmodels.stats.weightstats.ztest(x,y)[1]<0.02
