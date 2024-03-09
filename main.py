import data

def get_input():
    print("Ingrese el promedio de llegada a la cola en segundos: ")
    lambda_value = float(input())
    print(f'Lambda (Clientes por segundo): {lambda_value}')

    print("Ingrese el promedio de atención de la cola en segundos: ")
    miu_value = float(input())
    print(f'Miu (Respuesta en segundos por cliente): {miu_value}')

    print("Ingrese la desviación típica de la atención a la cola en segundos: ")
    desv_value = float(input())
    print(f'Desviación (Desiviación en segundos): {desv_value}')

    print("Ingrese el número de clientes bajo el cual se realizará la simulación: ")
    n_value = int(input())
    print(f'Clientes :  {n_value}')

    data.queue_data(lambda_value, miu_value, desv_value, n_value)


if __name__ == "__main__":
    get_input()
