import pandas
from os import listdir

files = listdir('X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports')

for f in files:
    path = f'X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports\\{f}'
    d = pandas.read_csv(path)
    try:
        r = d[d['Country/Region'] == 'Russia']
    except:
        
        d.rename(columns={'Country_Region': 'Country/Region', 'Province_State': 'Province/State', 'Last_Update': 'Last Update'}, inplace=True)
        
        d['Latitude'] = d['Lat']
        d['Longitude'] = d['Long_']
        
        del d['Lat']
        del d['Long_']
        
        del d['FIPS']
        del d['Admin2']
        del d['Active']
        del d['Combined_Key']
        
        r = d[d['Country/Region'] == 'Russia']
    if len(r) != 0:
        r.to_csv(f'X:\\DEL\\COVID-19\\csse_covid_19_data\\csse_covid_19_daily_reports_rus\\{f}')

