# JavaScript ES6 - Promises & Async/Await

## 1. Qu’est-ce qu’une Promise ?

Une Promise est un objet qui représente une opération asynchrone, et sa valeur future.

- Elle permet de gérer le succès ou l’échec d’une opération asynchrone de manière plus lisible que les callbacks.

Une Promise peut être dans trois états :

- Pending – en attente

- Fulfilled – réussie

- Rejected – rejetée (erreur)

Exemple simple

```js
const promise = new Promise((resolve, reject) => {
  const success = true;
  if (success) {
    resolve("Opération réussie !");
  } else {
    reject("Erreur !");
  }
});
```

## 2. Pourquoi utiliser les Promises ?

- Éviter le callback hell (enchaînement de callbacks imbriqués).

- Avoir un flux lisible et prévisible pour les opérations asynchrones.

- Permettre un chaînage propre avec .then() et .catch().

## 3. Utiliser `.then()`, `.catch()` et `.finally()`

- `.then()` → exécute une fonction si la Promise est résolue (`resolve`).

- `.catch()` → exécute une fonction si la Promise est rejetée (`reject`).

- `.finally()` → s’exécute toujours, quel que soit le résultat.

```js
promise
  .then(result => console.log("Succès :", result))
  .catch(error => console.log("Erreur :", error))
  .finally(() => console.log("Opération terminée"));
```

## 4. Les méthodes statiques de `Promise`

- `Promise.all([p1, p2, ...])` → attend que toutes les Promises soient résolues.

- `Promise.race([p1, p2, ...])` → renvoie la première Promise résolue ou rejetée.

- `Promise.allSettled([p1, p2, ...])` → renvoie le statut de toutes les Promises, résolues ou rejetées.

- `Promise.any([p1, p2, ...])` → renvoie la première Promise réussie.

Exemple

```js
const p1 = Promise.resolve(10);
const p2 = Promise.resolve(20);

Promise.all([p1, p2]).then(results => console.log(results)); // [10, 20]
```

## 5. Gestion d’erreurs avec `try` / `catch` et `throw`

- `throw` → permet de lancer une erreur.

- `try / catch` → permet de gérer les erreurs synchrones ou asynchrones (avec await).

```js
try {
  throw new Error("Une erreur survient !");
} catch (err) {
  console.log(err.message); // "Une erreur survient !"
}
```

## 6. `async` et `await`

- Une fonction `async` retourne toujours une Promise.

- `await` permet de mettre en pause l’exécution jusqu’à ce que la Promise soit résolue.

- Permet d’écrire un code asynchrone comme s’il était synchrone.

Exemple

```js
async function fetchData() {
  try {
    const data = await fetch("https://jsonplaceholder.typicode.com/todos/1")
      .then(res => res.json());
    console.log(data);
  } catch (err) {
    console.log("Erreur :", err);
  }
}

fetchData();
```
- Ici, `await` attend la réponse de `fetch` avant de continuer.

- Les erreurs sont gérées avec `try / catch`.

## 7. Exemple complet : Promises + async/await

```js
// Fonction qui retourne une Promise
function delay(ms) {
  return new Promise((resolve) => setTimeout(() => resolve("Terminé !"), ms));
}

// Avec then / catch
delay(1000)
  .then(msg => console.log("Then :", msg))
  .catch(err => console.log("Catch :", err));

// Avec async / await
async function run() {
  try {
    const msg = await delay(1000);
    console.log("Await :", msg);
  } catch (err) {
    console.log("Erreur :", err);
  }
}

run();
```

## Résumé

| Concept          | Utilité                                   |
| ---------------- | ----------------------------------------- |
| `Promise`        | Représente une opération asynchrone       |
| `.then()`        | Exécute si réussite                       |
| `.catch()`       | Exécute si erreur                         |
| `.finally()`     | Toujours exécuté                          |
| `Promise.all()`  | Attendre toutes les Promises              |
| `Promise.race()` | Première Promise résolue ou rejetée       |
| `async`          | Déclarer une fonction asynchrone          |
| `await`          | Pause jusqu’à la résolution d’une Promise |
| `try / catch`    | Gérer les erreurs                         |
| `throw`          | Lancer une erreur                         |

## Auteur

Projet d'école Holberton réalisé par Jules.
