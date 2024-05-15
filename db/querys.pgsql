-- SELECT * FROM projects_unesco  WHERE "Beneficiary Country / Region" = 'Guatemala';

-- SELECT count(*) FROM mortality_icd_10_oms;

-- SELECT * FROM projects_unesco WHERE "uses_funding_unesco_sector" = 'Culture'
-- SELECT * FROM projects_unesco
-- SELECT "Sectordf.to_sql('projects_unesco', engine, if_exists='append', index=False)" FROM uses_funding_unesco GROUP BY "Sector";

-- SELECT year, quarter, COUNT(quarter) 
--     FROM sources_funding_unesco 
--     GROUP BY cube(year, quarter);


-- SELECT pbo."Country", pbo."Year", pbo."Sex", pbo."total_population", pbo."births", mdco."name"
--     FROM "population_births_oms" pbo INNER JOIN "mortality_doc_country_oms" mdco
--     ON pbo."Country" = mdco."Country";


-- SELECT "Country Name" as country_name, "Year", "gdp_current_price" 
--     FROM "gdp_current_prices_countries"

SELECT "uses_funding_unesco_sector"
    FROM "projects_unesco"
    GROUP BY "uses_funding_unesco_sector";

SELECT "Sector", count(*) as total
FROM uses_funding_unesco
GROUP BY "Sector"
ORDER BY total desc;

SELECT "Country"
FROM sdg_education_percent_country
GROUP BY "Country";

SELECT "Country Name"
FROM gdp_current_prices_countries
GROUP BY "Country Name";

SELECT  year, quarter, COUNT(quarter), MIN("Contribution (USD)") 
FROM sources_funding_unesco 
GROUP BY cube(quarter, year)