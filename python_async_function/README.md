# 🚀 Projet d'apprentissage Asyncio en Python

Ce projet est un bac à sable pour apprendre la **programmation asynchrone en Python** avec les mots-clés `async`, `await`, et le module `asyncio`.

Il inclut aussi :
- L’exécution de programmes asynchrones avec `asyncio.run()`
- L’exécution concurrente de coroutines avec `asyncio.gather()`
- La création et la gestion de tâches asynchrones avec `asyncio.create_task()`
- L’utilisation du module `random` pour simuler des délais

---

## 📘 Objectifs d'apprentissage

### 1. Syntaxe `async` et `await`

- `async def` permet de définir une **coroutine**.
- `await` suspend l’exécution **sans bloquer** le reste du programme.

```python
async def my_coroutine():
    await asyncio.sleep(1)
    print("Finished")
```
### 2. Exécuter un programme async

On utilise `asyncio.run()` pour lancer une fonction asynchrone principale :

```python
async def main():
    await ma_coroutine()

asyncio.run(main())
```

### 3. Exécuter plusieurs coroutines en parallèle

Avec `asyncio.gather()`, on peut exécuter plusieurs coroutines en même temps :

```python
await asyncio.gather(
    my_coroutine(),
    another_coroutine(),
)
```

### 4. Créer des tâches asynchrones

`asyncio.create_task()` permet de lancer une coroutine en tâche de fond :

```python
task = asyncio.create_task(my_coroutine())
await task
```
C’est utile pour démarrer plusieurs opérations indépendantes.

### Utilisation du module `random`

Pour simuler des temps d’attente aléatoires :

```python
import random

delay = random.uniform(1.0, 3.0)
await asyncio.sleep(delay)
```

## Pourquoi apprendre ça ?

La programmation asynchrone est essentielle pour écrire des programmes :

- Réactifs (serveurs web, bots, APIs)

- Qui gèrent beaucoup d’opérations d'entrée/sortie (fichiers, internet, base de données)

- Qui ne doivent pas se bloquer en attendant une réponse

## Résumé rapide

| Concept                           | Description                                                     | Exemple clé                              |
| --------------------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| `async def`                       | Déclare une **fonction asynchrone** (coroutine)                 | `async def fonction():`                  |
| `await`                           | **Attend** une opération asynchrone sans bloquer le programme   | `await asyncio.sleep(1)`                 |
| `asyncio.run()`                   | Lance la boucle d’événement principale et exécute une coroutine | `asyncio.run(main())`                    |
| `asyncio.gather()`                | Lance **plusieurs coroutines en parallèle** et attend leur fin  | `await asyncio.gather(coro1(), coro2())` |
| `asyncio.create_task()`           | Crée une **tâche asynchrone** exécutable indépendamment         | `t = asyncio.create_task(coro())`        |
| `random.uniform(a, b)`            | Génère un float aléatoire entre `a` et `b`                      | `random.uniform(1, 3)`                   |
| `asyncio.sleep(n)`                | Simule un **temps d’attente non bloquant**                      | `await asyncio.sleep(2)`                 |
| Coroutine                         | Fonction async pouvant être **suspendue et reprise**            | `async def tâche(): ...`                 |
| Boucle d’événement (`event loop`) | Gère et planifie l’exécution des coroutines                     | Automatique avec `asyncio.run()`         |

## Auteur

Projet d'école Holberton réalisé par Jules.
