import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000):
        print("Numbers have to be from 1 to 1000")
        return []
    if (quantity > (max_num - min_num + 1)):
        print("Quantity is bigger than numbers amount")
        return []

    result = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(result)


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Lottery numbers:", lottery_numbers)
