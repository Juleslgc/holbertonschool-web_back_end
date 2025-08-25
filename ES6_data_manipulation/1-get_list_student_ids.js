export default function getListStudentIds(value) {
  if (!Array.isArray(value)) {
    return [];
  }
  return value.map((o) => o.id);
}
