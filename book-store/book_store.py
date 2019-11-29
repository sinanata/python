from collections import Counter

PRICE = 800

PRICE_PER_GROUP = {
    1: 1 * PRICE * 1.00,
    2: 2 * PRICE * 0.95,
    3: 3 * PRICE * 0.90,
    4: 4 * PRICE * 0.80,
    5: 5 * PRICE * 0.75,
}

def total(basket):
    if not basket:
        return 0

    books_collection = Counter(basket)
    prices = [PRICE * len(basket)]

    for max_group_size in range(2, len(books_collection) + 1):
        remaining_books_in_collection = books_collection.copy()
        prices.append(0)
        while remaining_books_in_collection:
            books_group_collection = Counter(b[0] for b in remaining_books_in_collection.most_common(max_group_size))
            prices[max_group_size - 1] += PRICE_PER_GROUP[len(books_group_collection)]
            remaining_books_in_collection -= books_group_collection

    return min(prices)

    pass
