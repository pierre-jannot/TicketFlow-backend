# README du backend projet

## Installation de FastAPI et Uvicorn

pip install fastapi uvicorn

## Lancement du serveur uvicorn

Dans le dossier TicketFlow, avec l'invite de commandes :

uvicorn main:app --reload

L'API est alors hébergée sur http://127.0.0.1:8000

## Endpoints

Dans main.py :

Endpoint GET permettant l'affichage des tickets :
Chemin : /tickets

Endpoint POST permettant de trier et filtrer les tickets :
Chemin : /tickets/sort
Valeurs attendues : Objet SortAndFilter avec la méthode de tri et les tags de filtres

Endpoint POST permettant l'ajout d'un ticket :
Chemin : /tickets
Valeurs attendues : Objet NewTicket avec les valeurs du titre, de la description, de la priorité et des tags

Endpoint PATCH permettant la mise à jour de la priorité d'un ticket :
Chemin : /tickets/{id}     -     {id} étant l'id du ticket à mettre à jour
Valeurs attendues : Objet UpdateTicket avec la valeur de la priorité

Endpoint DELETE permettant la suppression d'un ticket :
Chemin : /tickets/{id}     -     {id} étant l'id du ticket à supprimer