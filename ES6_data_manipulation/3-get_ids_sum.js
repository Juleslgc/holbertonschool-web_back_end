export default function getStudentIdsSum(list) {
  return list.reduce((acc, l) => acc + l.id, 0);
}
