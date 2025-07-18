import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Clients from './components/Clients';
import Programs from './components/Programs';
import Enrollments from './components/Enrollments';

function App() {
  return (
    <Router>
      <div>
        <h1>Health Information System</h1>
        <nav>
          <Link to="/clients">Clients</Link> |{" "}
          <Link to="/programs">Programs</Link> |{" "}
          <Link to="/enrollments">Enrollments</Link>
        </nav>
        <Routes>
          <Route path="/clients" element={<Clients />} />
          <Route path="/programs" element={<Programs />} />
          <Route path="/enrollments" element={<Enrollments />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
