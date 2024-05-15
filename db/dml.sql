CREATE TABLE dm_total_contribution_by_year_quarter
    as
    SELECT  year, quarter, COUNT(quarter), SUM("Contribution (USD)") FROM sources_funding_unesco GROUP BY quarter, year ORDER BY sum ASC;

