import { BrowserRouter, Route, Routes } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';

import ToolBar from './ToolBar/ToolBar';
import Login from './Login/Login';
import Home from './Home/Home';
import SignUp from './Login/SignUp/SignUp';
import Results from './Results/Results';
import About from './About/About';
import UploadAPK from './Upload/UploadAPK';
import SelectAlgorithms from './Upload/SelectAlgorithms';
import AdditionalUploads from './Upload/AdditionalUploads';

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
                <Route path="/upload" element={<UploadAPK />}></Route>
                <Route path="/upload/selectalgorithm" element={<SelectAlgorithms />}></Route>
                <Route path="/upload/additionaluploads" element={<AdditionalUploads />}></Route>
            </Routes>
        </BrowserRouter>
    );
}


export default App;
