from binary_search import search

def main():
    array = [int(i) for i in input("Enter the sorted array,seperated by commas : ").split(",")]
    number = int(input("Which number needs to be found : "))
    print(search(array,number))


if __name__ == "__main__":
    main()