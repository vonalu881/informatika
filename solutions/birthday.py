import random

def birthday_probability(people):
    if people > 365:
        return 1.0
    if people <= 1:
        return 0.0
        
    prob_all_different = 1.0
    for i in range(people):
        prob_all_different *= (365 - i) / 365

    return 1.0 - prob_all_different

def simulate_birthday(people, trials):
    matches = 0
    
    for _ in range(trials):
        birthdays = []
        for _ in range(people):
            birthdays.append(random.randint(1, 365))
            
        if len(set(birthdays)) < people:
            matches += 1
            
    return matches / trials