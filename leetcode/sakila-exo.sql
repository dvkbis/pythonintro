--1. Affichez le prénom et le nom de tous les acteurs de l'acteur de la table.
SELECT first_name, last_name
FROM actor

--2.Trouvez le numéro d'identification, le prénom et le nom de famille d'un acteur, 
--	dont vous ne connaissez que le prénom «William».
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = 'William'

--3. Affichez le prénom et le nom de chaque acteur dans une seule colonne en majuscules. 
--	Nommez la colonne Nom de l'acteur.
SELECT UPPER(first_name + ' ' + last_name) AS 'Nom de l''acteur'
FROM actor

--4. Sélectionner les clients actifs.
SELECT *
FROM customer
WHERE active = '1'

--5. Sélectionner les films sauf   'GREASE YOUTH'.
SELECT *
FROM film
WHERE title != 'GREASE YOUTH'

--6. Trouvez tous les acteurs dont le nom contient les lettres « GEN ».
SELECT *
FROM actor
WHERE last_name LIKE '%GEN%'

--7.Trouvez tous les acteurs dont les noms contiennent les lettres « LI » ou la 3e lettre est « E » . 
-- Cette fois, triez les lignes par nom et prénom, dans cet ordre.
SELECT *
FROM actor
WHERE last_name LIKE '%LI%' OR last_name LIKE '__E%'

--8. Affichez les colonnes country_id et country des pays suivants: 
--	Afghanistan, Bangladesh et Chine.
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh','China')

--9. Sélectionner les 5 premières descriptions de films ayant une description 
--	contenant le mot "Woman". 
SELECT *
FROM film
WHERE description LIKE '%Woman%'

--10. Récupérer la longueur des films en heures ainsi que leur titre et 
--	classez-les du plus long au plus court.

SELECT title, length
FROM film
ORDER BY length DESC

--11.	Sélectionner les films ayant comme fonctionnalités spéciales (special_features) :
--	des commentaires les trier par durée de location ascendante.
SELECT *
FROM film
WHERE special_features LIKE '%Commentaries%'
ORDER BY rental_duration ASC

--12.	Sélectionner les locations entre le 20 mai 2005 et le 25 mai 2005 et 
--	les trier du plus récent au plus ancien.
SELECT *
FROM rental
--WHERE rental_date BETWEEN '2005-05-20' AND '2005-05-26'
WHERE DATEPART(year,rental_date) = 2005 AND
	DATEPART(month, rental_date) = 5 AND
	DATEPART(day, rental_date) BETWEEN 20 AND 25
ORDER BY rental_date DESC



--13.	Sélectionner tous les titres de films ne commençant pas par "A".
SELECT title
FROM film
WHERE title NOT LIKE 'A%'
--14.	Sélectionner tous les films qui ne sont pas sortis en 2005.
SELECT *
FROM film
WHERE release_year != 2005

--15.	Sélectionner les clients qui ne se sont pas inscrits 
-- entre le 13 et le 14 février 2006.
SELECT *
FROM customer
WHERE DATEPART(year,create_date) = 2006 AND
	DATEPART(month, create_date) = 2 AND
	DATEPART(day, create_date) BETWEEN 13 AND 14

--	16.	Sélectionner les films dont l'id est entre 0-10 
--	ou dont la durée est supérieure à 3h et qui ont un rating PEGI (PG).

SELECT *
FROM film
WHERE film_id BETWEEN 0 AND 10 
	OR (length > 180 AND rating = 'PG')

--17. Quels acteurs portent le nom de famille «Johansson» et 
--	qui a joué dans le film 'Casper Dragonfly' ?
SELECT *
FROM actor ACTOR JOIN film_actor FILMACTOR ON ACTOR.actor_id = FILMACTOR.actor_id
	 JOIN film FILM ON FILM.film_id = FILMACTOR.film_id
WHERE FILM.title = 'Casper Dragonfly' AND ACTOR.last_name = 'Johansson'

--18. Quelle est l’adresse correspondant à chaque client ?
SELECT *
FROM customer C LEFT JOIN ADDRESS A ON C.address_id = A.address_id

--19. Sélectionner les paiements dont le montant est supérieur à 10. 
--	Quels sont les clients ayant fait ces paiements ? 
SELECT P.payment_id, P.amount, C.customer_id, C.first_name, C.last_name
FROM payment P JOIN customer C ON P.customer_id = C.customer_id
WHERE P.amount > 10

--20.	Sélectionner les adresses dont le code postal est 45844, 43331 et 65750. 
--	Quels sont les clients ayant ces codes postaux ?
SELECT A.postal_code, C.customer_id, C.first_name, C.last_name
FROM customer C JOIN address A ON C.address_id = A.address_id
WHERE postal_code IN (45844, 43331, 65750)

--21.	Combien y a-t-il de noms de famille d'acteurs distincts? 
SELECT COUNT(*)
FROM (SELECT DISTINCT last_name
		FROM actor) AS ACTOR

--22.	Quels acteurs ont joué dans quels films ?
SELECT A.first_name, A.last_name, F.title
FROM actor A JOIN film_actor FA ON A.actor_id = FA.actor_id
	 JOIN film F ON F.film_id = FA.film_id

--23.	Énumérez les noms de famille des acteurs,
--	ainsi que le nombre d'acteurs qui portent ce nom de famille. 
--	Triez et sélectionnez  les 5 noms les plus utilisés dans la base de données.
-- nom, nb
SELECT TOP 5 last_name, count(*) AS 'count'
FROM actor
GROUP BY last_name
ORDER BY count(*) DESC

--24.	Lister les noms de famille des acteurs et 
--	le nombre d'acteurs qui portent ce nom de famille, 
--	mais uniquement pour les noms partagés par au moins deux acteurs.
SELECT last_name, count(*) AS 'count'
FROM actor
GROUP BY last_name
HAVING count(*) > 1
ORDER BY count(*) DESC

--25.	Identifier les magasins, leur localisation et leur manager.
SELECT S.store_id, 
	A.address, C.city,
	STAFF.first_name, STAFF.last_name
FROM city C RIGHT JOIN address A ON C.city_id = A.city_id JOIN store S ON A.address_id = S.address_id 
	JOIN staff STAFF ON S.manager_staff_id = STAFF.staff_id 
	
--26.	Combien de films y a-t-il par langues ?
SELECT L.name, count(*)
FROM language L LEFT JOIN film F ON F.language_id = L.language_id
GROUP BY L.name

--27.	Quels sont les membres du staff sans image ?
SELECT first_name, last_name
FROM staff
WHERE picture IS NOT NULL

--28.	Combien y a-t-il de films où la durée de location est supérieure à 5 jours ?
SELECT COUNT(*)
FROM film
WHERE rental_duration > 5

--29. Quelle est la durée moyenne de tous les films de la base de données sakila?
SELECT AVG(CONVERT(FLOAT,length)) AS 'Durée moyenne des films'
FROM film

--30. Combien d'exemplaires de film existe-t-il dans le système d'inventaire 
--	avec le mot ‘Voyage’? 
SELECT COUNT(*)
FROM inventory I LEFT JOIN film F ON I.film_id = F.film_id
WHERE F.title LIKE '%Voyage%'

--31.	Calculer la somme et le nombre de paiements effectués par le client 
--	dont le prénom est "MARGARET".
SELECT 'MARGARET' AS 'name', SUM(P.amount) AS 'somme paiment', COUNT(*) AS 'nombre de paiment'
FROM customer C JOIN payment P ON C.customer_id = P.customer_id
WHERE first_name LIKE 'MARGARET'

--32. Quels sont les clients ayant un montant total de location 
--		supérieur à la moyenne générale ?
WITH Moy(customer_id, first_name, last_name, total_location) AS
	(SELECT C.customer_id, C.first_name, C.last_name, COUNT(*) AS 'total_location'
	FROM rental R JOIN customer C ON R.customer_id = C.customer_id
	GROUP BY C.customer_id, C.first_name, C.last_name)
SELECT last_name, first_name, total_location
FROM Moy
WHERE total_location > (SELECT AVG(total_location) FROM Moy)
ORDER BY total_location, last_name, first_name

--33.	Quels sont les clients ayant 
--	un montant total supérieur à la moyenne de leur magasin ?
WITH TotalCustomer(customer_id, store_id, total_paiement) AS
	(SELECT C.customer_id, C.store_id, SUM(P.amount) AS 'total paiement'
	FROM customer C JOIN payment P ON C.customer_id = P.customer_id
	GROUP BY C.customer_id, C.store_id)

SELECT T1.store_id, C.customer_id, C.first_name, C.last_name, T1.total_paiement
FROM TotalCustomer T1 JOIN customer C ON T1.customer_id = C.customer_id
WHERE EXISTS  ( 
	SELECT store_id, AVG(total_paiement)
	FROM TotalCustomer T2
	WHERE T1.store_id = T2.store_id
	GROUP BY store_id
	HAVING AVG(total_paiement) < T1.total_paiement)
ORDER BY store_id, total_paiement

--34.	Quel est le plus petit montant payé par l'utilisateur 1 ?
SELECT MIN (amount)
FROM (SELECT C.customer_id, P.amount AS 'amount'
	FROM customer C JOIN payment P ON C.customer_id = P.customer_id
	WHERE C.customer_id = 1) AS T

--35.	Quel acteur est apparu dans le plus de films? 
WITH NbActorFilm (actor_id, count) AS(
	SELECT actor_id, COUNT(*) AS 'count'
			FROM film_actor 
			GROUP BY actor_id)
SELECT A.first_name, A.last_name, count AS 'Nb de films'
FROM NbActorFilm N JOIN Actor A ON A.actor_id = N.actor_id
WHERE count = (SELECT MAX(count)
				FROM NbActorFilm)
	

--36. Les films commençant par les lettres W et C ont gagné en popularité. 
--	Utilisez des sous-requêtes pour afficher les titres des films 
--	en commençant par les lettres W et C dont la langue est l'anglais.
SELECT title
FROM film F
WHERE (title LIKE 'W%' OR title LIKE 'C%')
	AND language_id IN (SELECT language_id
						FROM language 
						WHERE name = 'English')

--37.	Sélectionne les 10 premiers clients actifs (le plus de location) du store 
--	dont Mike Hillyer est le manager 
--	(1er manière en jointure et une deuxième manière en sous requête).
--> JOIN
SELECT TOP 10 R.customer_id, C.first_name, C.last_name, count(*) AS 'nombre_de_locations'
FROM rental R JOIN customer C ON R.customer_id = C.customer_id
	JOIN store STORE ON C.store_id = STORE.store_id
	JOIN staff STAFF ON STORE.store_id = STAFF.staff_id
WHERE (STAFF.first_name LIKE 'Mike' AND STAFF.last_name LIKE 'Hillyer')
	AND C.active = '1'
GROUP BY R.customer_id, C.first_name, C.last_name
ORDER BY count(*) DESC

-->SOUS-REQUETE
SELECT customer_id, first_name, last_name
FROM customer 
WHERE customer_id IN (
	SELECT TOP 10 customer_id
	FROM rental R
	WHERE customer_id IN (
		SELECT customer_id
		FROM customer 
		WHERE store_id = (
			SELECT store_id 
			FROM store
			WHERE manager_staff_id = (
				SELECT staff_id
				FROM staff
				WHERE first_name LIKE 'Mike' AND last_name LIKE 'Hillyer'
			)
		) AND active = '1'
	) 
	GROUP BY customer_id
	ORDER BY count(*) DESC
)


--38.	Est-ce que «Academy Dinosaur» est disponible à la location dans le magasin 1? 
SELECT CASE WHEN count(*) > 0
			THEN 'OUI'
			ELSE 'NON'
		END AS 'Academy Dinosaur disponible dans magasin 1?'
FROM inventory I JOIN film F ON I.film_id = F.film_id
WHERE F.title LIKE 'Academy Dinosaur'
	AND I.store_id = 1

--39.	Est-ce qu'il y a des films qui n'ont jamais été loués ?
-- Pas dans le système de location?
SELECT title
FROM film F LEFT JOIN inventory I ON F.film_id = I.film_id
WHERE inventory_id IS NULL
GROUP BY title

--film jamais loué de la liste de film pouvant être loués
SELECT CASE WHEN count(*) > 0
			THEN 'OUI'
			ELSE 'NON'
		END AS 'Y a-t-il des films non loués?'
FROM (
	SELECT DISTINCT film_id
	FROM inventory INV
	WHERE NOT EXISTS(
		SELECT I.film_id, count(*)
		FROM inventory I JOIN rental R ON I.inventory_id = R.inventory_id
		WHERE INV.film_id = I.film_id
		GROUP BY I.film_id) 
) AS T
--40. Quelle est la durée moyenne des films par catégorie? 
SELECT C.name AS 'Category_name', AVG(F.length) AS 'durée moyenne des films'
FROM category C JOIN film_category FC ON 
	C.category_id = FC.category_id 
	JOIN film F ON
	FC.film_id = F.film_id
GROUP BY C.name

--41.	Quels sont les acteurs qui ont joué au moins 1 film (utiliser le EXIST)?
SELECT A.first_name, A.last_name
FROM actor A
WHERE EXISTS (SELECT FA.actor_id, COUNT(*)
			FROM film_actor FA
			WHERE A.actor_id = FA.actor_id
			GROUP BY FA.actor_id
			HAVING COUNT(*) >= 1)

--42.	Quels sont les acteurs qui ont déjà joué dans un film d'horreur (catégorie 'Horror’) ?
SELECT DISTINCT first_name, last_name
FROM actor
WHERE actor_id IN (
	SELECT DISTINCT actor_id
	FROM film_actor 
	WHERE film_id IN (
		SELECT film_id
		FROM film_category
		WHERE category_id = (
			SELECT category_id
			FROM category
			WHERE name = 'Horror'
		)
	)
)

--43.	Affichez le montant total appelé par chaque membre du personnel (staff) en août 2005.  
SELECT (
		SELECT CONCAT(first_name, ' ', last_name) 
		FROM staff st 
		WHERE st.staff_id = S.staff_id
	) as 'nom employé', 
	SUM(P.amount) AS 'Montant total'
FROM staff S JOIN payment P ON S.staff_id = P.staff_id 
WHERE YEAR(P.payment_date) = 2005 AND MONTH(P.payment_date) = 8
GROUP BY S.staff_id


--44.	Énumérez chaque film et le nombre d'acteurs qui sont répertoriés pour ce film. 
--		Utilisez les tables film_actor et film. 
SELECT F.film_id, F.title, 0 AS 'nombre_acteurs_repertories'
FROM film F LEFT JOIN film_actor FA ON F.film_id = FA.film_id
WHERE FA.actor_id IS NULL
GROUP BY F.film_id, F.title 
UNION
SELECT F.film_id, F.title, count(*) AS 'nombre_acteurs_repertories'
FROM film F LEFT JOIN film_actor FA ON F.film_id = FA.film_id
WHERE FA.actor_id IS NOT NULL
GROUP BY F.film_id, F.title 
ORDER BY film_id

--45.	Quels sont les acteurs qui ont joué avec Penelope Guiness ?
WITH MyActorId(actor_id) AS (
	SELECT actor_id
	FROM actor
	WHERE first_name LIKE 'Penelope' AND last_name LIKE 'Guiness'
)
SELECT DISTINCT A.first_name, A.last_name
FROM actor A JOIN film_actor FA ON A.actor_id = FA.actor_id
WHERE FA.film_id IN (
	SELECT film_id
	FROM film_actor
	WHERE actor_id = (
		SELECT actor_id
		FROM MyActorId
	)
) 
AND A.actor_id != (SELECT actor_id FROM MyActorId)
--46.	Vous souhaitez lancer une campagne de marketing par courriel au Canada,
--	pour laquelle vous aurez besoin des noms et 
--	adresses électroniques de tous les clients canadiens. Récupérez ces informations.
SELECT CU.first_name + ' ' + CU.last_name AS 'name', CU.email
FROM customer CU 
	JOIN address A  ON CU.address_id = A.address_id
	JOIN city CI ON A.city_id = CI.city_id
	JOIN country CO ON CI.country_id = CO.country_id
WHERE CO.country = 'Canada'

--47.	Les ventes sont à la traîne chez les jeunes familles 
--	et vous souhaitez cibler tous les films familiaux pour une promotion.
--	Identifiez tous les films classés comme films familiaux.
SELECT F.title
FROM film F JOIN film_category FC
	ON F.film_id = FC.film_id
WHERE FC.category_id =(
	SELECT category_id 
	FROM category
	WHERE name LIKE 'Family'
)


--48.	Affichez les films les plus fréquemment loués dans l'ordre décroissant.
SELECT F.title, count(*) AS 'Nbre de locations'
FROM rental R
	JOIN inventory I ON R.inventory_id = I.inventory_id
	JOIN film F ON I.film_id = F.film_id
GROUP BY F.title
ORDER BY count(*) DESC

--49.	Quels sont les acteurs qui ont joué dans toutes les catégories de film ?
SELECT A.first_name, A.last_name
FROM (
	SELECT DISTINCT FA.actor_id, FC.category_id
	FROM film_actor FA, film_category FC
	WHERE FA.film_id = FC.film_id) AS T
		JOIN actor A ON A.actor_id = T.actor_id
	GROUP BY A.first_name, A.last_name
	HAVING count(*) = (SELECT count(*) FROM category) 


--50.	Quels sont les cinq principaux genres en termes de revenus bruts ?

SELECT TOP 5 C.name, SUM(revenu_film) AS 'revenu par categorie'
FROM(
	SELECT film_id, SUM(revenu_inventaire) AS 'revenu_film'
	FROM (
			SELECT R.inventory_id, SUM(P.amount) AS 'revenu_inventaire'
			FROM payment P JOIN rental R 
				ON P.rental_id = R.rental_id
			GROUP BY R.inventory_id
		) AS T JOIN inventory I
			ON T.inventory_id = I.inventory_id
	GROUP BY film_id
) AS T2 JOIN film_category FC
		ON T2.film_id = FC.film_id
		JOIN category C
		ON FC.category_id = C.category_id
GROUP BY C.name
ORDER BY SUM(revenu_film) DESC


