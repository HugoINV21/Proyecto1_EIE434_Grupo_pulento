import os
import matplotlib.pyplot as plt
import numpy as np

def plot_metricas(diccionario_experimentos, ambiente, ruta):
    dir_dest = "resultados_graficos"
    os.makedirs(dir_dest, exist_ok=True)

    dat_ppo = None
    dat_msk = None
    
    for clv, dats in diccionario_experimentos.items():
        if dats["ambiente"] == ambiente and dats["ruta"] == ruta:
            if dats["politica"] == "PPO":
                dat_ppo = dats
            elif dats["politica"] == "PPO-Mask":
                dat_msk = dats

    if not dat_ppo or not dat_msk:
        print(f"Advertencia: Datos incompletos para {ambiente} - {ruta}")
        return

    mets = ['ISE', 'IAE', 'ITSE', 'ITAE']
    figura, ejs = plt.subplots(1, 4, figsize=(16, 5))
    figura.suptitle(f'Índices de error — {ambiente} | {ruta}')

    etqs = ['PPO', 'PPO-Mask']
    cols = ['#377eb8', '#e41a1c'] 

    for i, met in enumerate(mets):
        vals = [dat_ppo[met], dat_msk[met]]
        ejs[i].bar(etqs, vals, color=cols, width=0.5)
        ejs[i].set_title(met, fontweight='bold')
        if i == 0:
            ejs[i].set_ylabel('Valor del Índice')

    plt.tight_layout()

    nom_arch = f"metricas_{ambiente}_{ruta}.png"
    rut_g = os.path.join(dir_dest, nom_arch)
    plt.savefig(rut_g, dpi=300) 
    plt.close()


def plot_lidar(angulos, distancias, distancias_norm):
    dir_dest = "resultados_graficos"
    os.makedirs(dir_dest, exist_ok=True)

    figura, ejs = plt.subplots(1, 2, figsize=(14, 5))

    ejs[0].scatter(angulos, distancias, c=distancias, cmap='winter') 
    ejs[0].set_title('¿A qué distancia están los objetos?\n(Eje X: Ángulo | Eje Y: Metros)')
    ejs[0].set_xlabel('Ángulo de giro (0-360°)')
    ejs[0].set_ylabel('Distancia detectada (m)')
    ejs[0].grid(True, linestyle='--', alpha=0.3)

    ejs[1].plot(angulos, distancias_norm, color='red', marker='.')
    ejs[1].set_title('Datos Normalizados\n(Lo que procesa la IA)')
    ejs[1].set_xlabel('Sectores del sensor')
    ejs[1].set_ylabel('Valor (0.0 a 1.0)')
    ejs[1].grid(True, linestyle='--', alpha=0.3)

    plt.tight_layout()
    rut_g = os.path.join(dir_dest, "mapa_lidar.png")
    plt.savefig(rut_g, dpi=300)
    plt.close()


def plot_trayectorias(x_ppo, y_ppo, x_mask, y_mask, waypoints, nombre):
    dir_dest = "resultados_graficos"
    os.makedirs(dir_dest, exist_ok=True)

    plt.figure(figsize=(8, 8))

    plt.plot(x_ppo, y_ppo, label='Trayectoria PPO', color='teal', alpha=0.7)
    plt.plot(x_mask, y_mask, label='Trayectoria PPO-Mask', color='crimson', linestyle='--')

    x_m = [pto[0] for pto in waypoints]
    y_m = [pto[1] for pto in waypoints]
    plt.scatter(x_m, y_m, marker='s', color='black', label='Waypoints (Metas)', zorder=5) 

    plt.title(f'Comparación de Navegación: Ruta {nombre.capitalize()}', fontweight='bold')
    plt.xlabel('Posición X (metros)')
    plt.ylabel('Posición Y (metros)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.4)

    plt.axis('equal') 

    rut_g = os.path.join(dir_dest, f"trayectorias_{nombre}.png")
    plt.savefig(rut_g, dpi=300)
    plt.close()
