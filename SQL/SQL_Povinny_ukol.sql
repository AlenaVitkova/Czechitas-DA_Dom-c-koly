--1:
SELECT DATE_FROM_PARTS(iyear, imonth, iday) AS DATUM,
       country_txt AS zeme,
       COUNT(eventid) AS pocet_utoku,
       SUM(nkill) - SUM(nkillter) AS pocet_zabitych_obeti,
       SUM(nkillter) AS pocet_mrtvych_teroristu,
       SUM(nwound) AS pocet_zranenych
FROM teror
WHERE country_txt IN ('Iraq', 'Nigeria', 'Syria')
      AND iyear = 2015
GROUP BY iyear, imonth, iday, country_txt
HAVING pocet_utoku >= 10
   AND pocet_zabitych_obeti >= 8
ORDER BY country_txt ASC, DATUM ASC;

--2:
SELECT COUNT(eventid) AS pocet_utoku,
    SUM(nkill) - SUM(nkillter) AS pocet_obeti,
    CASE
        WHEN HAVERSINE(50.0755, 14.4378, latitude, longitude) <100 THEN '0-99km'
        WHEN HAVERSINE(50.0755, 14.4378, latitude, longitude) < 500 THEN '100-499km'
        WHEN HAVERSINE(50.0755, 14.4378, latitude, longitude) <1000 THEN '500-999km'
        WHEN HAVERSINE(50.0755, 14.4378, latitude, longitude) >= 1000 THEN '1000 a více km'
        ELSE 'exact location unknown'
    END AS vzdalenost_od_Prahy
FROM TEROR
WHERE iyear BETWEEN 2014 AND 2015
GROUP BY vzdalenost_od_Prahy
ORDER BY pocet_utoku DESC;

—3.
SELECT NKILL, EVENTID, IYEAR, COUNTRY_TXT, CITY, attacktype1_txt, targtype1_txt, gname, weaptype1_txt
FROM TEROR
WHERE COUNTRY_TXT IN ('Iraq', 'Afghanistan', 'Pakistan', 'Nigeria') AND (TARGTYPE1_TXT != 'Private Citizens & Property' 
    OR GNAME = 'Taliban')
ORDER BY NKILL DESC NULLS LAST
LIMIT 15;
