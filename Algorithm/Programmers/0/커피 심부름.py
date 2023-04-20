AMERICANO = "americano"
LATTE = "cafelatte"

coffee_price = {AMERICANO: 4500, LATTE: 5000}


def solution(order: list) -> int:
    answer = 0
    orders = order

    for order in orders:
        answer += get_price_form_menu(order)

    return answer


def get_price_form_menu(menu: str) -> int:
    if menu.startswith(AMERICANO) or menu.endswith(AMERICANO):
        return coffee_price[AMERICANO]
    elif menu.startswith(LATTE) or menu.endswith(LATTE):
        return coffee_price[LATTE]

    return coffee_price[AMERICANO]
