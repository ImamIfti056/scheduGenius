import React, { useEffect, useState } from "react";
import { getMasterRoutine } from "../services/api";


// const routineData = [
//   {
//     day: 'Monday',
//     period: { period_no: '1', start_time: '08:00:00', end_time: '08:50:00' },
//     faculty: 'frh',
//     course: 'Solid State',
//     classroom: '101',
//   },
//   {
//     day: 'Monday',
//     period: { period_no: '2', start_time: '08:50:00', end_time: '09:40:00' },
//     faculty: 'John Doe',
//     course: 'Physics',
//     classroom: '102',
//   },
//   {
//     day: 'sunday',
//     period: { period_no: '2', start_time: '08:50:00', end_time: '09:40:00' },
//     faculty: 'John Doe',
//     course: 'Physics',
//     classroom: '102',
//   },
//   {
//     day: 'thursday',
//     period: { period_no: '5', start_time: '11:40:00', end_time: '12:30:00' },
//     faculty: 'John Doe',
//     course: 'cehmisity',
//     classroom: '102',
//   },
//   {
//     day: 'wednesday',
//     period: { period_no: '4', start_time: '10:50:00', end_time: '11:40:00' },
//     faculty: 'John Doe',
//     course: 'Physics',
//     classroom: '102',
//   },
//   // Add more entries here for other days and periods...
// ];

const Routine = () => {
  const [routineData, setRoutineData] = useState([]);

  useEffect(() => {
    const fetchMasterRoutine = async () => {
      try {
        const data = await getMasterRoutine();
        setRoutineData(data.routines);
      } catch (error) {
        console.error('Error fetching master routine:', error);
      }
    };

    fetchMasterRoutine();
  }, []);
  console.log(routineData)

  // Function to group routine data by day and sort by time
  const groupByDayAndSortByTime = () => {
    const grouped = {};
    routineData.forEach((entry) => {
      // Group by day
      if (!grouped[entry.day]) {
        grouped[entry.day] = [];
      }
      grouped[entry.day].push(entry);
    });

    // Sort the periods within each day by start time
    Object.keys(grouped).forEach((day) => {
      grouped[day].sort((a, b) => {
        return a.period.start_time.localeCompare(b.period.start_time);
      });
    });

    return grouped;
  };

  // Grouping and sorting the data by day and time
  const groupedData = groupByDayAndSortByTime();

  // Function to create dynamic time slots from the routine data
  const createTimeColumns = (dayData) => {
    const timeColumns = dayData.map((entry) => {
      return {
        period_no: entry.period.period_no,
        start_time: entry.period.start_time,
        end_time: entry.period.end_time,
        faculty: entry.faculty,
        course: entry.course,
      };
    });
    return timeColumns;
  };

  return (
    <table className="table">
      {/* Table Head */}
      <thead>
        <tr>
          <th>Day | Time</th>
          {routineData
            .map((entry) => entry.period)
            .sort((a, b) => a.start_time.localeCompare(b.start_time))
            .map((period, index) => (
              <th key={index}>
                {period.start_time.slice(0, 5)} - {period.end_time.slice(0, 5)}
              </th>
            ))}
        </tr>
      </thead>

      {/* Table Body */}
      <tbody>
        {/* Loop through each day */}
        {Object.keys(groupedData).map((day) => {
          const dayRoutine = groupedData[day];
          const timeColumns = createTimeColumns(dayRoutine);

          return (
            <tr key={day}>
              <th>{day}</th>
              {/* Render each period dynamically */}
              {timeColumns.map((column, index) => (
                <td key={index}>
                  {column.faculty} - {column.course}
                </td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default Routine;



//   useEffect(() => {
//     const fetchRoutines = async () => {
//       try {
//         const response = await api.get("/routine/");
//         setRoutines(response.data);
//       } catch (error) {
//         console.error("Error fetching routines:", error);
//       }
//     };

//     fetchRoutines();
//   }, []);