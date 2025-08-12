# Introduction à NoSQL & MongoDB

## Environnement

- **OS :** Ubuntu 20.04 LTS
- **Python :** version 3.9
- **PyMongo** : version 4.8.0
- **MongoDB :** version 4.4

## Qu’est-ce que NoSQL ?

**NoSQL** = *Not Only SQL*
Un type de base de données qui ne repose pas uniquement sur le modèle relationnel (tables, lignes, colonnes).

Types courants :

- Document store (ex: MongoDB, CouchDB)
- Key-value store (ex: Redis)
- Column store (ex: Cassandra)
- Graph database (ex: Neo4j)

## Différences SQL vs NoSQL

| Aspect           | SQL (Relationnel) | NoSQL (Non-relationnel)           |
| ---------------- | ----------------- | --------------------------------- |
| Structure        | Tables fixes      | Flexible (JSON, clé-valeur, etc.) |
| Schéma           | Fixe              | Dynamique ou absent               |
| Scalabilité      | Verticale         | Horizontale                       |
| Langage requêtes | SQL               | API spécifique                    |
| Exemple          | MySQL, PostgreSQL | MongoDB, Redis                    |

## ACID

Garanties pour transactions fiables :

- **A**tomicité : tout ou rien

- **C**ohérence : état valide → état valide

- **I**solation : transactions indépendantes

- **D**urabilité : données persistantes

MongoDB est **ACID** au niveau d’un document, mais privilégie aussi **la scalabilité et la performance**.

## Document Storage

Les données sont stockées sous forme de **documents JSON/BSON** :

```json
{
  "_id": 1,
  "nom": "Dupont",
  "age": 29,
  "adresses": [
    {"ville": "Paris", "cp": "75001"},
    {"ville": "Lyon", "cp": "69001"}
  ]
}
```

## Avantages NoSQL

- Flexible : pas de schéma rigide
- Scalable : facile à distribuer
- Rapide : optimisé pour gros volumes
- Naturel : données proches des structures JSON

## Utiliser MongoDB avec PyMongo

### Connexion

```py
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["ma_base"]
collection = db["utilisateurs"]
```

### Insertion 

```py
collection.insert_one({"nom": "Dupont", "age": 29})
collection.insert_many([
    {"nom": "Martin", "age": 32},
    {"nom": "Durand", "age": 25}
])
```

### Lecture

```py
# Tous les documents
for doc in collection.find():
    print(doc)

# Filtrer
for doc in collection.find({"age": {"$gt": 25}}):
    print(doc)
```

### Mise à jour

```py
collection.update_one({"nom": "Martin"}, {"$set": {"age": 33}})
collection.update_many({"age": {"$lt": 30}}, {"$inc": {"age": 1}})
```

### Suppression

```py
collection.delete_one({"nom": "Martin"})
collection.delete_many({"age": {"$lt": 25}})
```

## Commandes MongoDB Shell essentielles

```bash
show dbs                               # Voir bases de données
use ma_base                            # Sélectionner/créer base
db.createCollection("utilisateurs")    # Créer collection
db.utilisateurs.insertOne({...})       # Ajouter un document
db.utilisateurs.find()                  # Lister documents
db.utilisateurs.find({age: {$gt: 25}})  # Filtrer
db.utilisateurs.updateOne({...}, {...}) # Mettre à jour
db.utilisateurs.deleteOne({...})        # Supprimer
db.utilisateurs.createIndex({nom: 1})   # Index sur "nom"
```
