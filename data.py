import pseudorandom
from scipy.stats import norm, expon

def queue_data(lambda_value, miu_value, desv_value, n_value):
    # random_exponential = pseudorandom.random_numbers(n_value)
    # random_normal = pseudorandom.random_numbers(n_value)
    random_exponential = [
        0.103545,
        0.85029,
        0.55093,
        0.75017
    ]

    random_normal = [
        0.58093,
        0.7437,
        0.25094,
        0.10345
    ]

    arrival = arrival_exp(random_exponential, lambda_value)
    attention = attention_norm(random_normal, miu_value, desv_value, n_value)
    print(arrival)
    print(attention)


def arrival_exp(random_exponential, lambda_value):
    arrival = []
    # Calcular la inversa exponencial
    arrival = expon.ppf(random_exponential, scale=1 / lambda_value)
    
    return arrival

def attention_norm(random_normal, miu_value, desv_value, n):
    attention = []
    # Calcular la inversa normal
    for i in range(n):
        value = norm.ppf(random_normal[i], loc=miu_value, scale=desv_value)

        # Restricción - Valores mayores a cero
        if value > 0:
            attention.append(value)
        else:
            attention.append(0)

    
    return attention


