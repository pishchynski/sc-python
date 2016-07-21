from random import randint


def get_links(filename: "Name of the file with links") -> list:
    """Return a list where each elements is a link string"""
    links_file = open(filename, "r")

    links = [link.strip("\n") for link in links_file]

    links_file.close()
    return links


links = get_links("links.txt")

random_link_index = randint(0, len(links) - 1)
random_link = links[random_link_index]

print(links)
print(random_link)
