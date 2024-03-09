import math
import output

def sequence(queue, service, n):
     # Tiempo de uso de la Cola
    use_queue = 0
    # Tiempo de uso del Servidor
    use_service = 0
    # Tiempo de ocio de Cola
    leisure_queue = 0
    # Tiempo de ocio del Servidor 
    leisure_service = 0

    for i in range(n):
        length = i + 1
        print(length)
        use_queue += queue[i]
        use_service += service[i]

    
        if length + 1 <= len(queue): 
            calculate_leisure = service[i] - queue[i + 1]

            if calculate_leisure > 0:
                leisure_queue += calculate_leisure
            else:
                leisure_service += calculate_leisure * -1

    # Tiempo promedio de Llegada
    lambd = use_queue / n
    # Tiempo promedio de Atención
    miu = use_service / n  
    # Número Promedio de Clientes en el Sistema
    L = lambd / (miu - lambd)
    # Número Promedio de Clientes en la cola
    Lq = math.pow(lambd, 2) / (miu * (miu - lambd))
    # Tiempo Promedio del sistema 
    W = L / lambd
    # Tiempo Promedio en la cola
    Wq = Lq / lambd
    # Ocupación del Sistema
    ro = lambd / miu
    # Probabilidad que este vació
    empty = 1 - ro

    initMeasures = {
        use_queue,
        use_service,
        leisure_queue,
        leisure_service,
        lambd,
        miu,
    }
    
    otherMeasures = {
        L,
        Lq,
        W,
        Wq,
        ro,
        empty
    }

    output.showInitMeasures(initMeasures)
    
    # print(f'Uso de Cola: {use_queue}')
    # print(f'Uso de Servicio: {use_service}')
    # print(f'Ocio Cola: {leisure_queue}')
    # print(f'Promedio de llegada por segundo (lambda): {lambd}')
    # print(f'Promedio de atención por petición (Miu): {miu} segundos')
    # print(f'Clientes en el sistema: {L}')
    # print(f'Clientes en la cola: {Lq}')
    # print(f'Tiempo de espera en el sistema: {W}')
    # print(f'Tiempo de espera en la cola: {Wq}')
    # print(f'Capacidad: {ro}')
    # print(f'Probabilidad que este vacío: {empty}')
    # print(measures)
            



