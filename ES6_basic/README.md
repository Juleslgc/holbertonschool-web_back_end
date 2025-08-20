# ES6 Basics – Introduction à ECMAScript 2015

## Qu’est-ce qu’ES6 ?

ES6 (aussi appelé ECMAScript 2015) est une version majeure de JavaScript qui a introduit de nombreuses nouvelles fonctionnalités rendant le code plus clair, puissant et moderne.

## Les nouveautés principales

### `let` et `const`

- `let` → variable réassignable (portée bloc).
- `const` → constante (non réassignable).

```js
let age = 25;
age = 26; // possible

const PI = 3.14;
PI = 3.1416; // erreur
```

### Fonctions fléchées (`=>`)

Syntaxe plus concise et `this` lié au contexte parent.

```js
const add = (a, b) => a + b;
```

Avec un seul argument :

```js
const square = x => x * x;
```

### Paramètres par défaut

```js
const greet = (name = "Invité") => `Bonjour, ${name}!`;

greet();       // Bonjour, Invité!
greet("Sam");  // Bonjour, Sam!
```

### Rest & Spread (`...`)

- Rest → regroupe les arguments en tableau

```js
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}
console.log(sum(1, 2, 3)); // 6
```

- Spread → décompose un tableau ou objet

```js
const arr = [1, 2, 3];
console.log(Math.max(...arr)); // 3
```

### Template literals (modèles littéraux)

Chaînes avec backticks `` ` `` → interpolation `${}` + multi-lignes.

```js
const name = "Alice";
console.log(`Bonjour, ${name}!`);
```

### Objets améliorés

Raccourcis et méthodes plus simples.

```js
const age = 25;
const user = {
  name: "Alice",
  age, // raccourci
  greet() {
    console.log(`Salut, je suis ${this.name}`);
  }
};
```

### Boucle `for...of`

Parcourir directement les valeurs d’un itérable.

```js
for (const fruit of ["pomme", "banane"]) {
  console.log(fruit);
}
```

### Modules (import/export)

Permet de découper le code en fichiers réutilisables.

```js
// math.js
export const add = (a, b) => a + b;

// main.js
import { add } from './math.js';
console.log(add(2, 3));
```

## Méthodes de variables

### Chaînes de caractères

```js
let texte = "Bonjour le monde";
```

**Méthodes utiles :**

- `texte.length` → longueur

- `texte.toUpperCase()`, `texte.toLowerCase()`

- `texte.includes("monde")` → true

- `texte.indexOf("monde")` → 8

- `texte.slice(0, 7`) → "Bonjour"

- `texte.replace("monde", "toi")`

- `texte.split(" ")` → ["Bonjour", "le", "monde"]

- `texte.trim()` → supprime espaces au début/fin

### Nombres

```js
let x = 42;
```

**Méthodes utiles :**

- `x.toFixed(2)` → "42.00"

- `x.toString()` → "42"

- `Number.isInteger(x)` → true

- `Math.round(x)`, `Math.floor(x)`, `Math.ceil(x)`

- `Math.random()`, `Math.max()`, `Math.min()`

### Tableaux

```js
let arr = [1, 2, 3, 4];
```

**Méthodes utiles :**

- `arr.length` → taille

- `arr.push(5)`, `arr.pop()` → ajouter/retirer fin

- `arr.shift()`, `arr.unshift(0)` → retirer/ajouter début

- `arr.map(x => x*2)` → [2,4,6,8]

- `arr.filter(x => x > 2)` → [3,4]

- `arr.reduce((a,b)=>a+b,0)` → 10

- `arr.find(x=>x>2)` → 3

- `arr.includes(3)` → true

- `arr.sort()`, `arr.reverse()`

- `arr.join(",")` → "1,2,3,4"

### Objets

```js
let user = { nom: "Alice", age: 25 };
```

**Méthodes utiles :**

- `Object.keys(user)` → ["nom", "age"]

- `Object.values(user)` → ["Alice", 25]

- `Object.entries(user)` → [["nom","Alice"], ["age",25]]

- `Object.assign({}, user, { ville: "Paris" })`

- `Object.hasOwn(user, "nom")` (ES2022)

### Booléens

```js
let actif = true;
```

**Méthodes utiles :**

- `actif.toString()` → "true"

- `Boolean(0)` → false (conversion)

### Dates

```js
let maintenant = new Date();
```

**Méthodes utiles :**

- `maintenant.getFullYear()`, `.getMonth()`, `.getDate()`

- `maintenant.getHours()`, `.getMinutes()`

- `maintenant.toISOString()`

- `Date.now()` → timestamp actuel

### Variables spéciales

N’ont pas de méthodes directes, mais peuvent être testées :
```js
if (variable === undefined) { ... }
if (variable === null) { ... }
```

## Auteur

Projet d'école Holberton réalisé par Jules.