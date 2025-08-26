export default function hasValuesFromArray(set, array) {
  for (const object of array) {
    if (!set.has(object)) {
      return false;
    }
  }
  return true;
}
