import webbrowser


ORIGIN = 'm/02_286' # Google Flights code for NYC area
DESTINATIONS = ['SYD', 'MEL', 'CNS', 'ASP', 'AYQ']
DATES= ['2019-04-22', '2019-04-25', '2019-04-30']


if __name__ == '__main__':
    for destination in DESTINATIONS:
        for date in DATES:
            webbrowser.open('https://www.google.com/flights/#flt=/%s.%s.%s;c:USD;e:1;sd:1;t:f;tt:o' % (ORIGIN, destination, date))
