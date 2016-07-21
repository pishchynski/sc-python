import webbrowser

from Anton.youtube_alarm.utils import get_links_from_file, get_random_link

links = get_links_from_file("links.txt")

random_link = get_random_link(links)

webbrowser.open(random_link)
