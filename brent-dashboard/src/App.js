import React from 'react';
import PriceChart from './components/PriceChart';
import ChangePointTable from './components/ChangePointTable';

function App() {
  return (
    <div className="App">
      <h1>Brent Oil Price Change Point Analysis</h1>
      <PriceChart />
      <ChangePointTable />
    </div>
  );
}

export default App;
