EDA
*shape
*dtypes
*columns
* No. Countries 187
* Years 13
* THe following countries have Nan in Pig Meat
    ['Afghanistan',
 'Kuwait',
 'Mauritania',
 'Pakistan',
 'Saudi Arabia',
 'Tunisia',
 'United Arab Emirates']
 This is important since the countries listed are muslim countiries and the pig meat consuption is null or restringed.   maybe this is the reason why of the null?? we can set this to 0kg is is the case for analysis and consider this at the end of the work when interpreting data. 
 
* The following Nan was found in Bovine Meat
 kiribati:  I learned that this country consumes mostly fish, because the mainteinance of xow meat is very difficult/impossible so they di not consume this type of meat which is "Bovine Meat". SOn this is mor geographyc rather than ideological as in the case of muslim places
* CUba also presents Nan values in the GDP per capita for the rears 2021 and 2022, but it corresponds to only two daya. It was removed from the analysis.
*South sudan also presents 4 Nans from 2019 - 2022
. THese rows will also be removed and if study is not good enugh for each country, it will be removed. As a input data for a total analysis/study/modeling, it is important data

* Data is divided in 5 big groups because we have so many countries, visualizadion is almost impossible unless we do several plots and is not ideal. The five groups are
    1. low
    2. Medium-low
    3. Medium
    4. High
    5. Extremely high.
The grpups were made to analise the consuption distribution across contries and the findings are that uin all 5 groups chiken is the most popular meat while Mutton & Goat is the less most consumed.
Among the 5 groups, we checked how many countries consume each type of meat, and we find that only in year 2022  above 80  countries consume chiken, around 30 (check numbers well) consume Pig, surprisingly cow is below, so maybe 25-28 countries and less than 10 countries consume Mutton & goat. 

* In average of the years 2010-2022 the numbers are not dramaticaly different, but changes are notisable. Chicken is consumed in almost 80 countries, pig reaches almost 40 countries and just below is cow, mutton and goat show not visible changes.

 Top 5 meat-consuming countries in 2022 (kg/person/year):
        Country  meat_2022
1779      Tonga     147.51
878      Israel     113.18
77    Argentina     112.08
103   Australia     111.40
1197   Mongolia     108.47

 Bottom 5 meat-consuming countries in 2022 (kg/person/year):
         Country  meat_2022
290      Burundi       3.63
146   Bangladesh       4.25
1517      Rwanda       4.97
1080  Madagascar       5.21
1331       Niger       5.25
