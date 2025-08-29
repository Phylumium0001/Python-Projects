# URL shortening service
from utils.normalize import normalize_url
from utils.hash_url import generate_hash_value
from utils.generate_short_url import generate_url
from utils.user_id import generate_user_id
from utils.database import Database


def add_new_url(url, db_obj, add_user_id=False):
    # Normalize
    normalized_url = normalize_url(url)

    # Hash and obtain key
    hash_value = generate_hash_value(normalized_url)

    if add_user_id:
        # Add user id to url
        # Get User_id
        user_id = generate_user_id()

        # Generate short Url
        short_url = generate_url(hash_value, user_id)

    else:
        short_url = generate_url(hash_value)

    print(short_url)

    # Store in Db
    db_obj.add_new_url(short_url, url)


def expand_url(short_url, db_obj):
    # Retrieve the url representation from the db
    try:
        corresponding_link = db_obj.find_url(short_url)
        print(corresponding_link)
    except Exception as e:
        print(e)


def show_all_urls(db_obj):
    res = db_obj.show_all_urls()
    print("Shorten links > Original Links")
    for url in res:
        print(f"{url[0]} > {url[1]}")


if __name__ == "__main__":
    print("Welcome to the Url Shortening Service")
    db_obj = Database()

    while True:
        response = input(
            "[1] Shorten link\n[2] Expand link\n[3] Show database \n[4] Quit\n> ")

        if response == "1":
            url = input("Enter Url > ")
            add_new_url(url, db_obj)

        elif response == "2":
            short_url = input("Enter short Url > ")
            try:
                url = expand_url(short_url, db_obj)
            except Exception as e:
                url = None
                print(e)
            print(url)

        elif response == "3":
            show_all_urls(db_obj)

        elif response == "4":
            break

        else:
            print("Dont know what you are saying")
