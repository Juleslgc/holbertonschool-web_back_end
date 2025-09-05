import express from 'express';
import StudentsController from './StudentsController.js';

const app = express();
const PORT = 1245;

app.get('/students', StudentsController.getAllStudents);
app.get('/students/:major', StudentsController.getAllStudentsByMajor);

app.listen(PORT, () => {
  console.log(`Server running on http://127.0.0.1:${PORT}`);
});
