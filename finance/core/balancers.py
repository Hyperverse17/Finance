
def get_variable_objectives(user_id:int) -> dict:
    objectives = {}
    if user_id == 1:
        objectives['S&P500'] = 0.5 # los keys deben ser idénticos a los keys de my_portfolio
        objectives['Emergentes'] = 0.4
        objectives['Oro'] = 0.1
        discriminant = sum(objectives.values())

        if discriminant != 1:
            raise ValueError
        
        return objectives
    
def get_fixed_objectives(user_id:int) -> dict:
    objectives = {}
    if user_id == 1:
        objectives['CETES'] = 0.2
        objectives['BONOS'] = 0.3
        objectives['UDIBONOS'] = 0.5
        discriminant = sum(objectives.values())

        if discriminant != 1:
            raise ValueError
        
        return objectives
        
            
def portfolio_balancer(type, curr_portfolio, to_add):
    """
    Calcula la distribución de una nueva inversión para acercarse a los pesos objetivos. 
    curr_portfolio: Diccionario con el valor actual en MXN/USD de cada activo.
    to_add: Monto total a invertir.
    """
    
    if type == "variable":
        user_objectives = get_variable_objectives(1)
    elif type == "fixed":
        user_objectives = get_fixed_objectives(1)
        
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
            distribution[asset] = (needs[asset] / total_needed) * to_add
    
    return distribution

