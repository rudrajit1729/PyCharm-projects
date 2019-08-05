import random
import urllib.request
def download_web_image(url):
    name=random.randrange(1,1000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)
#examples
#download_web_image("https://i.pinimg.com/originals/69/ca/89/69ca89cb4b8ff780ee4bfab9593a4e2b.jpg")
#download_web_image("https://pixel.nymag.com/imgs/daily/vulture/2019/03/06/06-captain-marvel-round-up.w700.h467.jpg")
#download_web_image("https://pbs.twimg.com/media/D9myHSaXoAU7Kr9.jpg")
#download_web_image("http://oyster.ignimgs.com/wordpress/stg.ign.com/2019/04/thor-infinitywar.jpg")
download_web_image("Link to be pasted here")
