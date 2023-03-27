from sys import argv

#  Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
#  Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
#  Для простоты договоримся, что год может быть в диапазоне [1, 9999].
#  Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
#  Проверку года на високосность вынести в отдельную защищённую функцию.

# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

__all__ = ['_gregorian_year', 'is_date']

def _gregorian_year(year: int) ->bool:
    if year % 400 ==0:
        return True
    elif year % 100 == 0:
        return False 
    elif year % 4 == 0:
        return True
    else:
        return False
    
def is_date(date: str) -> bool:
    day = date.split('.')[0]
    month = date.split('.')[1]
    year = date.split('.')[2]
    if month in ['01', '03', '05', '07', '08', '10', '12'] and 1 <= int(day) <= 31 and 1 <= int(year) <= 9999:
        return True
    elif month in ['04', '06', '09', '11'] and 1 <= int(day) <= 30 and 1 <= int(year) <= 9999:
        return True
    elif month == '02' and 1 <= int(day) <= 28 and 1 <= int(year) <= 9999 and not _gregorian_year(int(year)) or \
         month == '02' and 1 <= int(day) <= 29 and 1 <= int(year) <= 9999 and _gregorian_year(int(year)):
        return True 
    else:
        return False 
        
    

if __name__ == '__main__':
    name, date = argv
    #date = input("Введите дату в формате DD.MM.YYYY: ")       # python task1_2.py 25.03.2023
    print(is_date(date))                                       # True     
