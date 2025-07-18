import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Enrollments() {
  const [enrollments, setEnrollments] = useState([]);
  const [form, setForm] = useState({ client_id: '', program_id: '' });

  useEffect(() => {
    fetchEnrollments();
  }, []);

  const fetchEnrollments = async () => {
    const res = await axios.get('http://127.0.0.1:5000/enrollments');
    setEnrollments(res.data);
  };

  const enroll = async (e) => {
    e.preventDefault();
    await axios.post('http://127.0.0.1:5000/enrollments', form);
    fetchEnrollments();
    setForm({ client_id: '', program_id: '' });
  };

  return (
    <div>
      <h2>Enrollments</h2>
      <form onSubmit={enroll}>
        <input placeholder="Client ID" value={form.client_id} onChange={e => setForm({...form, client_id: e.target.value})} />
        <input placeholder="Program ID" value={form.program_id} onChange={e => setForm({...form, program_id: e.target.value})} />
        <button type="submit">Enroll Client</button>
      </form>

      <ul>
        {enrollments.map(e => (
          <li key={e.id}>Client {e.client_id} → Program {e.program_id}</li>
        ))}
      </ul>
    </div>
  );
}

export default Enrollments;
