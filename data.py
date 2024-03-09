import pseudorandom

def queue_data(lambda_value, miu_value, desv_value, n_value):
    random_exponential = pseudorandom.random_numbers(n_value)
    random_normal = pseudorandom.random_numbers(n_value)

    print(random_exponential)
    print(random_normal)

