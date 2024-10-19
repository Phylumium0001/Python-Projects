def search(array,searched_number):
    # Find the middle of the array
    mid = len(array) // 2
    if array[mid] == searched_number:
        return searched_number
    # When the searched number is greater than the middle number
    # Use the right side of the array
    elif len(array) == 1:
        if array[0] != searched_number:
            return None
         
    elif searched_number > array[mid]:
        print(array[mid:])
        return search(array[mid:],searched_number)
    
    elif searched_number < array[mid]:
        print(array[:mid])
        return search(array[:mid],searched_number)
    
    
