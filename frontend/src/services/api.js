import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

export const getMasterRoutine = async () => {
  const res = await api.get('/routine/');
  return res.data;
}

// export const getFaculties = async () => {
//   const response = await api.get(`/faculties/`);
//   return response.data;
// };

// export const getCourses = async () => {
//   const response = await api.get(`/courses/`);
//   return response.data;
// };

// export const getClassrooms = async () => {
//   const response = await api.get(`/classrooms/`);
//   return response.data;
// };

// export const getPeriods = async () => {
//   const response = await api.get(`/periods/`);
//   return response.data;
// };

// export const addRoutine = async (routineData) => {
//   await api.post(`/master-routine/`, routineData);
// };

export default api;
