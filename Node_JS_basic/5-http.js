const fs = require('fs').promises;
const http = require('http');

const host = 'localhost';
const port = '1245';

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

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Conetent-Type', 'text/plain');
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const result = await countStudents('database.csv');
      res.end(`This is the list of our students\n${result}`);
    } catch (err) {
      console.error(err);
      res.statusCode = 500;
      res.end('Cannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}`);
});
