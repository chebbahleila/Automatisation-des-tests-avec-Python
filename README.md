# Automatisation-des-tests-avec-Python

Telecharger Python : www.python.org/downloads/
prendre la version 3.10.2
apres execution du fichier telechargé, aller sur le fichier phython et enregistrer l'emplacement du repertoire ou se trouve le fihicer Python.exe (exp: C:\user\Python), copier aussi le repertoire du fichier scripts (exp: c:\users\Python\scripts)
aller sur Poste de travail, clique droit, cliquer sur propriété, cliquer sur "outils system avancée", puis "envirenement variables..", dans system variables choisir PATH, cliquer sur modifier, ajouter les deux liens ( C:\user\Python, et C:\users\Python\scripts ), tout enregistrer.
ouvrir l'invité de commande (la bare de recherche windows, ecrire cmd)
ecrire "python" puis entrée 
la version de python s'affiche Python 3.10.2 --> python est bien installer la machine
ecrire quit() puis entrée pour en sortir
ecrire pip puis entrée --> les options de la commande pip s'affichent, c'est qu'il est est bien installer et il est possible d'installer d'autres programmes maintenant.

telecharger Pycharm sur le site https://www.jetbrains.com/pycharm/download/ et prendre la version community
au moment de l'installation il est possible que le repertoire du fichier python.exe soit demandé.

apres l'ouverture de pycharm, aller sur file, crée un projet, entrée la localisation du projet souhaité et précisez le lien de l'interprete cad le lien vers (phython.exe)

clique droit sur le projet a gauche, nouveau, python projet, entrée un nom MyPythonProgram 
clique droit sur le projet python et nouveau, fichier python, entrée un nom HelloWorld
ecrire sur le fichier, print("Hello World")
clique droit sur la page, executer HelloWorld --> la fenetre de la console s'affiche avec en premier ligne le lien de l'interprete et le lien du fichier exécuté et en deuxieme ligne le mot Hello World.

pour telecharger chromdriver pour selenium
aller sur le site https://chromedriver.chromium.org/downloads
telechargé la Version 97.0.4692.99 (suivant votre version de chrome: aller sur les trois point en haut a droite, aide, a propos de chorme pour voir votre version)


pour installer selenium, ouvrir l'invité de commande
entrée pip install -U selenium
personnelement cette commande n'a pas fonctionner chez moi. j'ai crée un nouveau fichier python, et ecris dessus

from selenium import webdriver
driver = webdriver.Chrome("C://selenium//chrome//")



