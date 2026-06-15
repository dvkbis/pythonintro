### Key words
- BLOB (Binary Large Object)
- checksum
    - prend le contenu binaire
    - en sha256 
    - vérifier l'intégrité d'un fichier
    - git va s'en servir vérifier si le fichier a été modif (manière rapide)
- tree
    - ensemble de blob
    - commit : quel est le tree qui est lié à ce commit

- branch (en général)
    - une par feature
    - une par dev

### Advices
- .git ignore generator qui génére le git ignore avec la bonne syntaxe
-  OU git ignore template
- FORK > Pull request || Rebase (IMPORTANT)
- Branch main > Créer sa propre branche

### Commands
- git checkout HEAD^ 
    - **^** > Trouver le parent
- git checkout HEAD~4 
    - **~** > Revenir n parent en arriére
- git branch -f HEAD~3 
    -  Forcer à bouger une branche à l'emplacement HEAD^3
- git reset [ref-commit]
- git revert 
    -  Annuler des changements et partager ces annulations avec d'autres
- git cherry-pick <Commit1> <Commit2> <...> 
    -  copier une série de commits en-dessous de notre emplacement actuel (HEAD)
- git rebase -i
    - Pareil que cherry-pick mais avec une interface 
    - Git va ouvrir une interface graphique et montrer quels commits vont être copiés
    - 3 possibilités:
        - réarranger les commits
        - (dé)selectionner des commits (pick)
        - écraser des commits
- git commit --amend 
    - modifies your most recent commit without creating a new one 
- git tag [tag] [ref-commit]
    - Un tag est associé a un seul commit
- git describe [ref]
 - Réponse : <tag>-<numCommits>-g<hash>

- git bisect [start/reset/good/bad] 
    - debogage pour trouver un bug 
- git fetch 
    -  rapporter (fetch) des données depuis un dépôt distant vers le nôtre
    -  met à jour nos branches distantes (par exemple, o/main)

- git fetch; git merge origin/main  == git pull




 
