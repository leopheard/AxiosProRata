from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://feeds.megaphone.fm/pro-rata"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "http://megaphone-prod.s3.amazonaws.com/podcasts/75a0a63e-7284-11e9-a623-1b50e2843885/image/53aa1a75b60e36e8a5daaa6f9fde44382b12e7d7db1ee809e53544ddb1cc2126a09b70662657dfa250798d6ffc0f75f332b7bc6e0a6d1fa3009a965dbab2920f.jpeg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "http://megaphone-prod.s3.amazonaws.com/podcasts/75a0a63e-7284-11e9-a623-1b50e2843885/image/53aa1a75b60e36e8a5daaa6f9fde44382b12e7d7db1ee809e53544ddb1cc2126a09b70662657dfa250798d6ffc0f75f332b7bc6e0a6d1fa3009a965dbab2920f.jpeg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
