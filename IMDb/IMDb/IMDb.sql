--Quel est le film le plus long ?
--SELECT title, duration
--FROM movies
--ORDER BY duration DESC
--LIMIT 5;

--Quels sont les 5 films les mieux notés ?
--SELECT title, score
--FROM movies
--ORDER BY score DESC
--LIMIT 5;

--Dans combien de films a joué Morgan Freeman ? Tom Cruise ?


--Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?
--SELECT title, score
--FROM movies
--WHERE genre = 'Comedy' 
--ORDER BY score DESC
--LIMIT 3;

-------- EXEMPLE ------
----WHERE genre = 'Drama'
----WHERE genre = 'Horror' 
----WHERE genre = 'Comedy' 


--Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?


--Quel est la durée moyenne d’un film en fonction du genre ?
--SELECT genre, sum(duration)/LENGTH(genre) as duree_moyenne_genre
--FROM movies
--GROUP BY genre

------------ BONUS -------------

--En fonction du genre, afficher la liste des films les plus longs.
SELECT title, duration
FROM movies
WHERE genre = "Comedy"
ORDER BY duration DESC
LIMIT 10;

-------- EXEMPLE --------
----WHERE genre = 'Drama'
----WHERE genre = 'Horror' 
----WHERE genre = 'Comedy' 

--En fonction du genre, quel est le coût de tournage d’une minute de film ?


--Quelles sont les séries les mieux notées ?
--SELECT title, score
--FROM series
--ORDER BY score DESC
--LIMIT 10



