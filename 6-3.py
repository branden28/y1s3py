def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split(',')
            name = parts[0].strip()
            gender = parts[1].strip().upper()
            age = int(parts[2].strip())
            income = int(parts[3].strip()) 
            data.append([name, gender, age, income])

    return data


def print_entries(data):
    for entry in data:
        print(*entry)

def print_females(data):
    for index, entry in enumerate(data):
        if entry[1] == 'F':
            print(f"[{index}] {entry[0]}")

def find_richest(data):
    richest_male = ('', 0)
    richest_female = ('', 0)
    
    for entry in data:
        name, gender, age, income = entry
        if gender == 'M' and income > richest_male[1]:
            richest_male = (name, income)
        elif gender == 'F' and income > richest_female[1]:
            richest_female = (name, income)
    
    print(f'The richest man is {richest_male[0]} with income {richest_male[1]}')
    print(f'The richest woman is {richest_female[0]} with income {richest_female[1]}')

def calculate_means(data):
    total_age = sum(entry[2] for entry in data)
    total_income = sum(entry[3] for entry in data) 
    count = len(data)

    mean_age = round(total_age / count, 1)
    mean_income = round(total_income / count, 1)

    print(f'Mean age = {mean_age}')
    print(f'Mean incomes = {mean_income}')


def compute_median_income(data):
    incomes = sorted(entry[3] for entry in data)
    n = len(incomes)
    median = (incomes[n//2] if n % 2 == 1 else (incomes[n//2 - 1] + incomes[n//2]) / 2)
    print(f"Incomes:")
    print(f"Median income = {median:.1f}")
    print(f"Max = {max(incomes):.1f}, Min = {min(incomes):.1f}")

file_path = 'A2_input.csv'
entries = read_csv(file_path)
print_entries(entries)
print_females(entries)
find_richest(entries)
calculate_means(entries)
compute_median_income(entries)
