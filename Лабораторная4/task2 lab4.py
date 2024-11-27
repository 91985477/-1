def calculate_months_without_debt(money_capital: float, salary: float, spend: float, increase: float) -> int:
    current_spend = spend
    months = 0

    while money_capital >= 0:
        # Увеличиваем расходы на 5% каждый месяц, начиная со второго месяца
        if months > 0:
            current_spend *= (1 + increase)

        # Покрываем расходы зарплатой
        remaining_spend = current_spend - salary

        # Если зарплаты не хватает, используем подушку безопасности
        if remaining_spend > 0:
            money_capital -= remaining_spend
        else:
            money_capital -= current_spend

        # Увеличиваем счетчик месяцев
        months += 1

        # Если подушка безопасности закончилась, выходим из цикла
        if money_capital < 0:
            break

    return months

# Параметры
money_capital = 100000  # Финансовая подушка безопасности
salary = 50000  # Ежемесячная зарплата
spend = 60000  # Ежемесячные расходы
increase = 0.05  # Рост цен (5%)

# Рассчитаем количество месяцев без долгов
months_without_debt = calculate_months_without_debt(money_capital, salary, spend, increase)
print(f"Количество месяцев без долгов: {months_without_debt}")
