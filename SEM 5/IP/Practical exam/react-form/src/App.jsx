import { useState } from "react";
import Profile from "./Profile.jsx";

export default function App(){
  const [name, setName] = useState("");
  const [items, setItems] = useState([]);
  const [age, setAge] = useState(20);
  function add(){
    if(name.trim().length < 3) return alert("min 3 chars");
    setItems(prev => [...prev, {id: Date.now(), text: name.trim()}]); 
    setName("");
  }
  return (
   
      <div style={{padding:20}}>
        <Profile name="Zaheen" age={age}/>
        <button onClick={()=>setAge(a=>a+1)}>Increase age</button>
        <h2>React Form</h2>
        <input value={name} onChange={e=>setName(e.target.value)} placeholder="name"/>
        <button onClick={add}>Add</button>
        <ul>{items.map(it => <li key={it.id}>{it.text} ({new Date(it.id).toLocaleTimeString()})</li>)}</ul>
      </div>
   
  );
}
