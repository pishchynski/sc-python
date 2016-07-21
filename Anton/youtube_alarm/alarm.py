links_file = open("links.txt", "r")
links = [link.strip("\n") for link in links_file]
links_file.close()
