import requests, os
from N4Tools.Design import (
    Animation,
    Text,
    Color,
)
class ToolStyle:
    def __init__(self):
        self.AN = Animation()
        self.CO = Color()
        self.TX = Text()

        self.intro = self._intro()
        os.system('clear')
        print(self.intro)

    def _intro(self):
        return self.TX.CentreAlignPro([
            self.TX.Figlet('N4User')+'\n',
            '[ [$LYELLOW]@No_Name_999[$NORMAL] ]'
            ])+'\n'

    def CustomInput(self,text):
        text = self.CO.LBLUE+text
        self.AN.SlowText(text,timer=.02)
        return input()

ToolStyle = ToolStyle()

class UserSearch:
    links = [
        'https://www.facebook.com/',
        'https://twitter.com/',
        'https://www.instagram.com/',
        'https://www.youtube.com/user/',
        'https://www.pinterest.com/',
        'https://www.flickr.com/people/',
        'https://vimeo.com/',
        'https://soundcloud.com/',
        'https://disqus.com/',
        'https://medium.com/@',
        'https://about.me/',
        'https://flipboard.com/',
        'https://slideshare.net/',
        'https://open.spotify.com/user/',
        'https://www.scribd.com/',
        'https://www.patreon.com/',
        'https://bitbucket.org/',
        'https://gitlab.com/',
        'https://www.github.com/',
        'https://www.goodreads.com/',
        'https://www.instructables.com/member/',
        'https://www.codecademy.com/',
        'https://en.gravatar.com/',
        'https://pastebin.com/u/',
        'https://foursquare.com/',
        'https://tripadvisor.com/members/',
        'https://www.wikipedia.org/wiki/User:',
        'https://news.ycombinator.com/user?id=',
        'https://www.codementor.io/',
        'https://www.trip.skyscanner.com/user/',
        'https://blogspot.com/',
        'https://wordpress.com/',
        'https://tumblr.com/',
        'https://livejournal.com/',
        'https://slack.com/',
        'https://ask.fm/',
        'https://www.snapchat.com/add/',
        'https://www.tiktok.com/@',
        'https://haraj.com.sa/users/',
        'https://t.me/',
    ]
    accses_links = []

    def start(self):
        username = ToolStyle.CustomInput('Enter Username : ')
        print('')
        try:
            self.search(username)
        except KeyboardInterrupt:
            pass
        print('')
        ToolStyle.CustomInput('Done...[ enter ]')
        if self.accses_links:
            os.system('clear')
            print (ToolStyle.intro)
            for num,req in enumerate(self.accses_links):
                num += 1
                host = req.url.replace('https://', '')
                host = host.split('/')[0]
                for _del in ['www.','.io','.com','.net','.org']:
                    host = host.replace(_del,'')

                Zs = '0' if len(self.accses_links) > 9 and num < 10 else ''
                print(
                    ToolStyle.CO.reader(f'[[$LGREEN]{Zs}{num}[$/]] {host}')
                )

            print('')
            try:
                while True:
                    num = ToolStyle.CustomInput('Enter Number : ')
                    try:
                        print(f'\n{self.accses_links[int(num)-1].url}\n')
                    except:
                        print('\nNot found!\n')
            except KeyboardInterrupt:
                exit('\n\n:D good-bye')

    def search(self,username):
        for link in self.links:
            link = link + username
            is_error = False

            try:
                req = requests.get(link)
            except requests.exceptions.ConnectionError as e:
                # wifi error:
                is_error = True
                print(ToolStyle.CO.reader(
                    f'[ [$RED]Error[$/] ] {e}'
                    )
                )

            if not is_error:
                if req.status_code == 200 and\
                        not req.is_redirect and\
                        username.lower() in req.url.lower():
                    self.accses_links.append(req)
                    color = ToolStyle.CO.LGREEN
                else:
                    color = ToolStyle.CO.LRED

                host = link.replace('https://','')
                host = host.split('/')[0]
                print(f'[ {color+str(req.status_code)} ] [{color+host}]')

if __name__ == '__main__':
    tool = UserSearch()
    tool.start()
