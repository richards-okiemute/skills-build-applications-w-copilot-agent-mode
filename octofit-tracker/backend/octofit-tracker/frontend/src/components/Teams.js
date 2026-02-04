import React, { useEffect, useState } from 'react';

export default function Teams(){
  const [data, setData] = useState([]);
  const CODESPACE = process.env.REACT_APP_CODESPACE_NAME;
  const BASE = CODESPACE ? `https://${CODESPACE}-8000.app.github.dev` : 'http://localhost:8000';
  const endpoint = `${BASE}/api/teams/`;

  useEffect(()=>{
    console.log('Fetching Teams from', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        console.log('Teams response:', json);
        const items = json.results ? json.results : json;
        setData(items);
      })
      .catch(err => console.error('Teams fetch error', err));
  },[]);

  return (
    <div>
      <h2>Teams</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
