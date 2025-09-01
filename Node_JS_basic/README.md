# 📘 Introduction à Node.js et Express.js

Ce document présente les bases pour travailler avec **Node.js** et **Express.js**, ainsi que quelques outils pratiques pour développer plus rapidement.

---

## 🚀 1. Exécuter du JavaScript avec Node.js

Node.js permet d’exécuter du **JavaScript côté serveur**.

```bash
node app.js
```

**Exemple :**

```js
console.log("Hello Node.js !");
```

---

## 📦 2. Utiliser les modules Node.js

* **Modules natifs** (fournis avec Node) : `fs`, `http`, etc.
* **Modules tiers** (installés avec npm) : `express`, etc.
* **Modules personnalisés** : créés par vous-même.

**Exemple :**

```js
// math.js
function add(a, b) {
  return a + b;
}
module.exports = add;

// app.js
const add = require("./math.js");
console.log(add(2, 3));
```

---

## 📂 3. Lire des fichiers avec le module `fs`

```js
const fs = require("fs");

fs.readFile("test.txt", "utf8", (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

---

## ⚙️ 4. Utiliser `process`

* **Arguments de la ligne de commande** :

```js
console.log(process.argv);
```

* **Variables d’environnement** :

```js
console.log(process.env.USER);
```

---

## 🌐 5. Créer un serveur HTTP avec Node.js

```js
const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("Hello, Node.js Server!");
});

server.listen(3000, () => console.log("Serveur sur http://localhost:3000"));
```

---

## ⚡ 6. Créer un serveur avec Express.js

```bash
npm install express
```

```js
const express = require("express");
const app = express();

app.get("/", (req, res) => {
  res.send("Hello Express.js !");
});

app.listen(3000, () => console.log("Express sur http://localhost:3000"));
```

---

## 🛣️ 7. Créer des routes avancées avec Express.js

```js
const express = require("express");
const app = express();

app.get("/users", (req, res) => {
  res.json([{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }]);
});

app.get("/user/:id", (req, res) => {
  res.send(`Utilisateur ${req.params.id}`);
});

app.post("/user", (req, res) => {
  res.send("Nouvel utilisateur créé !");
});

app.listen(3000, () => console.log("API sur http://localhost:3000"));
```

---

## ✨ 8. Utiliser ES6 avec Babel

### Installation

```bash
npm install @babel/core @babel/cli @babel/preset-env @babel/node --save-dev
```

### Configurer `.babelrc`

```json
{
  "presets": ["@babel/preset-env"]
}
```

### Exemple avec `import/export`

```js
// math.js
export function add(a, b) {
  return a + b;
}

// app.js
import { add } from "./math.js";
console.log(add(4, 5));
```

Exécution :

```bash
npx babel-node app.js
```

---

## 🔄 9. Utiliser Nodemon

Nodemon redémarre automatiquement l’application à chaque modification.

### Installation

```bash
npm install -g nodemon
```

### Utilisation

```bash
nodemon app.js
```

---

## ✅ Résumé

* **Node.js** → exécuter du JS côté serveur.
* **Modules** → natifs, tiers, personnalisés.
* **`fs`** → gérer les fichiers.
* **`process`** → arguments & variables d’environnement.
* **http** → serveur basique.
* **Express** → serveur + API.
* **Babel** → support ES6+.
* **Nodemon** → redémarrage automatique.

---

🚀 Avec ces bases, vous pouvez déjà créer une **API REST complète** et la développer rapidement.

