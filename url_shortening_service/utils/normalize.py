def normalize_url(url: str):
    protocol = "http://"

    if url.startswith(protocol):
        url = url.replace(protocol, "")

    if url.startswith("www."):
        url = url.replace("www.", "")

    return url
