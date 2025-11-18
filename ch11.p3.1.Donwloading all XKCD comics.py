import os, webbrowser , bs4 ,requests
#file = os.makedirs('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\XKCD', exist_ok=True)
#It's wrong -_- so Creating a folder name XKCD like

file='C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python312\\Ai Swighat\\XKCD'
os.makedirs(file,exist_ok=True)

url ='http://xkcd.com'
while not url.endswith('#'):
    
    print(f'Downloading....{url}')
    try:
        res=requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(f'Getting error on {url} as {e}')
        

    #print(res.text[:1000])
    #To get inside
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    #print(soup) #To print html text
    comic=soup.select('#comic img') #It will get but as list: or comic[0]
    '''<img src="//imgs.xkcd.com/comics/mission_to_culture.png"
title="It can't be very MUCH money ...
they apparently can't even afford a sampler.
I mean, with a little remixing, some of this could be kinda good!"
alt="Mission to Culture" style="image-orientation:none">'''
    if comic ==[]:
        print('Could not find comic img')
        
    else:
        comicU = 'https:'+comic[0].get('src')  #//imgs.xkcd.com/comics/mission_to_culture.png it's a raw image file to download -_-
        print('Downloading img from '+ comicU)
        try:
            resi = requests.get(comicU)
            resi.raise_for_status()
        except Exception as e:
            print(f'Getting error on {resi} as {e}')

        #comment it
        webbrowser.open(comicU)

        #Now need to save the image
        img = open(os.path.join(file,os.path.basename(comicU)),'wb')
        for i in resi.iter_content(10000):
            img.write(i)
        img.close()

    #Now need to change page so get the buttons URL
    prevlink = soup.select('a[rel="prev"]')[0].get('href')
    ##url = url + prevlink it's a problem as it's url is url with previous one so at 2nd time it becomes url + previous + previous
    url = 'http://xkcd.com' + prevlink
    

print('Done..')
                   
        
    
    
    
