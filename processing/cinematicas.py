import numpy as np


def calcular_movimiento(x, y, theta, v, omega, dt=1):
#saturacion
    v = np.clip(v,-0.8,0.8)

    #modelo cinematico
    x_nuevo=x+v*np.cos(theta)*dt
    y_nuevo=y+v*np.cos(theta)*dt
    theta_nuevo=theta + omega*dt

    return x_nuevo,y_nuevo,theta_nuevo

def distancia_al_objetivo(x,y,x_meta,y_meta):
    
        distancia=(np.sqrt((x_meta-x)**2+(y_meta-y)**2))          
        return distancia

def calcular_error_seguimiento(x_real, y_real, x_ideal, y_ideal):
    
    # Tomar el largo mínimo para evitar errores
    n = min(len(x_real), len(x_ideal))
    
    # Recortar arrays
    x_r = x_real[:n]
    y_r = y_real[:n]
    x_i = x_ideal[:n]
    y_i = y_ideal[:n]
    
    # Error punto a punto (distancia euclidiana)
    errores = np.sqrt((x_r - x_i)**2 + (y_r - y_i)**2)
    
    return errores
