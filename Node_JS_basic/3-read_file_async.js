const fs = require('fs').promises;

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
    console.log(`Number of students: ${students.length}`);

    const csStudents = students.filter((student) => student.field === 'CS');
    const csName = csStudents.map((student) => student.firstname);
    console.log(`Number of students in CS: ${csStudents.length}. List: ${csName.join(', ')}`);

    const sweStudents = students.filter((student) => student.field === 'SWE');
    const sweName = sweStudents.map((student) => student.firstname);
    console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweName.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
