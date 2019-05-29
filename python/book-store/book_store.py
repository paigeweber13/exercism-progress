def total(basket):
    PRICE_PER_BOOK = 800

    different_books = set()
    num_additional_books = 0
    for book in basket:
        if book not in different_books:
            different_books.add(book)
        else:
            num_additional_books += 1

    total_cost = 0

    # TODO: edge case where you buy a set of books twice. Each set gets a 
    # discount

    num_from_set = len(different_books)
    total_cost += num_from_set * PRICE_PER_BOOK 
    discount = 0
    if num_from_set == 2:
        discount = 0.05
    elif num_from_set == 3:
        discount = 0.1
    elif num_from_set == 4:
        discount = 0.2
    elif num_from_set == 5:
        discount = 0.25
    total_cost *= (1 - discount)
    
    total_cost += num_additional_books * PRICE_PER_BOOK
    return total_cost
