Voici des définitions courtes, claires et adaptées à un entretien technique.

### Git

**Git** est un **système de gestion de versions** distribué qui permet de **suivre les modifications** du code source, **de collaborer** à plusieurs développeurs sur un même projet et de **gérer différentes versions** grâce aux branches (*branches*) et aux fusions (*merges*).

**Version interview :**

> Git est un outil de versioning qui permet de suivre l'historique du code, de collaborer en équipe et de gérer différentes versions d'une application de manière sécurisée.

---

### Docker

**Docker** est une **plateforme de conteneurisation** qui permet de **créer, déployer et exécuter des applications dans des conteneurs**. Un conteneur embarque l'application et toutes ses dépendances, garantissant un comportement identique quel que soit l'environnement d'exécution.

**Version interview :**

> Docker permet d'encapsuler une application et ses dépendances dans un conteneur afin qu'elle fonctionne de manière identique en développement, en test et en production.

---

### Python

**Python** est un **langage de programmation interprété**, **polyvalent** et **orienté objet**, reconnu pour sa **syntaxe simple** et sa **grande bibliothèque standard**. Il est utilisé dans le **développement web**, l'**automatisation**, la **data science**, l'**intelligence artificielle** et bien d'autres domaines.

**Version interview :**

> Python est un langage de programmation de haut niveau, facile à lire et à maintenir, utilisé aussi bien pour le développement logiciel que pour l'analyse de données, l'automatisation et l'intelligence artificielle.

---

### POO (Programmation Orientée Objet)

La **POO** est un **paradigme de programmation** qui organise le code autour d'objets. Un objet combine des données (attributs) et des comportements (méthodes). L'objectif est de rendre le code plus modulaire, réutilisable et maintenable.

Les 4 piliers de la POO sont :

* **Encapsulation** : protéger les données et contrôler leur accès.
* **Héritage** : réutiliser et étendre le comportement d'une classe existante.
* **Polymorphisme** : utiliser une même interface pour différents comportements.
* **Abstraction** : masquer la complexité et exposer uniquement l'essentiel.

**Version interview :**

> La POO est une méthode de conception logicielle qui consiste à modéliser une application sous forme d'objets. Elle améliore la réutilisabilité, la maintenabilité et l'organisation du code grâce à l'encapsulation, l'héritage, le polymorphisme et l'abstraction.

### Réponse très courte si l'intervieweur demande « en une phrase »

* **Git** : outil de gestion de versions permettant de suivre et partager les modifications du code.
* **Docker** : outil de conteneurisation garantissant qu'une application fonctionne de la même façon partout.
* **Python** : langage de programmation simple, polyvalent et très utilisé dans de nombreux domaines.
* **POO** : paradigme de programmation basé sur les objets pour produire un code modulaire et maintenable.

### Architecture 3 couches
L'architecture 3 couches consiste à séparer une application en une couche Présentation (interface utilisateur), une couche Métier (règles de gestion) et une couche Accès aux Données (persistance). Cette séparation facilite la maintenance, les tests et l'évolution de l'application.

* Exemple Spring Boot
* Controller → couche Présentation
* Service → couche Métier
* Repository → couche Accès aux Données