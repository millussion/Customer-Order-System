def calculate_total_sales(orders):
    total_day = sum(order[3] for order in orders.values())
    return f"Total sales of the day: ${int(total_day):,}"