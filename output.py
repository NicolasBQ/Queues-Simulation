from tabulate import tabulate

def showInitMeasures(use_queue, leisure_queue, use_service, leisure_service):
    print("Resultados Iniciales de Simulación: ")
    headers = ['','Uso (s)', 'Ocio (s)', 'Total (s)', 'Porcentaje de Uso (%)']
    table = [[
        'Cola', 
        use_queue, 
        leisure_queue,
        use_queue + leisure_queue,
        (use_queue * 100)  / (use_queue + leisure_queue)
    ], [
        'Servicio',
        use_service,
        leisure_service,
        use_service + leisure_service,
        (use_service * 100) / (use_service + leisure_service)
    ], [
        'Total Simulación',
        use_queue + use_service,
        leisure_queue + leisure_queue,
        (use_queue + leisure_queue) + (use_service + leisure_service),
        ((use_queue + use_service) * 100) / ((use_queue + leisure_queue) + (use_service + leisure_service))
    ]]

    print(tabulate(table, headers, tablefmt='simple'))