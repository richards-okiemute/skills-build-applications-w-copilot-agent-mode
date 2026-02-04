import React, { useEffect, useState } from 'react';

export default function Workouts(){
  const [data, setData] = useState([]);
  const CODESPACE = process.env.REACT_APP_CODESPACE_NAME;
  const BASE = CODESPACE ? `https://${CODESPACE}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${BASE}/api/workouts/`;

  useEffect(()=>{
    console.log('Fetching Workouts from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Workouts response:', json);
        const items = json.results ? json.results : json;
        setData(items);
      })
      .catch(err => console.error('Workouts fetch error', err));
  },[]);

  return (
    <div>
      <h2>Workouts</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
