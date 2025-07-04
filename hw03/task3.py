import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern = r'[^0-9]'

    cleaned_phone_numbers = re.sub(pattern, '', phone_number)

    if cleaned_phone_numbers.startswith('0') and len(cleaned_phone_numbers) == 10:
        cleaned_phone_numbers = '+38' + cleaned_phone_numbers

    if cleaned_phone_numbers.startswith('380'):
        cleaned_phone_numbers = '+' + cleaned_phone_numbers


    return cleaned_phone_numbers
    



sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS:", sanitized_numbers)
  