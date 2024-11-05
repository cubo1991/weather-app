def cambiarTemperatura(sistema):
    # En esta funcion recibimos un parametro ingresado por el usuario y devolvemos dos variables: simbolo para cambiar el simbolo que se ve en pantalla
    #y unidad para cambiar en el url que le mandamos a la api para que nos haga el cambio a la unidad correspondiente

    if sistema.upper() == 'F':
        simbolo = 'F'
        unidad = 'imperial'
        return simbolo, unidad
    
    if sistema.upper() == 'C':
        simbolo = 'C'
        unidad = 'metric'
        return simbolo, unidad