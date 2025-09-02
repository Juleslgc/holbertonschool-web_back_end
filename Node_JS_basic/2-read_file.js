const fs = require('fs');

function countStudents(database) {
  if (!fs.existsSync(database)) {
    throw new Error('Cannot load the database');
  } else {
    const data = fs.readFileSync(database, 'utf8');
    const lines = data.trim().split('\n'); // Séparer les lignes
    const headers = lines[0].split(','); // Première ligne = noms des colonnes
    const students = [];
    for (let i = 1; i < lines.length; i += 1) {
      const values = lines[i].split(',');
      const obj = {};
      headers.forEach((header, index) => {
        obj[header] = values[index];
      });
      students.push(obj);
    }
    console.log(`Number of students: ${students.length}`);

    const csStudents = students.filter((student) => student.field === 'CS');
    const csName = csStudents.map((student) => student.firstname);
    console.log(`Number of students in CS: ${csStudents.length}. List: ${csName.join(', ')}`);

    const sweStudents = students.filter((student) => student.field === 'SWE');
    const sweName = sweStudents.map((student) => student.firstname);
    console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweName.join(', ')}`);
  }
}
module.exports = countStudents;
