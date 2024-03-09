from tabulate import tabulate

def showInitMeasures(measures):
    headers = ['','Uso', 'Ocio', 'Total']
    table = [[
        'Cola', 
        measures.use_queue, 
        measures.leisure_queue,
        measures.use_queue + measures.leisure_queue
    ], [
        'Servicio',
        measures.use_service,
        measures.leisure_service,
        measures.use_service + measures.leisure_service
    ]]

    print(tabulate(table, headers, tablefmt='simple'))