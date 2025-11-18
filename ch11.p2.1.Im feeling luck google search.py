import webbrowser , sys ,pyperclip , requests , bs4 #bs4 to find links of web browsers 

if len(sys.argv)>1:
    addr=''.join(sys.argv[1:])
else:
    addr = pyperclip.paste()

print('Googling....'+addr)

try:
    res = requests.get('http://google.com/search?q='+addr)
    res.raise_for_status()
except Exception as e:
    print('There is a exception '+e)
    sys.exit()

search = bs4.BeautifulSoup(res.text,'html.parser')

#Open browser tab for each result
link = search.select('a')

numOpen=min(10,len(link))
try:
    for i in range(numOpen):
        href = link[i].get('href')
        if href.startswith('/url?q='): #removing junk urls
            print(href)
            url =href.split('&')[0].replace('/url?q=','')
            print(url)
            webbrowser.open(url)
        else:
            webbrowser.open('http://google.com'+href)
except Exception as e:
    print('There is a exception '+e)

