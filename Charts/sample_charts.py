#ESTO ES UN MÓDULO, puedes ejecutarlo en main.py

import matplotlib.pyplot as plt #Uso de pyplot

def generate_PIE_chart():
    labels = ["A","B","C"]
    values = [100,200,200]
    #Paara generar la grafica, obtenemos la figura y las cordenadas desde matplotlib
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #Podriamos indicarle despues que queremos ver la gráfica con plt.show() pero en esta ocasion queremos generar una imagen para que el programa no se atore aqui simplemente 

    #Le indicaremos que genere la grafica y lo guarde en un archivo como tal
    plt.savefig("pie.png")
    plt.close()


#Lo que va en main como script de ejecución es lo siguiente:
#Script que prueba el modulo "Sample" para generar charts
import sample_charts as sch

def run():
    """
    ACTUALIZA en formato png la gráfica de pastel o circular al ejecutarse
    """
    sch.generate_PIE_chart()

if __name__ == "__main__":
    run()

