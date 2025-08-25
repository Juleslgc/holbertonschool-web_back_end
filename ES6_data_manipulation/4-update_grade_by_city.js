export default function updateStudentGradeByCity(list, city, newGrades) {
  const student = list.filter((l) => l.location === city);
  const students = student.map((s) => {
    let grade = 'N/A';
    for (const object of newGrades) {
      if (s.id === object.studentId) {
        grade = object.grade;
        break;
      }
    }
    return { ...s, grade };
  });
  return students;
}
