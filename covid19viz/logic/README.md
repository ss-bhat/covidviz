#### Real Time DATA API

This application uses [covid-data-api](https://pypi.org/project/covid-data-api/) python package.
All the data are taken from the 
[CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse) 
with the below mentioned data sources. 
There are several methods to extract the statistics and counts for the country or province.

##### Usage Details - API Endpoints:

###### Action 1: Get stats:
Gets the latest total stats for all confirmed, deaths and recovered till the latest date available.
[get_stats](/api/v1/action/get_stats)
```
{
    result: {
        confirmed: 593291,
        deaths: 27198,
        last_updated: "2020-03-27 00:00:00",
        recovered: 130915
    },
    status: "success"
}
```
###### Action 2: Show all available Countries:
Shows all the available countries [show_available_countries](/api/v1/action/show_available_countries)
```
{
    count: 176,
    result: [
        "Afghanistan",
        "Albania",
        "Algeria",
        "Andorra"
    }
}
```
###### Action 3: Show all available Provinces:
Shows all the available provinces/regions [show_available_regions](/api/v1/action/show_available_regions)
```
{
    count: 76,
    result: [
        "Australian Capital Territory",
        "New South Wales"
        ],
    status: "success"
}
```
###### Action 4: Get records for all the countries:
Shows current data for all the countries [get_all_records_by_country](/api/v1/action/get_all_records_by_country)
```
result: {
    afghanistan: {
        confirmed: 110,
        deaths: 4,
        label: "Afghanistan",
        last_updated: "2020-03-27 00:00:00",
        lat: "33.0",
        long: "65.0",
        recovered: 2
    },
    albania: {
        confirmed: 186,
        deaths: 8,
        label: "Albania",
        last_updated: "2020-03-27 00:00:00",
        lat: "41.1533",
        long: "20.1683",
        recovered: 31
    },
}
```
###### Action 5: Get records for all the state/Province:
Shows current data for all the available regions [get_all_records_by_provinces](/api/v1/action/get_all_records_by_provinces)
```
{
result: {
    alberta: {
        confirmed: 542,
        country: "Canada",
        deaths: 2,
        label: "Alberta",
        last_updated: "2020-03-27 00:00:00",
        lat: "53.9333",
        long: "-116.5765"
        },
    anhui: {
        confirmed: 990,
        country: "China",
        deaths: 6,
        label: "Anhui",
        last_updated: "2020-03-27 00:00:00",
        lat: "31.8257",
        long: "117.2264",
        recovered: 984
        }
    }
}
```
###### Action 6: Filter by Country:
Filter the data by a given country. Returns the current stats for 
that country [filter_by_country?country=ireland](/api/v1/action/filter_by_country?country=ireland)

**Note:** Country name is case insensitive, you can use show_available_countries to verify the country name.
```
{
    result: {
        confirmed: 2121,
        deaths: 22,
        label: "Ireland",
        last_updated: "2020-03-27 00:00:00",
        lat: "53.1424",
        long: "-7.6921",
        recovered: 5
    },
    status: "success"
}
```
###### Action 7: Filter by Province/State:
Filter the data by a given province. Returns the current stats for 
the given region [filter_by_province?province=British Columbia](/api/v1/action/filter_by_province?province=British%20Columbia)

**Note:** Province/region name is case insensitive, you can use show_available_regions to verify the region/province name.
```
{
    result: {
        confirmed: 725,
        country: "Canada",
        deaths: 14,
        label: "British Columbia",
        last_updated: "2020-03-27 00:00:00",
        lat: "49.2827",
        long: "-123.1207"
    },
    status: "success"
}
```
###### Action 8: Get history data for a given Country:
Shows all the country metrics confirmed, recovered and deaths till the latest date [get_history_by_country?country=ireland](/api/v1/action/get_history_by_country?country=ireland)
```
{
    result: {
        ireland: {
            history: ....,
            label: "Ireland",
            lat: "53.1424",
            long: "-7.6921"
        }
    },
    status: "success"
}
```
###### Action 9: Get history data for a given State/Province:
Shows all the region metrics confirmed, recovered and deaths till the latest date [get_history_by_province?province=British Columbia](/api/v1/action/get_history_by_province?province=British%20Columbia)
```
{
    result: {
        british_columbia: {
            history: {},
            label: "British Columbia",
            lat: "49.2827",
            long: "-123.1207"
            }
        },
    status: "success"
}
```
Shows all the state/province metrics confirmed, recovered and deaths for the dates till the latest date.

##### Data Sources:
 
All used data sources [CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse).

##### Copying and License

###### Terms and conditions of the data provider:
[CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse)

###### Terms and Condition of this API:
License: [MIT](https://github.com/gtkChop/covid19/blob/master/LICENSE)