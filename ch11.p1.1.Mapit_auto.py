import webbrowser, pyperclip, sys , urllib
#C:\> mapit (870 Valencia St, San Francisco, CA 94110)
#sys.argv[0] [1] [2+]
'''In google
https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110,
+USA/@37.7169742,-122.4676214,11.72z/data=!4m6!3m5!1s0x808f7e3dae0d389d:
0x26ff1ce51ce8ccff!8m2!3d37.7589699!4d-122.4216488!16s
%2Fg%2F11yfd08xjt?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D    '''


# normally https://www.google.com/maps
#addr = '870 Valencia St, San Francisco, CA 94110'

if len(sys.argv)>1:
    addr = '+'.join(sys.argv[1:])
else:
    addr = pyperclip.paste()
    addr='+'.join(addr.split())
#addr = urllib.parse.quote(addr,safe='')
print('https://www.google.com/maps/place/' + addr)
webbrowser.open('https://www.google.com/maps/place/' + addr)
