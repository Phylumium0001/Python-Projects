
def generate_url(hash, user_id=False):
    # Forms the short url
    # domain/xhh-xhh-xhh-xhh
    url = "shlk.com/"

    # Seperate hash into four chunks
    # Get first 8 chars of hash
    hash_part = hash[:9]
    hash_chunks = [hash_part[0:3], hash_part[3:6], hash_part[6:]]

    if user_id:
        # Use user_id

        # This includes the user id to the short url
        for id, chunk in zip(list(user_id), hash_chunks):
            if url == "shlk.com/":
                url += f"{id}{chunk}"
                continue

            url += f"-{id}{chunk}"

    else:
        for chunk in hash_chunks:
            if url == "shlk.com/":
                url += chunk
                continue
            url += f"-{chunk}"

    return url
