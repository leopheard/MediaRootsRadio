from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL0 = "https://anchor.fm/s/5217eb0/podcast/rss"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/dir-logo/255779/255779_300x300.jpg"},
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/dir-logo/255779/255779_300x300.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL0)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL0)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
