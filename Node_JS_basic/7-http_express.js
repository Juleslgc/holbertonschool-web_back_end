const express = require('express');
const fs = require('fs').promises;

const app = express();
const port = 1245;

async function countStudents(database) {
  try {
    const data = await fs.readFile(database, 'utf8');
    const lines = data.trim().split('\n');
    const headers = lines[0].split(',');
    const students = [];

    for (let i = 1; i < lines.length; i += 1) {
      const value = lines[i].split(',');
      const obj = {};
      headers.forEach((header, index) => {
        obj[header] = value[index];
      });
      students.push(obj);
    }
    let out = `Number of students: ${students.length}\n`;

    const csStudents = students.filter((student) => student.field === 'CS');
    const csName = csStudents.map((student) => student.firstname);
    out += `Number of students in CS: ${csStudents.length}. List: ${csName.join(', ')}\n`;

    const sweStudents = students.filter((student) => student.field === 'SWE');
    const sweName = sweStudents.map((student) => student.firstname);
    out += `Number of students in SWE: ${sweStudents.length}. List: ${sweName.join(', ')}`;

    return out;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    res.set('Content-Type', 'text/plain');
    const result = await countStudents('database.csv');
    res.status(200).send(`This is the list of our students\n${result}`);
  } catch (err) {
    console.error(err);
    res.status(500).send('Cannot load the database');
  }
});

app.use((req, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(404).send('Not Found');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
module.exports = app;
