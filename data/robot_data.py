import numpy as np

def cargar_experimentos():
    """
    Retorna el diccionario con los datos de las Tablas 6, 7 y 8.
    """
    experimentos = {
        # TABLA 6: Experimento simple (Métricas de Error)
        "exp1": {"politica": "PPO", "ambiente": "real", "ruta": "simple", "ISE": 434.99, "IAE": 135.93, "ITSE": 6932.79, "ITAE": 2601.61, "tiempo_s": None, "pasos": None, "reward_medio": None},
        "exp2": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "simple", "ISE": 362.85, "IAE": 128.92, "ITSE": 5869.30, "ITAE": 2669.86, "tiempo_s": None, "pasos": None, "reward_medio": None},
        "exp3": {"politica": "PPO", "ambiente": "simulado", "ruta": "simple", "ISE": 73.35, "IAE": 24.51, "ITSE": 203.90, "ITAE": 89.73, "tiempo_s": None, "pasos": None, "reward_medio": None},
        "exp4": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "simple", "ISE": 73.79, "IAE": 22.91, "ITSE": 200.16, "ITAE": 73.77, "tiempo_s": None, "pasos": None, "reward_medio": None},

        # TABLA 7: Ruta Cuadrada (Desempeño)
        "exp5": {"politica": "PPO", "ambiente": "simulado", "ruta": "cuadrada", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 27.89, "pasos": 270, "reward_medio": 7.12},
        "exp6": {"politica": "PPO", "ambiente": "real", "ruta": "cuadrada", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 112.48, "pasos": 594, "reward_medio": 3.75},
        "exp7": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "cuadrada", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 24.42, "pasos": 235, "reward_medio": 7.94},
        "exp8": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "cuadrada", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 103.46, "pasos": 569, "reward_medio": 4.13},

        # TABLA 8: Ruta Triangular (Desempeño)
        "exp9": {"politica": "PPO", "ambiente": "simulado", "ruta": "triangular", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 26.20, "pasos": 254, "reward_medio": 7.38},
        "exp10": {"politica": "PPO", "ambiente": "real", "ruta": "triangular", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 104.37, "pasos": 581, "reward_medio": 3.92},
        "exp11": {"politica": "PPO-Mask", "ambiente": "simulado", "ruta": "triangular", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 22.75, "pasos": 219, "reward_medio": 8.25},
        "exp12": {"politica": "PPO-Mask", "ambiente": "real", "ruta": "triangular", "ISE": None, "IAE": None, "ITSE": None, "ITAE": None, "tiempo_s": 116.71, "pasos": 638, "reward_medio": 4.45}
    }
    return experimentos

def generar_trayectoria_ideal(waypoints, puntos_por_segmento=100):
    """
    Genera puntos intermedios entre waypoints usando interpolación lineal.
    """
    x_ideal = []
    y_ideal = []

    # Iterar sobre pares de puntos consecutivos
    for i in range(len(waypoints) - 1):
        punto_inicio = waypoints[i]
        punto_fin = waypoints[i+1]

        # Generar puntos intermedios con linspace
        segmento_x = np.linspace(punto_inicio[0], punto_fin[0], puntos_por_segmento)
        segmento_y = np.linspace(punto_inicio[1], punto_fin[1], puntos_por_segmento)

        # Agregar a las listas usando .extend()
        x_ideal.extend(segmento_x)
        y_ideal.extend(segmento_y)

    return np.array(x_ideal), np.array(y_ideal)

def simular_lidar(n_sectores=36, d_min=0.5, d_max=30.0):
    """
    Simulación de lectura de sensor RPLIDAR S2 con detección de obstáculos.
    """
    # 1. Arreglo de ángulos de 0 a 360°
    angulos_deg = np.linspace(0, 360, n_sectores)

    # 2. Distancias aleatorias uniformes
    distancias = np.random.uniform(d_min, d_max, n_sectores)

    # 3. Simulación de Obstáculo: Índices [5:9] (incluye el 9 para cubrir el rango visual)
    distancias[5:10] = np.random.uniform(0.5, 2.0, len(distancias[5:10]))

    # 4. Normalización según fórmula d_norm = (d - d_min) / (d_max - d_min)
    distancias_norm = (distancias - d_min) / (d_max - d_min)

    return angulos_deg, distancias, distancias_norm


import matplotlib.pyplot as plt

# --- 1. Gráfica de Trayectoria ---
ruta_triangular = [[0, 0], [4, 0], [2, 4], [0, 0]]
x, y = generar_trayectoria_ideal(ruta_triangular)

plt.figure(figsize=(6, 5))
plt.plot(x, y, 'b--', label='Trayectoria Ideal')
plt.scatter([p[0] for p in ruta_triangular], [p[1] for p in ruta_triangular], color='red', label='Waypoints')
plt.title("Planificación de Ruta (Trayectoria Ideal)")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.legend()
plt.grid(True)
plt.show()

# --- 2. Gráfica Polar del LiDAR ---
angulos, distancias, _ = simular_lidar()
# Convertimos ángulos a radianes para la gráfica polar
radianes = np.deg2rad(angulos)

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(radianes, distancias, color='g', linewidth=1)
ax.fill(radianes, distancias, alpha=0.2, color='green')
ax.set_title("Simulación de Lectura LiDAR (Presencia de Obstáculo)")
plt.show()
