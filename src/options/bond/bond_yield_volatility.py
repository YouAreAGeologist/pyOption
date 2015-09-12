def get_bond_yield_volatility_from_price(sigma_p, y, duration):
    return sigma_p / (y * (duration / (1 + y)))


def get_bond_yield_volaility_from_bond_yield(sigma_y, y, duration):
    return sigma_y * (y * (duration / (1 + y)))
