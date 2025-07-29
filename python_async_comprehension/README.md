# Générateurs Asynchrones, Compréhensions Asynchrones et Typage en Python

## Introduction

Ce projet explique comment utiliser les générateurs asynchrones (`async generators`) en Python, comment exploiter les compréhensions asynchrones (`async comprehensions`) pour parcourir ces générateurs, ainsi que la manière de typer ces générateurs pour rendre le code plus clair et robuste.

---

## 1. Générateurs Asynchrones

Un générateur asynchrone est une fonction définie avec `async def` qui produit une série de valeurs de manière asynchrone grâce à l'instruction `yield`. Contrairement aux générateurs classiques, il peut inclure des opérations asynchrones (avec `await`) entre les valeurs produites.

### Exemple

```python
import asyncio
from typing import AsyncGenerator

async def compteur() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)  # Simulation d'une opération asynchrone
        yield i  # Production d'une valeur
```
Ce générateur produit un nombre toutes les secondes, sans bloquer l'exécution.

## 2. Compréhensions Asynchrones

Pour consommer un générateur asynchrone, on utilise la syntaxe `async for`. Les compréhensions asynchrones permettent de construire facilement des listes ou autres collections à partir d'itérables asynchrones.

### Exemple

```python
async def main():
    resultats = [x * 2 async for x in compteur()]
    print(resultats)

asyncio.run(main())
```
Ce code récupère toutes les valeurs produites par compteur, les double, et stocke le résultat dans une liste.

## 3. Typage des Générateurs Asynchrones

Pour annoter le type d'un générateur asynchrone, on utilise AsyncGenerator du module typing.

**Syntaxe :**
```python
from typing import AsyncGenerator

async def nom_fonction() -> AsyncGenerator[TypeDesValeurs, None]:
    ...
```

- Le premier paramètre indique le type des valeurs produites (`yield`).

- Le second paramètre est le type des valeurs pouvant être envoyées dans le générateur via `.asend()` (rarement utilisé, souvent `None`).

## Résumé

| Concept                  | Syntaxe / Exemple                                   | Description                                                 |
| ------------------------ | --------------------------------------------------- | ----------------------------------------------------------- |
| Générateur asynchrone    | `async def gen() -> AsyncGenerator[int, None]: ...` | Produit des valeurs avec `yield` en async                   |
| Compréhension asynchrone | `[x async for x in gen()]`                          | Parcourt un générateur asynchrone pour construire une liste |
| Typage                   | `AsyncGenerator[TypeValeur, None]`                  | Annotation de type pour générateur asynchrone               |

## Conclusion

Les générateurs asynchrones et compréhensions asynchrones sont des outils puissants pour gérer des flux de données asynchrones efficacement en Python. Leur typage permet d'améliorer la qualité du code, notamment dans les projets complexes.

## Exemple complet

```python
import asyncio
from typing import AsyncGenerator

async def compteur() -> AsyncGenerator[int, None]:
    for i in range(5):
        await asyncio.sleep(1)
        yield i

async def main():
    resultats = [x * 2 async for x in compteur()]
    print(resultats)

asyncio.run(main())
```

## Auteur

Projet d'école Holberton réalisé par Jules.
