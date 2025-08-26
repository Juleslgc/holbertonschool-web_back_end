# ES6 - data manipulation

## Introduction

Avec ES6 (ECMAScript 2015), JavaScript a introduit de nombreuses fonctionnalités pour manipuler les données de manière plus concise et expressive.
Ce guide couvre les principales techniques pour travailler avec les tableaux, les objets, les Map, les Set, ainsi que les Typed Arrays.

## 1. Manipulation des tableaux

### 1.1 `map()`

Transforme chaque élément d’un tableau et retourne un nouveau tableau.

```js
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]
```

### 1.2 `filter()`

Filtre les éléments selon une condition et retourne un nouveau tableau.

```js
const numbers = [1, 2, 3, 4];
const even = numbers.filter(n => n % 2 === 0); // [2, 4]
```

### 1.3 `reduce()`


Réduit un tableau à une seule valeur en appliquant une fonction cumulatrice.

```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((acc, n) => acc + n, 0); // 10
```

## 2. Typed Arrays

Les Typed Arrays permettent de manipuler des données binaires de manière efficace.

Exemples :

- `Int8Array` : entiers signés de -128 à 127

- `Uint8Array` : entiers non signés de 0 à 255

- `Float32Array` : nombres flottants 32 bits

Exemple :

```js
const buffer = new ArrayBuffer(4); // 4 octets
const int8 = new Int8Array(buffer);

int8[0] = 100;
int8[1] = -50;

console.log(int8); // Int8Array [100, -50, 0, 0]
```

### DataView

Permet de lire/écrire différents types sur un même ArrayBuffer.

```js
const buffer = new ArrayBuffer(4);
const view = new DataView(buffer);

view.setInt8(0, 127);
view.setUint16(1, 500);

console.log(view.getInt8(0));  // 127
console.log(view.getUint16(1)); // 500
```

## 3. Structures de données ES6

### 3.1 `Set`

Collection de valeurs uniques.

```js
const fruits = new Set(["pomme", "banane"]);
fruits.add("orange");
console.log(fruits.has("pomme")); // true
```

### 3.2 `Map`

Collection de paires clé → valeur.

```js
const dict = new Map();
dict.set("chien", "dog");
dict.set("chat", "cat");

console.log(dict.get("chien")); // "dog"
console.log(dict.has("chat"));  // true
```

## 4. Trucs et astuces

- Vérifier si une variable est un tableau :

```js
Array.isArray(myArray); // true ou false
```

- Couper une chaîne :

```js
const text = "Bonjour le monde";
text.slice(0, 7); // "Bonjour"
text.startsWith("Bonjour"); // true
```

- Mettre à jour un Map :

```js
const map = new Map([["a", 1]]);
map.set("a", 100); // update
```

- Filtrer et transformer un tableau combiné :

```js
const students = [
  { id: 1, city: "Paris" },
  { id: 2, city: "London" }
];

const parisStudents = students
  .filter(s => s.city === "Paris")
  .map(s => ({ ...s, grade: "N/A" }));
```

## Auteur

Projet d'école Holberton réalisé par Jules.
