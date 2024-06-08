import instaloader
import os
L = None
def inst_login():
    global L
    L = instaloader.Instaloader()
    L.login('pocolocioa', 'Q47y18xQ')    
def download_reel(link=None):
    try:
        if "https://www.instagram.com/reel/" in link: link = find_between_r(link, 'https://www.instagram.com/reel/', '/')
        if "https://www.instagram.com/reels/" in link: link = find_between_r(link, 'https://www.instagram.com/reels/', '/')

        print(link)
        if "/?" in link: 
            link = link.partition('/?')[0]

        print(link)

        post = instaloader.Post.from_shortcode(L.context, link)

        video_url = post.video_url

        filename = L.format_filename(post, target=post.owner_username)

        path= os.path.join(os.path.dirname(__file__), f"_videos/{filename}")

        L.download_pic(filename=path, url=video_url, mtime=post.date_utc)

        return path
    
    except: return "Wrong url or private instagram pofile"


def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
    