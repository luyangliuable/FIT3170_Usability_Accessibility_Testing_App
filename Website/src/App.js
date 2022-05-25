import { BrowserRouter, Route, Routes } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';

import ToolBar from './ToolBar/ToolBar';
import Login from './Login/Login';
import Home from './Home/Home';
import SignUp from './Login/SignUp/SignUp';
import Results from './Results/Results';
import About from './About/About';
import Upload from './Upload/Upload';

function App() {
  return (
    <BrowserRouter>
      <ToolBar />

      <Routes>
        <Route path="" element={<Home />}></Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/login/signup" element={<SignUp />}></Route>
        <Route path="/about" element={<About />}></Route>
        <Route path="/results" element={<Results />}></Route>
        <Route path="/upload" element={<Upload />}></Route>
      </Routes>
    </BrowserRouter>
  );
}


export default App;
