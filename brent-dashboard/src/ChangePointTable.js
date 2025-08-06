import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ChangePointTable = () => {
  const [changePoints, setChangePoints] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/change-points").then(res => setChangePoints(res.data));
  }, []);

  return (
    <div>
      <h3>Detected Change Points</h3>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Event</th>
            <th>Mu Before</th>
            <th>Mu After</th>
          </tr>
        </thead>
        <tbody>
          {changePoints.map((cp, idx) => (
            <tr key={idx}>
              <td>{cp.date}</td>
              <td>{cp.event}</td>
              <td>{cp.mu_before.toFixed(4)}</td>
              <td>{cp.mu_after.toFixed(4)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ChangePointTable;
