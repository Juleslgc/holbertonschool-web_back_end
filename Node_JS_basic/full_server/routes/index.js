import express from 'express';
import StudentsController from '../controllers/StudentsController.js';
import AppController from '../controllers/AppController.js';


const router = express.Router();

router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

router.use((_, res) => {
  res.setHeader('Content-Type', 'text/plain');
  res.status(404).send('Not Found\n');
});

export default router;
