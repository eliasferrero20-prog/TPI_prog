#Programar funciones.
def costo_A(x):
    return 40* x + 200
def costo_B(x):
    return 70* x + 50
def costo_C(x):
    return -2* (x**2) + 80* x +100

#Plan más económico para un valor de x
def determinar_mejor_plan(x):
    val_A = costo_A(x)
    val_B = costo_B(x)
    val_C = costo_C(x)
    if val_A <= val_B and val_A <= val_C:
        return "Plan A"
    elif val_B <= val_A and val_B <= val_C:
        return "Plan B"
    else:
        return "Plan C"

#Evaluar las funciones para los valores
valores_x = [0, 5, 10, 15, 20, 25, 30, 40, 50]
print("X (Horas) | Costo A  | Costo B  | Costo C  | Plan Más Económico")
for i in range(9):
    x_actual = valores_x[i]
    cA = costo_A(x_actual)
    cB = costo_B(x_actual)
    cC = costo_C(x_actual)
    mejor_plan = determinar_mejor_plan(x_actual)
    print(x_actual, "\t  | $", cA, "\t | $", cB, "\t| $", cC, "\t|", mejor_plan)

#Graficar en el intervalo dado (0 <= x <= 50)
import matplotlib.pyplot as plt
import numpy as np

x_grafico = np.linspace(0, 50, 500)
y_A = costo_A(x_grafico)
y_B = costo_B(x_grafico)
y_C = costo_C(x_grafico)
plt.plot(x_grafico, y_A, color="blue", linewidth=2, label="A(x) = 40x + 200")
plt.plot(x_grafico, y_B, color="green", linewidth=2, label="B(x) = 70x + 50")
plt.plot(x_grafico, y_C, color="red", linewidth=2, label="C(x) = -2x² + 80x + 100")
plt.scatter(valores_x, [costo_A(i) for i in valores_x], color="black", zorder=5)
plt.title("Análisis Comparativo de Planes de Software (UTN)", fontsize=12, fontweight="bold")
plt.xlabel("Horas Utilizadas Mensualmente (x)")
plt.ylabel("Costo Mensual en $ (y)")
plt.xlim(0, 50)
plt.ylim(0, 1000)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.show()