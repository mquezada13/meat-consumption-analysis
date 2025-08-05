# Share of the world's population with formal basic education - Data package

This data package contains the data that powers the chart ["Share of the world's population with formal basic education"](https://ourworldindata.org/grapher/share-of-the-world-population-with-at-least-basic-education?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For normal countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.

## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## No formal education
Share of people  aged 15 or older who have not received some kind of formal [primary](#dod:primary-education), [secondary](#dod:secondary-education), or [tertiary](#dod:tertiary-education) education.
Last updated: December 11, 2024  
Next update: December 2025  
Date range: 1820–2100  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
World Bank (2024); van Zanden, J. et al.; Wittgenstein Centre (2024) – with major processing by Our World in Data

#### Full citation
World Bank (2024); van Zanden, J. et al.; Wittgenstein Centre (2024) – with major processing by Our World in Data. “No formal education” [dataset]. World Bank, “World Bank Education Statistics (EdStats)”; van Zanden, J. et al., “How Was Life? Global Well-being since 1820 - Education 2014”; Wittgenstein Centre, “Human Capital, Wittgenstein Centre 3” [original data].
Source: World Bank (2024), van Zanden, J. et al., Wittgenstein Centre (2024) – with major processing by Our World In Data

### What you should know about this data
* Historical data for educational attainment between 1870 to 1950 comes from van Zanden, J. et al. (2014).
* Data for 1950 to 2015 is sourced from the Wittgenstein Centre Human Capital Centre. These projections are based on collected census and survey data. The SSP2 is a middle-of-the-road scenario that combines medium fertility with medium mortality, medium migration, and the Global Education Trend (GET) education scenario. For more information and other projection models, consult the Wittgenstein Centre for Demography and Global Human Capital's website: https://dataexplorer.wittgensteincentre.org/.
* Data for 2020 onwards is also based on the Medium Shared Socioeconomic Pathways (SSP2) Wittgenstein Centre for Demography and Global Human Capital projections. For more information, see https://pure.iiasa.ac.at/id/eprint/19487/.

### How is this data described by its producer - World Bank (2024), van Zanden, J. et al., Wittgenstein Centre (2024)?
Recent data from 2010 onwards is based on the Wittgenstein Centre for Demography and Global Human Capita. These projections are based on collected census and survey data for the base year (around 2010) and the Medium Shared Socioeconomic Pathways (SSP2) projection model. The SSP2 is a middle-of-the-road scenario that combines medium fertility with medium mortality, medium migration, and the Global Education Trend (GET) education scenario. For more information and other projection models, consult the Wittgenstein Centre for Demography and Global Human Capital's website: http://www.oeaw.ac.at/vid/dataexplorer/.

World Bank variable id: PRJ.ATT.15UP.NED.MF.

Original source: Wittgenstein Centre for Demography and Global Human Capital: http://www.oeaw.ac.at/vid/dataexplorer/.

### Sources

#### World Bank – World Bank Education Statistics (EdStats)
Retrieved on: 2024-11-04  
Retrieved from: https://datacatalog.worldbank.org/search/dataset/0038480/education-statistics  

#### van Zanden, J. et al. – How Was Life? Global Well-being since 1820 - Education
Retrieved on: 2023-08-14  
Retrieved from: https://www.oecd-ilibrary.org/economics/how-was-life/education-since-1820_9789264214262-9-en  

#### Wittgenstein Centre – Human Capital, Wittgenstein Centre
Retrieved on: 2024-12-06  
Retrieved from: https://dataexplorer.wittgensteincentre.org/wcde-v3/  

#### Notes on our processing step for this indicator
For each country and year, the share of the population aged 15 and older with no formal education was calculated. This involved summing up the population with no formal education and dividing it by the total population aged 15 and older for each country and year, then converting this ratio into a percentage.

A global estimate was calculated for each year by summing the total population aged 15 and older across all countries and the total population within this age group with no formal education. The share of the global population aged 15+ with no formal education was then computed for each year.

Historical data from van Zanden, J. et al. (2014) with estimates from 1870 to 1950 was combined with educational attainment estimates from Wittgenstein Centre for Demography and Global Human Capita.


## At least some basic education
Share of people  aged 15 or older who have received at least some kind of formal [primary](#dod:primary-education), [secondary](#dod:secondary-education), or [tertiary](#dod:tertiary-education) education.
Last updated: December 11, 2024  
Next update: December 2025  
Date range: 1820–2100  
Unit: %  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
World Bank (2024); van Zanden, J. et al.; Wittgenstein Centre (2024) – with major processing by Our World in Data

#### Full citation
World Bank (2024); van Zanden, J. et al.; Wittgenstein Centre (2024) – with major processing by Our World in Data. “At least some basic education” [dataset]. World Bank, “World Bank Education Statistics (EdStats)”; van Zanden, J. et al., “How Was Life? Global Well-being since 1820 - Education 2014”; Wittgenstein Centre, “Human Capital, Wittgenstein Centre 3” [original data].
Source: World Bank (2024), van Zanden, J. et al., Wittgenstein Centre (2024) – with major processing by Our World In Data

### What you should know about this data
* Historical data for educational attainment between 1870 to 1950 comes from van Zanden, J. et al. (2014).
* Data for 1950 to 2015 is sourced from the Wittgenstein Centre Human Capital Centre. These projections are based on collected census and survey data. The SSP2 is a middle-of-the-road scenario that combines medium fertility with medium mortality, medium migration, and the Global Education Trend (GET) education scenario. For more information and other projection models, consult the Wittgenstein Centre for Demography and Global Human Capital's website: https://dataexplorer.wittgensteincentre.org/.
* Data for 2020 onwards is also based on the Medium Shared Socioeconomic Pathways (SSP2) Wittgenstein Centre for Demography and Global Human Capital projections. For more information, see https://pure.iiasa.ac.at/id/eprint/19487/.

### How is this data described by its producer - World Bank (2024), van Zanden, J. et al., Wittgenstein Centre (2024)?
Recent data from 2010 onwards is based on the Wittgenstein Centre for Demography and Global Human Capita. These projections are based on collected census and survey data for the base year (around 2010) and the Medium Shared Socioeconomic Pathways (SSP2) projection model. The SSP2 is a middle-of-the-road scenario that combines medium fertility with medium mortality, medium migration, and the Global Education Trend (GET) education scenario. For more information and other projection models, consult the Wittgenstein Centre for Demography and Global Human Capital's website: http://www.oeaw.ac.at/vid/dataexplorer/.

World Bank variable id: PRJ.ATT.15UP.NED.MF.

Original source: Wittgenstein Centre for Demography and Global Human Capital: http://www.oeaw.ac.at/vid/dataexplorer/.

### Sources

#### World Bank – World Bank Education Statistics (EdStats)
Retrieved on: 2024-11-04  
Retrieved from: https://datacatalog.worldbank.org/search/dataset/0038480/education-statistics  

#### van Zanden, J. et al. – How Was Life? Global Well-being since 1820 - Education
Retrieved on: 2023-08-14  
Retrieved from: https://www.oecd-ilibrary.org/economics/how-was-life/education-since-1820_9789264214262-9-en  

#### Wittgenstein Centre – Human Capital, Wittgenstein Centre
Retrieved on: 2024-12-06  
Retrieved from: https://dataexplorer.wittgensteincentre.org/wcde-v3/  

#### Notes on our processing step for this indicator
For each country and year, the share of the population aged 15 and older with no formal education was calculated. This involved summing up the population with no formal education and dividing it by the total population aged 15 and older for each country and year, then converting this ratio into a percentage.

A global estimate was calculated for each year by summing the total population aged 15 and older across all countries and the total population within this age group with no formal education. The share of the global population aged 15+ with no formal education was then computed for each year.

Historical data from van Zanden, J. et al. (2014) with estimates from 1870 to 1950 was combined with educational attainment estimates from Wittgenstein Centre for Demography and Global Human Capita.

To calculate the share of the population with at least some basic education, the share of the population with no formal education was subtracted from 100%.


    