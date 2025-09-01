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
    process.stdout.write(`Number of students: ${students.length}\n`);

    const csStudents = students.filter((student) => student.field === 'CS');
    const csName = csStudents.map((student) => student.firstname);
    const csfield = csStudents.length > 0 ? csStudents[0].field : 'CS';
    process.stdout.write(`Number of students in ${csfield}: ${csStudents.length}. List: ${csName.join(', ')}\n`);

    const sweStudents = students.filter((student) => student.field === 'SWE');
    const sweName = sweStudents.map((student) => student.firstname);
    const swefield = sweStudents.length > 0 ? sweStudents[0].field : 'SWE';
    process.stdout.write(`Number of students in ${swefield}: ${sweStudents.length}. List: ${sweName.join(', ')}\n`);
  }
}
module.exports = countStudents;
