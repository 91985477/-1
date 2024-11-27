def calculate_required_capital(salary: float, spend: float, increase: float, months: int) -> int:
    money_capital = 0
    current_spend = spend

    for month in range(months):
        # Расходы текущего месяца
        if month > 0:
            current_spend *= (1 + increase)

        # Покрываем расходы зарплатой
        remaining_spend = current_spend - salary

        # Если зарплаты не хватает, используем подушку безопасности
        if remaining_spend > 0:
            money_capital += remaining_spend

    return round(money_capital)

# Параметры
salary = 50000  # Ежемесячная зарплата
spend = 60000  # Ежемесячные расходы
increase = 0.03  # Рост цен (5%)
months = 10  # Количество месяцев

# Рассчитаем необходимую подушку безопасности
required_capital = calculate_required_capital(salary, spend, increase, months)
print(f"Необходимая подушка безопасности: {required_capital} руб.")
