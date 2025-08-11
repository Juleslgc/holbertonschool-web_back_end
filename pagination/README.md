# Pagination

## Introduction
La **pagination** est une technique permettant de diviser un grand ensemble de données en plusieurs pages plus petites et plus faciles à consulter.  
Elle est utilisée dans les sites web, les applications mobiles, les API et même dans les documents imprimés.

---

## Objectifs
- Améliorer l'expérience utilisateur en évitant la surcharge visuelle.
- Réduire le temps de chargement en n'affichant que les données nécessaires.
- Faciliter la navigation et le repérage d’informations.

---

## Types de pagination

| Type | Description | Avantages | Inconvénients |
|------|-------------|-----------|---------------|
| **Classique** (numéros de page) | Navigation via liens numérotés ou boutons "Suivant/Précédent" | Simple, prévisible | Peut nécessiter plusieurs clics |
| **Défilement infini** | Chargement automatique lors du défilement | Immersion continue | Moins pratique pour rechercher un élément précis |
| **Bouton "Voir plus"** | Ajoute plus de contenu sans changer de page | Rapide et simple | Peut donner un effet de liste interminable |
| **Pagination par curseur** | Utilise un identifiant comme pointeur dans les requêtes | Performances optimales | Plus technique à implémenter |

---

## Exemple en SQL

### Pagination avec LIMIT et OFFSET
```sql
-- Page 2 avec 10 résultats par page
SELECT * 
FROM produits
ORDER BY id
LIMIT 10 OFFSET 10;
```

### Pagination avec curseur (plus performante)

```sql
SELECT *
FROM produits
WHERE id > 50
ORDER BY id
LIMIT 10;
```

## Schéma visuel

![schéma visuel](/pagination/image/Schéma_visuel.png)