from datetime import datetime

def get_date():
    
    while True:
        
        date_input = input("Введите дату в формате DD.MM.YYYY: ")
        
        try:
            parsed_date = datetime.strptime(date_input, "%d.%m.%Y")
            return parsed_date
            
        except ValueError:
            print("Ошибка: неверный формат даты. Убедитесь, что используете формат DD.MM.YYYY и вводите только цифры. Попробуйте снова.")

def calculate_days_difference(date1, date2):
    

    difference = date2 - date1
    days = difference.days
    
    if days < 0:
        days = days * -1
    return days

print("Введите первую дату:")
Date_1 = get_date()
print("Введите вторую дату:")
Date_2 = get_date()
result = calculate_days_difference(Date_1, Date_2)

print("Абсолютная разница в днях между второй и первой датой:", result, "дней")