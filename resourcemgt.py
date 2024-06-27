MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0
}

def calculate_value(quarters, dimes, nickels, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

def calculate_coins(dollars):
    quarters = round(dollars // 0.25)
    left = dollars % 0.25
    dimes = round(left // 0.1)
    left = left % 0.1
    nickels = round(left // 0.05)
    left = left % 0.05
    pennies = round(left // 0.01)
    return quarters, dimes, nickels, pennies