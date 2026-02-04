import React, { useEffect, useState } from 'react';

export default function Leaderboard(){
  const [data, setData] = useState([]);
  const CODESPACE = process.env.REACT_APP_CODESPACE_NAME;
  const BASE = CODESPACE ? `https://${CODESPACE}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${BASE}/api/leaderboard/`;

  useEffect(()=>{
    console.log('Fetching Leaderboard from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Leaderboard response:', json);
        const items = json.results ? json.results : json;
        setData(items);
      })
      .catch(err => console.error('Leaderboard fetch error', err));
  },[]);

  return (
    <div>
      <h2>Leaderboard</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
