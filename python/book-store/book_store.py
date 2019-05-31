def total(basket):
    PRICE_PER_BOOK = 800

    book_sets = [set()]
    for book in basket:
        book_added = False
        for book_set in book_sets:
            if book not in book_set:
                book_set.add(book)
                book_added = True
                break
        if not book_added:
            book_sets.append(set([book]))

    total_cost = 0

    # IT's NOT THAT SIMPLE. YOU HAVE TO FIND THE MAXIMUM DISCOUNT YEESH
    # add books to smallest set? 

    # Options:
    #  * keep list of "candidate" sets that have a slot, add it to the smallest
    #    one.
    #  * find number of repeated books.... those must not be in the same set.
    #    Highest number of repeated books will give the minimum number of sets
    #    we need... true but unhelpful

    # JUST GOING TO MAKE CANDIDATE LIST FOR NOW. I'll see if there's a more
    # elegant solution after submitting this one

    for book_set in book_sets:
        num_from_set = len(book_set)
        cost_from_this_set = num_from_set * PRICE_PER_BOOK 
        discount = 0
        if num_from_set == 2:
            discount = 0.05
        elif num_from_set == 3:
            discount = 0.1
        elif num_from_set == 4:
            discount = 0.2
        elif num_from_set == 5:
            discount = 0.25
        cost_from_this_set *= (1 - discount)
        total_cost += cost_from_this_set
    
    return total_cost
