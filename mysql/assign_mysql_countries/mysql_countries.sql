SELECT countries.name AS Contrie_name, languages.language AS Language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language = "Slovene"
ORDER BY languages.percentage DESC;


SELECT countries.name As countrie, count(cities.name) AS cities_number
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name 
ORDER BY cities_number DESC;



SELECT countries.name As countrie, cities.name AS city , cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Mexico" and cities.population > 500000
order by cities.population DESC;

SELECT countries.name AS Contrie_name, languages.language AS Language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89.0
ORDER BY languages.percentage DESC;

SELECT countries.name As country, countries.surface_area AS Surface_area, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.surface_area < 501 and cities.population > 100000;

SELECT  countries.name country, countries.capital AS capital,countries.life_expectancy AS life_expectancy,countries.government_form AS government_form
FROM countries
WHERE countries.government_form = "Constitutional Monarchy" and capital > 200 and life_expectancy > 75;

SELECT  countries.name AS country_name, cities.name AS city_name, cities.district as district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina" and cities.district = "Buenos Aires" AND  cities.population >500000;


SELECT countries.region, count(countries.name) AS countries
FROM countries
GROUP BY countries.region
ORDER BY countries desc;











