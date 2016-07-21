from random import randint


def get_links_from_file(filename: "Name of the file with links") -> list:
    """Return a list where each elements is a link string"""
    links_file = open(filename, "r")

    links = [link.strip("\n") for link in links_file]

    links_file.close()
    return links


def get_random_link(links: list) -> str:
    """Return a link string, randomly chosen from a links list"""
    random_link_index = randint(0, len(links) - 1)
    random_link = links[random_link_index]

    return random_link
