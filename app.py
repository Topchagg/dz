# List comprehansions  ( [] ) => [[] , [] , []] +
# OOP

# 1) [{} , {} ,{}]
# step => 1) unpack list -> filter() , for / while , {} -> items() -> tuple(key, value) ->

# 2)
# employee = [
#     {
#         "name": "John",
#         "company": "Microsoft"
#     },

#     {
#         "name": "Mike",
#         "company": "Microsoft"
#     },

#     {
#         "name": "Bob",
#         "company": "IBM"
#     },

#     {
#         "name": "Jim",
#         "company": "IBM"
#     }
# ]

# filtred_values = filter(
#     lambda el: el["name"] == "Jim" and eclerkl['company'] == "IBM", employee)

# print(list(filtred_values))
# companies = [
#     {
#         "label": "Microsoft"
#     },
#     {
#         "label": "IBM"
#     }
# ]


# def to_list(arr):
#     return list(arr)


# def filtred_employee(arr, attr, condition_value, callback=None):
#     if callback == None:
#         raise ValueError("Error")

#     return to_list(filter(lambda emp: emp[attr] == condition_value, arr))


# IBM_employee = filtred_employee(employee, "company", "IBM")
# microsoft_employee = filtred_employee(
#     employee, "company", "Microsoft", to_list)

# for company in companies:
#     if company["label"] == "Microsoft":
#         company['emloyee'] = microsoft_employee
#     else:
#         company['emloyee'] = IBM_employee

# print(companies)


# str methods
# min , max , sum
# print(type("Hello"))

# print("Hello world")
# print("Hello \nworld")
# print("Hello \tworld")
# print('I\'m')

# print("Hello"[4])

# full_name = "John Doe"

# name = full_name[:5:2]
# surname = full_name[5:]

# print(name, surname)
# print("hello  " + "world")

# useful function
# print(len("Hello"))

# password = "kir23 kir rik bob kir"
# print(len(password.strip()))
# new_str = password.strip("kir")
# print(new_str)

# string = "Goodbye world!"

# print(sting.replace("Goodbye", 'Hello'))

# print(string.startswith("Good"))
# print(string.endswith("ld!"))

# print(string[string.index("w"): string.index("!") + 1])
# print("Hello world".count("l"))
# print("Ho-Ho-Hi".find("Ho"))

# huckcuh
# word = "huckcuh"

# print(word[:2:-1])

# data = [
#     [
#         {"product_id": 1, "label": "Pepsi", "price": 23},
#         {"product_id": 2, "label": "Fanta", "price": 13},
#         {"product_id": 3, "label": "Sprite", "price": 10},
#         {"product_id": 4, "label": "Coca-Cola", "price": 11},
#         {"product_id": 5, "label": "Red bull", "price": 18},
#     ],
#     [
#         {"product_id": 6, "label": "Nuts", "price": 23},
#         {"product_id": 7, "label": "Bounty", "price": 13},
#         {"product_id": 8, "label": "Twix", "price": 10},
#         {"product_id": 9, "label": "Mars", "price": 11},
#         {"product_id": 10, "label": "Roshen", "price": 18},
#     ]
# ]

# drinks, *other = data
# print(drinks)


# print(max(drinks))
# print(*drinks)

# nums = (1, 2, 3, 4, 5, 6)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# splited_hello = [char for char in "Hello"]
# print(splited_hello)


# nums = [num * 2 for num in [2, 4, 6]]
# print(nums)

# Task
# We have a restaurant

# user = {
#     "name": "John",
#     "money" : in range(200 - 500)
# }

# Our restaurant also has a menu and staff

# It's (programm) should start with greeting from staff ("Julia , Aida , Sam (not manualy) ... glad to see you here .") , then it's send a request to =>
# John.

# After -> John may ask about menu , or go away
# if "go away"  ->  then programm send msg -> Are you sure about this ? if y/n -> y -> game over
# n -> turn back to : John may ask about menu , or go away
# if "stay here" -> John should get a menu and then if he has money he might to buy something . (search by name)
# if John hasn't any money he should "go away" but before he must to pay his bill (bill + comission)
# John might order so much food as he want (money!)


menu = {
    "dishes": [
        {"name": "Karbonara", "price": 240},
        {"name": "Pizza", "price": 300},
        {"name": "Pasta", "price": 200},
        {"name": "Salamy white", "price": 500},
    ],

    "drinks": [
        {"name": "Wine", "price": 40},
        {"name": "Cola", "price": 30},
        {"name": "7up", "price": 45},
        {"name": "Fanta", "price": 50},
    ],
}

waitress = [
    {
        "name": "Julia",
        "tips": "10%"
    },

    {
        "name": "Aida",
        "tips": "12%"
    },

    {
        "name": "transSam",
        "tips": "14%"
    },

    {
        "name": "Gaga",
        "tips": "24%"
    },
]
user = {
    'Money': 1000
}

def bought(user_choice_pos:list, money:int, i:int):
    user['Money'] = user['Money'] - menu[user_choice_pos][i]['price']
    del menu[user_choice_pos][i]
    print('Well, now u have')
    print(user["Money"])
    main_page(menu)
def ask_exit():
    user_choice = input('Are u sure?Y/N')
    match(user_choice):
        case 'Y':
            print("Okay, bye!")
            exit
        case 'N':
            print("Okay, go again!")
            main_page(menu)

def back_main():
    main_page(menu)


def main_page():
    user_choice = input('What u wanna do? Check menu?(a), or Go away (b)')
    match(user_choice):
        case 'A':
            pass

        case 'B':
           user_choice = input(' Are  u sure? Y/N')
           match(user_choice):
               case 'Y':
                   print('k')
               case 'N':
                   print('s')

def read_pos(user_choice:str):
     is_running = True
     i = -1
     while is_running:
                for key, value in menu[user_choice]:
                    i = i + 1
                    print((menu[user_choice][i]))
                  
                    is_running = False


def buy(user_choice_pos:menu, money:int ):
    print(menu, money)


def ask_buy(user_choice_pos:list):
    user_choice = input('Do u wanna buy something?(Y) Or go to main page(B)')
    match(user_choice):
        case 'Y':
            user_choice_food = input('Okay, please , write full name of position WITHOUT mistakes!:)')
            len_of = len(user_choice_pos) - 1
            i = -1
            is_running = True
            while is_running:
                i = i + 1
                if i <= len_of:
                    if (menu[user_choice_pos][i]['name']) == user_choice_food:
                        print(menu[user_choice_pos][i])
                        user_choice_check = input(f'Okay! Thats youre? If Yea and u wanna buy that please press Y if no press N. Youre money {user}')
                        is_running = False
                        match(user_choice_check):
                            case 'Y':
                                bought(user_choice_pos, user["Money"], i)
                                
                            case 'N':
                                   back_main()
        case 'B':
            main_page(menu) 

def waiters(waiters:list):
    len_waiters = len(waitress) - 1
    is_running = True
    i = - 1
    while is_running:
        i = i + 1
        if i <= len_waiters:
            print(waitress[i]['name'])
            if i == len_waiters:
                print('Theyre greetings you!')
                is_running = False

def main_page(menu:list):
    user_choice = input('What u wanna do, check Dishesh(A) drinks(B)? or quit? (Q)')
    is_running = True
    i = - 1
    match(user_choice):
        case 'A':
           user_choice_pos = 'dishes'
           read_pos(user_choice_pos)
           ask_buy(user_choice_pos)

                

        case 'B':
             user_choice_pos = 'drinks'
             read_pos(user_choice_pos)
             ask_buy(user_choice_pos)

        case 'Q':
            ask_exit()




def main():
    waiters(waitress)
    main_page(menu)

if __name__ == "__main__":
    main()