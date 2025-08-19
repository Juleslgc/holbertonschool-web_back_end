export default function createEmployeesObject(departmentName, employees) {
  const Job = {
    [`${departmentName}`]: employees,
  };
  return Job;
}
