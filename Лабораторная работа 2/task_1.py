money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital + salary
count = 0
while spend < budget:
    count += 1
    budget -= spend
    budget += salary
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", count)
