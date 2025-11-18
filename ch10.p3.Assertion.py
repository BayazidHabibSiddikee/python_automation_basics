market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switch(stop):
    for key in stop.keys():
        if stop[key]=='green':
            stop[key]='yellow'
        elif stop[key]=='yellow':
            stop[key]='red'
        elif stop[key]=='red':
            stop[key]='green'
assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
switch(market_2nd)
