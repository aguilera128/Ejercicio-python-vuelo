# HH:mm:ss entrar y devolver en este formato

def ceroAlante(entero):
    if entero >= 0 and entero <10:
        valor = str(0)+str(entero)
    else:
        valor = str(entero)
    return valor


def tiempoLLegada (h_salida,t_vuelo):

    h_salida = h_salida.split(":")
    t_vuelo = t_vuelo.split(":")

    hora_salida = []
    tiempo_vuelo = []

    for h in h_salida:
        hora_salida.append(int(h))
        # print(hora_salida)
    for t in t_vuelo:
        tiempo_vuelo.append(int(t))
        # print(tiempo_vuelo)

    segundo_llegada = hora_salida[2] + tiempo_vuelo[2]
    minuto_llegada = hora_salida[1] + tiempo_vuelo[1]
    hora_llegada = hora_salida[0] + tiempo_vuelo[0]

    if segundo_llegada >= 60:
        segundo_llegada -= 60
        minuto_llegada += 1

    if minuto_llegada >= 60:
        minuto_llegada -= 60
        hora_llegada += 1

    if hora_llegada >= 24:
        hora_llegada -= 24

    return "Su hora de llegada es: " + ceroAlante(hora_llegada) + ":" + ceroAlante(minuto_llegada) + ":" + ceroAlante(segundo_llegada)


if __name__ == '__main__':
    h_salida = input("Introduzca la hora de salida (HH:mm:ss): \n")
    t_vuelo = input("Introduzca el tiempo de vuelo (HH:mm:ss): \n")
    print(tiempoLLegada(h_salida,t_vuelo))