import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ReferenceDot } from 'recharts';
import axios from 'axios';

const PriceChart = () => {
  const [prices, setPrices] = useState([]);
  const [changePoints, setChangePoints] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/prices").then(res => setPrices(res.data));
    axios.get("http://localhost:5000/api/change-points").then(res => setChangePoints(res.data));
  }, []);

  return (
    <div>
      <h3>Brent Oil Price Chart</h3>
      <LineChart width={1000} height={400} data={prices}>
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="Price" stroke="#8884d8" />
        {changePoints.map((cp, idx) => (
          <ReferenceDot key={idx} x={cp.date} y={null} label={cp.event} r={5} stroke="red" />
        ))}
      </LineChart>
    </div>
  );
};

export default PriceChart;
