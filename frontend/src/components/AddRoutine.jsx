import React, { useEffect, useState } from "react";
import { getFaculties, getCourses, getClassrooms, getPeriods, addRoutine } from "../services/api";

const AddRoutine = () => {
  const [formData, setFormData] = useState({
    faculty: "",
    course: "",
    classroom: "",
    period: "",
    day: "",
  });

  const [faculties, setFaculties] = useState([]);
  const [courses, setCourses] = useState([]);
  const [classrooms, setClassrooms] = useState([]);
  const [periods, setPeriods] = useState([]);

  // Fetching required data for dropdowns
  useEffect(() => {
    const fetchData = async () => {
      try {
        setFaculties(await getFaculties());
        setCourses(await getCourses());
        setClassrooms(await getClassrooms());
        setPeriods(await getPeriods());
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    fetchData();
  }, []);

  console.log('fac',faculties)
  console.log('coruse',courses)
  console.log('rooo,',classrooms)
  console.log('perid',periods)

  // Handling input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Submitting the routine
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addRoutine(formData);
      alert("Routine added successfully!");
      setFormData({ faculty: "", course: "", classroom: "", period: "", day: "" });
    } catch (error) {
      console.error("Error adding routine:", error);
      alert("Failed to add routine.");
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white shadow-md rounded-md">
      <h2 className="text-xl font-semibold mb-4">Add Routine</h2>
      <form onSubmit={handleSubmit}>
        {/* Faculty */}
        <label className="block mb-2">Faculty:</label>
        <select name="faculty" value={formData.faculty} onChange={handleChange} required className="w-full p-2 mb-4 border rounded">
          <option value="">Select Faculty</option>
          {faculties.map((fac) => (
            <option key={fac.id} value={fac.id}>{fac.faculty_name}</option>
          ))}
        </select>

        {/* Course */}
        <label className="block mb-2">Course:</label>
        <select name="course" value={formData.course} onChange={handleChange} required className="w-full p-2 mb-4 border rounded">
          <option value="">Select Course</option>
          {courses.map((course) => (
            <option key={course.id} value={course.id}>{course.course_no} - {course.course_title}</option>
          ))}
        </select>

        {/* Classroom */}
        <label className="block mb-2">Classroom:</label>
        <select name="classroom" value={formData.classroom} onChange={handleChange} required className="w-full p-2 mb-4 border rounded">
          <option value="">Select Classroom</option>
          {classrooms.map((room) => (
            <option key={room.id} value={room.id}>{room.classroom_no}</option>
          ))}
        </select>

        {/* Period */}
        <label className="block mb-2">Period:</label>
        <select name="period" value={formData.period} onChange={handleChange} required className="w-full p-2 mb-4 border rounded">
          <option value="">Select Period</option>
          {periods.map((p) => (
            <option key={p.id} value={p.id}>{p.start_time} - {p.end_time}</option>
          ))}
        </select>

        {/* Day */}
        <label className="block mb-2">Day:</label>
        <select name="day" value={formData.day} onChange={handleChange} required className="w-full p-2 mb-4 border rounded">
          <option value="">Select Day</option>
          {["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"].map((day) => (
            <option key={day} value={day}>{day}</option>
          ))}
        </select>

        {/* Submit Button */}
        <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
          Add Routine
        </button>
      </form>
    </div>
  );
};

export default AddRoutine;
