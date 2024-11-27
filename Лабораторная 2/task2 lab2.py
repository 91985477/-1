import random

def flip_coin(num_flips):
    heads = 0
    tails = 0

    for _ in range(num_flips):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1

    return heads, tails

def analyze_coin_flips(flip_counts):
    results = []

    for num_flips in flip_counts:
        heads, tails = flip_coin(num_flips)
        ratio = min(heads, tails) / max(heads, tails)
        results.append((num_flips, heads, tails, ratio))

    return results

# Количество подбрасываний для экспериментов
flip_counts = [10, 100, 1000, 10000, 100000, 1000000]

# Проведение экспериментов
results = analyze_coin_flips(flip_counts)

# Вывод результатов
for num_flips, heads, tails, ratio in results:
    print(f"Подбрасываний: {num_flips}, Орлов: {heads}, Решек: {tails}, Соотношение: {ratio:.4f}")
