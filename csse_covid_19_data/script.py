import pandas
from os import listdir

files = listdir('X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports')

for f in files:
    path = f'X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports\\{f}'
    d = pandas.read_csv(path)
    try:
        r = d[d['Country/Region'] == 'Russia']
    except:
        d['Country/Region'] = d['Country_Region']
        del d['Country_Region']
        
        d['Province/State'] = d['Province_State']
        del d['Province_State']
        
        d['Last Update'] = d['Last_Update']
        del d['Last_Update']
        
        r = d[d['Country/Region'] == 'Russia']
    if len(r) != 0:
        r.to_csv(f'X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports_rus\\{f}')

