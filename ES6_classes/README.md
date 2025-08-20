# ES6 Classes & Object-Oriented Programming (POO)

Ce document explique les **bases des classes en ES6** et de la **programmation orientée objet (POO)** en JavaScript.  

---

## 1. Comment définir une classe
En ES6, une classe se définit avec le mot-clé `class` et possède un constructeur (`constructor`) pour initialiser ses propriétés.  

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

const alice = new Person("Alice", 25);
console.log(alice.name); // Alice
```
## 2. Comment ajouter des méthodes à une classe

On ajoute des méthodes directement à l’intérieur de la classe. Elles seront accessibles sur toutes les instances.

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  introduce() {
    return `Hello, my name is ${this.name}`;
  }
}

const bob = new Person("Bob");
console.log(bob.introduce()); // Hello, my name is Bob
```

## 3. Pourquoi et comment ajouter une méthode statique à une classe

- Une méthode statique appartient à la classe elle-même, et non à ses instances.

- Elle est utilisée pour des opérations utilitaires ou liées à la classe, pas à un objet précis.

```js
class MathUtils {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathUtils.add(5, 3)); // 8
// ⚠️ Impossible d’appeler via une instance : new MathUtils().add() ❌
```

## 4. Comment étendre une classe à partir d'une autre

On peut créer une **classe enfant** qui hérite d’une classe parente grâce au mot-clé `extends`.
On utilise `super()` pour appeler le constructeur parent.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks: Woof!`);
  }
}

const rex = new Dog("Rex");
rex.speak(); // Rex barks: Woof!
```

## 5. Métaprogrammation et symboles

- Les Symbols créent des identifiants uniques.

- Utile pour ajouter des propriétés "cachées" ou éviter les conflits de noms.

- Ils sont souvent utilisés en métaprogrammation (code qui manipule du code).

```js
const id = Symbol("id");

class User {
  constructor(name) {
    this.name = name;
    this[id] = Math.random(); // identifiant unique
  }

  getId() {
    return this[id];
  }
}

const u1 = new User("Alice");
const u2 = new User("Bob");

console.log(u1.getId()); // identifiant unique différent de u2
console.log(Object.keys(u1)); // ["name"] → la clé Symbol est "cachée"
```

## 6. Résumé rapide

- `class` → définit une classe.

- `constructor` → initialise les attributs.

- `Méthodes classiques` → ajoutées dans le corps de la classe.

- `static` → définit une méthode ou propriété de classe (utilisée sans instance).

- `extends` → permet l’héritage.

- `super()` → appelle le constructeur ou les méthodes de la classe parente.

- `Symbol()` → crée une clé unique, utile pour de la métaprogrammation.

## Auteur

Projet d'école Holberton réalisé par Jules.