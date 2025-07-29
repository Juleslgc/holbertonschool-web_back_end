# Variable Annotations en Python

Ce projet est un mini-cours et démonstration de
l'utilisation des **annotations de type** (*variable
annotations*) en Python.  
Il montre comment rendre son code plus clair,
maintenable, et vérifiable avec des outils comme `mypy`.

---

## Introduction aux Variable Annotations

### Qu’est-ce qu’une variable annotation ?

En Python, les *variable annotations* permettent
d’indiquer le **type d’une variable** sans changer son
comportement à l'exécution.  
Elles sont utiles pour :
- documenter le code,
- aider à la relecture et à l’autocomplétion dans les IDE,
- détecter des erreurs de type avec des outils comme `mypy`.

---

### Syntaxe de base

```python
age: int = 25
nom: str = "Alice"
notes: list[int] = [14, 16, 18]
```

### Pourquoi c’est utile ?

- Plus lisible
- Moins d’erreurs
- Compatible avec les IDE et les outils comme mypy
- Aide à documenter les fonctions, classes et variables

### Exemple de fonction typée

```python
def moyenne(notes: list[int]) -> float:
    return sum(notes) / len(notes)
```

- `notes: list[int]` → une liste d'entiers
- `-> float` → retourne un flottant

### Exemple d’erreur détectée avec `mypy`

```python
def triple(x: int) -> int:
    return x * 3

resultat: str = triple(4)  # erreur de type
```

Analyse avec :

```bash
mypy fichier.py
```

Résultat :

```go
error: Incompatible types in assignment (expression has
type "int", variable has type "str")
```

## À retenir

| Syntaxe | Signification |
|  -----------------  |  ----------------------  |
| `nom: str = "Alice"` | Variable `nom` est une chaine |
| `notes: list[int]` | Liste d'entiers |
| `-> float` | Type de retour d’une fonction |
| `Optional[str]` | Peut être une chaîne ou None |
| `Union[int, float]` | Accepte int ou float |

## Auteur

Projet d'école Holberton réalisé par Jules.