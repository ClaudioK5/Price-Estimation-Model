def decide_price_strategy(elasticity, current_price):

    if elasticity > -1:

        new_price = current_price * 1.02

        return new_price

    elif elasticity == -1:

        new_price = current_price

        return new_price

    else:

        current_price = current_price*0.98

        return current_price

