# Print the items as the search process is going on
from binary_search import binary_search


def visualise(array, search_item):
    index, updates = binary_search(array, search_item)

    for update in updates:
        low, high, mid = update
        print(array[low:high])
    print(f"**{index}**")
