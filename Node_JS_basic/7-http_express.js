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

app.get('/', (_, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.get('/students', async (_, res) => {
  const response = 'This is the list of our students\n';
  try {
    res.setHeader('Content-Type', 'text/plain');
    const result = await countStudents('database.csv');
    res.status(200).send(`${response}${result}`);
  } catch (err) {
    res.send(response + err.message);
  }
});

app.use((_, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.status(404).send('Not Found');
});

app.listen(port, () => {
  console.log(`Server running at http://127.0.0.1:${port}`);
});
module.exports = app;
