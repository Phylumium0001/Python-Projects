
def search(array, searched_number):
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
        return search(array[mid:], searched_number)

    elif searched_number < array[mid]:
        print(array[:mid])
        return search(array[:mid], searched_number)


def binary_search(array, searched_number):
    low, high = 0, len(array) - 1
    updates = []

    while low < high:
        mid = (high + low) // 2

        # print(f"Low > {low} : High > {high} : Mid > {mid}")
        updates.append((low, high, mid))

        if array[mid] == searched_number:
            # Found the number
            return mid, updates

        elif high - low == 1:
            if array[low] == searched_number:
                return low, updates
            elif array[high] == searched_number:
                return high, updates
            break

        elif array[mid] > searched_number:
            # Shift to left
            high = mid - 1

        elif array[mid] < searched_number:
            # Shift to right
            low = mid

    return None, []
