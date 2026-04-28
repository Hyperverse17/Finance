
from data.databases.distributions import *
                
def portfolio_balancer(user_id:int, type:str, curr_portfolio:dict, to_add:float):
    """
    Calcula la distribución de una nueva inversión para acercarse a los pesos objetivos. 
    curr_portfolio: Diccionario con el valor actual en MXN/USD de cada activo.
    to_add: Monto total a invertir.
    """
    
    if type == "variable":
        user_objectives = get_variable_objectives(user_id)

    elif type == "fixed":
        user_objectives = get_fixed_objectives(user_id)
        
    curr_portfolio_value = sum(curr_portfolio.values())
    final_portfolio_value = curr_portfolio_value + to_add
    
    needs = {}
    distribution = {}

    # 1. Calcular cuánto debería tener cada activo para cumplir el % ideal
    # 2. Comparar con lo que ya tengo para ver el "faltante"
    for asset, weight in user_objectives.items():
        ideal_amt = final_portfolio_value * weight
        curr_amt = curr_portfolio.get(asset, 0) # Regresa 0 por defecto
        # Necesidad es lo que me falta para llegar al ideal
        needed = max(0, (ideal_amt - curr_amt)) #   Se calcula la diferencia entre el monto ideal y el real, si es negativo, regresa cero (Estrategia de no vender)
        needs[asset] = needed

    # 3. Ajustar la distribución al monto real de la nueva inversión
    total_needed = sum(needs.values()) # Se  suman todas las necesidades, esto con el fin de calcular las proporciones para saber qué activo necesita más que otro después..   
    
    if total_needed > 0:
        for asset in needs:
            # Proporcionalizamos la nueva inversión según las necesidades detectadas
            distribution[asset] = round((needs[asset] / total_needed) * to_add,2)
    
    return distribution

