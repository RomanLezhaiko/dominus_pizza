""" 
4. #classmethod #dataclass
* Пиццерии Dominus требуется написать программу, которая способна осуществлять 
заказ пицц из их фирменной коллекции(пока что там только два варианта) либо же 
покупатель может сам указать, какие из ингредиентов предложенных пиццерией добавить,
чтобы получилось все как покупатель любит. Пиццы характеризуются ингридентами
и диаметром, от этого будет зависеть и цена. Заказ может состоять из нескольких пицц.
Денег у пиццерии хватает только на консольное приложение.
"""
from  sys import stdin
from dataclasses import dataclass

menu_message = 'Введите 1 для заказа пиццы. Введите 2 для выхода из приложения.'
choice_message = """Введите 1 для заказа пиццы Pepperoni. Введите 2 для заказа пиццы Branded.
Введите 3 для заказа пиццы Custom(c выбором ингридиентов по вкусу). Введите 4 для завершения заказа"""
size_message = """Введите 1 для заказа маленькой пиццы. Введите 2 для заказа средней пиццы.
Введите 3 для заказа большой пиццы. Введите 4 для заказа семейной пиццы"""
count_message = """Сколько пицц Вы хотите заказать? Введите число."""
hello_message = f"""Вас приветствует пиццерия Dominus!
{menu_message}"""
error_message = f"""Такой команды не существует!
{menu_message}"""
print(hello_message)


@dataclass
class Ingredients():
    base: float = 13.25
    meat: float = 1.99
    chiken: float = 1.57
    tomato: float = 0.89
    mushrooms: float = 0.99
    pepper: float = 0.95
    bacon: float = 3.23
    chilli: float = 2.10
    cheese: float = 1.56


@dataclass
class Pizzas():
    pepperoni: float = 25.56
    branded: float = 30.91
    

@dataclass
class Sizes():
    small_size: float = 0.6
    middle_size: float = 0.75
    large_size: float = 1.0
    family_size: float = 1.3


class User(object):
    """
    Class User
    
    Creates an instance of a User class
    """
    def __init__(self) -> None:
        """ 
        __init__ function
        
        :param self: self object of class
        :returns: return None 
        """
        self.__name = ''
        self.__phone_number = ''
        self.__adress = ''
        self.__summ = 0.0
        self.__cart = ''
    
       
    def get_name(self) -> str:
        """ 
        Get name function
        
        :param self: self object of class
        :returns: return str
        """
        return f'{self.__name}'
    
    
    def set_name(self, name) -> None:
        """ 
        Set name function
        
        :param self: self object of class
        :param name: name of object
        :returns: return None
        """
        self.__name = name
    
    
    def get_phone_number(self) -> str:
        """ 
        Get phone_number function
        
        :param self: self object of class
        :returns: return str
        """
        return f'{self.__phone_number}'
    
    
    def set_phone_number(self, phone_number) -> None:
        """ 
        Set phone_number function
        
        :param self: self object of class
        :param phone_number: phone_number of object
        :returns: return None
        """
        self.__phone_number = phone_number
    
    
    def get_adress(self) -> str:
        """ 
        Get adress function
        
        :param self: self object of class
        :returns: return str
        """
        return f'{self.__adress}'
    
    
    def set_adress(self, adress) -> None:
        """ 
        Set adress function
        
        :param self: self object of class
        :param adress: adress of object
        :returns: return None
        """
        self.__adress = adress
    
    
    def get_summ(self) -> str:
        """ 
        Get summ function
        
        :param self: self object of class
        :returns: return str
        """
        return f'{self.__summ}'
    
    
    def set_summ(self, summ) -> None:
        """ 
        Set summ function
        
        :param self: self object of class
        :param summ: summ of object
        :returns: return None
        """
        self.__summ += summ
    
    
    def get_cart(self) -> str:
        """ 
        Get cart function
        
        :param self: self object of class
        :returns: return str
        """
        return f'{self.__cart}'
    
    
    def set_cart(self, pizza, size, count) -> None:
        """ 
        Set cart function
        
        :param self: self object of class
        :param cart: cart of object
        :returns: return None
        """
        cart_tmp = pizza + ',' + str(size) + ',' + str(count) + '\n'
        self.__cart += cart_tmp
    
    
    # @classmethod
    # def custom_pizza(cls, ingredients, size, count):
    #     summ = ingredients.base
    #     summ += ingredients.meat
    #     summ *= size.small_size
    #     cls.set_summ(user, summ)
    
    
    @classmethod
    def pizza_1(cls, pizzas, size, count):
        summ = pizzas.pepperoni * count * size
        summ_str = '%.2f' % summ
        cls.set_summ(user, float(summ_str))
        cls.set_cart(user, 'Pepperoni', size, count)
    
    
    @classmethod
    def pizza_2(cls, pizzas, size, count):
        summ = pizzas.branded * count * size
        summ_str = '%.2f' % summ
        cls.set_summ(user, float(summ_str))
        cls.set_cart(user, 'Branded', size, count)
    
    
    name = property(get_name, set_name)
    phone_number = property(get_phone_number, set_phone_number)
    adress = property(get_adress, set_adress)
    summ = property(get_summ, set_summ)
    cart = property(get_cart, set_cart)


def choice_size() -> float:
    flag_exit = False
    size = 0.0
    print(size_message)
    while not flag_exit:
        for line in stdin:
            line = line.strip()
            if line == '1':
                size = Sizes.small_size
                break
            elif line == '2':
                size = Sizes.middle_size
                break
            elif line == '3':
                size = Sizes.large_size
                break
            elif line == '4':
                size = Sizes.family_size
                break
            else:
                print('Такого размера не существует!', size_message, sep='\n')
        flag_exit = True
    
    return size


def choice_count() -> int:
    flag_exit = False
    count = 0
    print(count_message)
    while not flag_exit:
        for line in stdin:
            line = line.strip()
            if line.isdigit():
                count = int(line)
                break
            else:
                print('Вы ввели не число!', count_message, sep='\n')
        flag_exit = True
    
    return count


def make_order() -> None:
    flag_exit = False
    print(choice_message)
    while not flag_exit:
        for line in stdin:
            print(user.get_summ())
            print(user.get_cart())
            line = line.strip()
            if line == '1':
                user.pizza_1(pizzas=Pizzas, size=choice_size(), count=choice_count())
            elif line == '2':
                user.pizza_2(pizzas=Pizzas, size=choice_size(), count=choice_count())
            elif line == '3':
                size = choice_size()
                count = choice_count()
            elif line == '4':
                flag_exit = True
                break
            else:
                print('Такой команды не существует!')
            
            print(choice_message)
            
    print(menu_message)


user = User()
for line in stdin:
    line = line.strip()
    if line == '1': 
        make_order()
    elif line == '2':
        break
    else:
        print(error_message)