import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<h1>VoxBabel — Lobby</h1>} />
        <Route path="/meeting/:roomId" element={<h1>Meeting Room</h1>} />
        <Route path="/dashboard" element={<h1>Dashboard</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
