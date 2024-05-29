export default function updateStudentGradeByCity(ids, city, newGrades) {
  return ids
    .filter((id) => id.location === city)
    .map((student) => {
      const gradeObject = newGrades.find((grade) => grade.studentId === student.id);
      const grade = gradeObject ? gradeObject.grade : 'N/A';
      return { ...student, grade };
    });
}
