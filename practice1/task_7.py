import random

industries = [
    "Сельское хозяйство",
    "Легкая промышленность",
    "Тяжелая промышленность группы А",
    "Тяжелая промышленность группы Б",
    "Военно промышленный комплекс",
    "Наука",
    "Химическая промышленность"
]

num_republics = int(input("Введите количество республик: "))

republic_names = [f"Республика {i}" for i in range(1, num_republics + 1)]

industry_allocation = {}
for industry in industries:
    development_levels = ["избыточно развитые", "сбалансированно развитые", "слабо развитые"]
    allocation = [random.choice(development_levels) for _ in range(num_republics)]
    industry_allocation[industry] = allocation

print("Статистика развития по каждой из республик:")
for republic in republic_names:
    print(f"\n{republic}:")
    for industry in industries:
        print(f"{industry}: {industry_allocation[industry][republic_names.index(republic)]}")

# Самая отстающая отрасль
development_counts = {industry: 0 for industry in industries}
for industry in industries:
    for allocation in industry_allocation[industry]:
        development_counts[industry] += 1 if allocation == "слабо развитые" else 0
most_backward_industry = max(development_counts, key=development_counts.get)
backwardness_level = development_counts[most_backward_industry]
print(f"\nСамая отстающая отрасль: {most_backward_industry}")
print(f"Уровень отсталости: {backwardness_level}/{num_republics}")

# Самая развитая отрасль
development_counts = {industry: 0 for industry in industries}
for industry in industries:
    for allocation in industry_allocation[industry]:
        development_counts[industry] += 1 if allocation == "избыточно развитые" else 0
most_developed_industry = max(development_counts, key=development_counts.get)
development_level = development_counts[most_developed_industry]
print(f"\nСамая развитая отрасль: {most_developed_industry}")
print(f"Уровень развития: {development_level}/{num_republics}")

# Самая сбалансированная отрасль
development_counts = {industry: 0 for industry in industries}
for industry in industries:
    for allocation in industry_allocation[industry]:
        development_counts[industry] += 1 if allocation == "сбалансированно развитые" else 0
most_balanced_industry = max(development_counts, key=development_counts.get)
balance_level = development_counts[most_balanced_industry]
print(f"\nСамая сбалансированная отрасль: {most_balanced_industry}")
print(f"Уровень сбалансированности: {balance_level}/{num_republics}")