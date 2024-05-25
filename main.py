# Функція жадібного алгоритму
def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount -= coin * count
    return result

# Функція динамічного програмування
def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    if dp[amount] == float('inf'):
        return {}
    
    result = {}
    i = amount
    while i > 0:
        coin = coin_used[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin
    
    return result

# Тестовий приклад
amount = 113
print("Результат жадібного алгоритму:", find_coins_greedy(amount))
print("Результат алгоритму динамічного програмування:", find_min_coins(amount))
