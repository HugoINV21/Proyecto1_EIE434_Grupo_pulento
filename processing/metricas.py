import numpy as np

def calcular_IAE(errores, dt):
    return np.sum(np.abs(errores)) * dt
    
def calcular_ISE(errores, dt):
    return np.sum(np.square(errores)) * dt

def calcular_ITAE(errores, dt):
    t = np.arange(len(errores)) * dt
    return np.sum(t * np.abs(errores)) * dt

def calcular_ITSE(errores, dt):
    t = np.arange(len(errores)) * dt
    return np.sum(t * np.square(errores)) * dt

def calcular_todas_las_metricas(errores, dt):
    ise = round(calcular_ISE(errores, dt), 2)
    iae = round(calcular_IAE(errores, dt), 2)
    itse = round(calcular_ITSE(errores, dt), 2)
    itae = round(calcular_ITAE(errores, dt), 2)
    resultados = {
        "ISE": ise,
        "IAE": iae,
        "ITSE": itse,
        "ITAE": itae
    }
    
    return resultados

def calcular_mejora(valor_ppo, valor_mask):
    porcentaje = ((valor_ppo - valor_mask) / valor_ppo) * 100
    return round(porcentaje, 2)
