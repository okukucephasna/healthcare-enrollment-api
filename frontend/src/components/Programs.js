import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Clients() {
  const [clients, setClients] = useState([]);
  const [form, setForm] = useState({ name: '', age: '', gender: '' });

  useEffect(() => {
    fetchClients();
  }, []);

  const fetchClients = async () => {
    const res = await axios.get('http://127.0.0.1:5000/clients');
    setClients(res.data);
  };

  const addClient = async (e) => {
    e.preventDefault();
    await axios.post('http://127.0.0.1:5000/clients', form);
    fetchClients();
    setForm({ name: '', age: '', gender: '' });
  };

  return (
    <div>
      <h2>Clients</h2>
      <form onSubmit={addClient}>
        <input placeholder="Name" value={form.name} onChange={e => setForm({...form, name: e.target.value})} />
        <input placeholder="Age" value={form.age} onChange={e => setForm({...form, age: e.target.value})} />
        <input placeholder="Gender" value={form.gender} onChange={e => setForm({...form, gender: e.target.value})} />
        <button type="submit">Add Client</button>
      </form>

      <ul>
        {clients.map(c => (
          <li key={c.id}>{c.name} - {c.age} - {c.gender}</li>
        ))}
      </ul>
    </div>
  );
}

export default Clients;
