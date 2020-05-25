# -*- coding: utf-8 -*-
# @Author  : Qi Shao
"""
下载 ECMWF-ERA5 reanalysis 1000hPa relative humidity in china
"""

import cdsapi

# download data
def download(year, month, day, time):
    try:
        c = cdsapi.Client()
        c.retrieve(
            'reanalysis-era5-pressure-levels',
            {
                'product_type': 'reanalysis',
                'variable': 'relative_humidity',
                'pressure_level': '1000',
                'year': year,
                'month': [month],
                'day': [day],
                'time': [time],
                'format': 'netcdf',
                'area': [54, 73, 18, 136],
            },
            '../data/ECMWF/rh/nc/rh_' + year + month + day + '_' + time.replace(':', '') + '.nc')
        print('rh_' + year + month + day + '_' + time + '.nc')
    except:
        pass


if __name__ == '__main__':
    years = ['2019']
    months = ['12']
    days = ['01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31']
    times = [
        '00:00', '01:00', '02:00',
        '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00',
        '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00',
        '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00',
        '21:00', '22:00', '23:00',
    ]
    for year in years:
        for month in months:
            for day in days:
                for time in times:
                    download(year, month, day, time)




