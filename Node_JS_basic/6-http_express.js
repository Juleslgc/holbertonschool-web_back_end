const express = require('express');

const app = express();
const port = 1245;

app.get('/', (_, res) => {
  res.set('Content-Type', 'text/plain');
  res.status(200).send('Hello Holberton School!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
module.exports = app;
