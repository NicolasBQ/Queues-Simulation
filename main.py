def get_input():
    print("Ingrese el promedio de llegada a la cola en minutos: ")
    lambda_value = float(input())

    print("Ingrese el promedio de atención de la cola en minutos: ")
    miu_value = float(input())

    print("Ingrese la desviación típica de la atención a la cola en minutos: ")
    desv_value = float(input())

    print("Ingrese el número de clientes bajo el cual se realizará la simulación: ")
    n_value = int(input())

if __name__ == "__main__":
    get_input()
