SELECT *
FROM movies;

----Quel est le film le plus long ?

--SELECT title, duration
--FROM movies
--ORDER BY duration DESC
--LIMIT 5;

----Quels sont les 5 films les mieux notés ?

--SELECT title, score
--FROM movies
--ORDER BY score DESC
--LIMIT 5;

----Dans combien de films a joué Morgan Freeman ? Tom Cruise ?

--SELECT actors, COUNT(*) AS nombre_de_films
--FROM movies
--WHERE actors LIKE '%Morgan Freeman%'
--GROUP BY actors;

----Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?

--SELECT title, score
--FROM movies
--WHERE genre = 'Comedy' 
--ORDER BY score DESC
--LIMIT 3;

-------- EXEMPLE ------
----WHERE genre = 'Drama'
----WHERE genre = 'Horror' 
----WHERE genre = 'Comedy' 


----Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?

--SELECT country, COUNT(*) AS nombre_de_films
--FROM movies
--WHERE id IN (SELECT id FROM movies ORDER BY score DESC LIMIT 100)
--GROUP BY country
--ORDER BY nombre_de_films DESC;



----Quel est la durée moyenne d’un film en fonction du genre ?

--SELECT genre, sum(duration)/LENGTH(genre) as duree_moyenne_genre
--FROM movies
--GROUP BY genre

------------ BONUS -------------

----En fonction du genre, afficher la liste des films les plus longs.

--SELECT title, duration
--FROM movies
--WHERE genre = "Comedy"
--ORDER BY duration DESC
--LIMIT 10;

-------- EXEMPLE --------
----WHERE genre = 'Drama'
----WHERE genre = 'Horror' 
----WHERE genre = 'Comedy' 

----En fonction du genre, quel est le coût de tournage d’une minute de film ?

--SELECT genre, ROUND((SUM(budget) / (SUM(duration) / COUNT(duration))) / AVG(LENGTH(title)), 2) AS cout_par_minute
--FROM movies
--WHERE duration > 0
--GROUP BY genre
--ORDER BY cout_par_minute DESC


----Quelles sont les séries les mieux notées ?

--SELECT title, score
--FROM series
--ORDER BY score DESC
--LIMIT 10



--SELECT *
--FROM movies
--WHERE title LIKE "La %" OR title LIKE "The %"

--SELECT actors, COUNT(title)
--FROM movies
--WHERE actors LIKE
--GROUP BY actors


--SELECT title,year, country
--FROM movies
--WHERE year<2000 AND country != 'United States' 
--ORDER BY score DESC



