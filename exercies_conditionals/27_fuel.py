def total_cost(litres, price_per_litre):
    litres_dicount = litres // 2
    max_dicount = min(25, litres_dicount * 5)
    total = litres * price_per_litre - max_dicount
    cost_in_dollars = total / 100
    return f"{cost_in_dollars:.2f} {'dollar' if cost_in_dollars <= 1 else 'dollars'}"
