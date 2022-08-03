import React from 'react'
import { Container } from "react-bootstrap";
import { useState } from 'react';

import './Upload.css';

import ResultBox from "./components/ResultBox"
import UploadBox from "./components/UploadBox"
import ReportsTable from "../Results/components/ReportsTable"

// export default class Upload extends Component {

const AdditionalUploads = () => {
    const [resultFiles, updateResultFiles] = useState(["./dir_to_file/example_result_file.jpeg"]);
    const [currentAppStatus, updateCurrentAppStatus] = useState("READY");
    var reports = [];  /* TODO link to backend */
    return (
        <Container className='container-nav'>
            <div className="upload-root">

                <p className="upload-text-60 upload-text-center">ADDITIONAL UPLOADS</p>
                <p className="upload-text-30 upload-text-center">Upload your APK or MP4 files to evaluated for bugs</p>

                <div className="upload-vspacing-40"> </div>

                <div className="upload-div-group-white">
                    <div className="upload-align-left">
                        <UploadBox resultFiles={resultFiles} updateResultFiles={updateResultFiles} currentAppStatus={currentAppStatus} updateCurrentAppStatus = { updateCurrentAppStatus }/>
                    </div>

                    <div className="upload-div-vcenter">
                        { /* https://icons.getbootstrap.com/icons/three-dots-vertical/ */}
                        <svg xmlns="http://www.w3.org/2000/svg" width="128px" height="128px" fill="#828282" transform="rotate(90 0 0)" viewBox="0 0 16 16">
                            <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z" />
                        </svg>
                    </div>

                    <div className="upload-align-right">
                        <ResultBox className="upload-align-right" resultFiles={resultFiles} updateResultFiles={updateResultFiles} currentAppStatus={currentAppStatus} updateCurrentAppStatus={updateCurrentAppStatus } />
                    </div>
                </div>

                <div className="upload-vspacing-40"> </div>

                <div className="upload-div-group-white">
                    <p className="upload-text-48 upload-text-dark upload-full-width">RESULTS INCLUDE</p>

                    <div className="upload-side-padding-120">
                        <div className="upload-div-mid upload-side-padding-40">
                            <p className="upload-text-36 upload-text-dark upload-full-width">• Precision</p>
                            <p className="upload-text-36 upload-text-dark upload-full-width">• Recall</p>
                            <p className="upload-text-36 upload-text-dark upload-full-width">• F1 Score</p>
                        </div>

                        <div className="upload-div-mid upload-side-padding-40">
                            <p className="upload-text-36 upload-text-dark upload-full-width">• Bug Replays</p>
                            <p className="upload-text-36 upload-text-dark upload-full-width">• Bug Screenshots</p>
                        </div>
                    </div>
                </div>

                <div className="upload-vspacing-40"> </div>
                <div className="upload-vspacing-40"> </div>

                <div className="upload-div-full">
                    <p className="upload-text-48 upload-full-width">APK BUG REPORTS</p>

                    {/* Display the actual table if there is data */}
                    {reports.length > 0 &&
                        <ReportsTable reports={reports} />}

                    {/* Display message if table is empty*/}
                    {reports.length === 0 &&
                        <p className="upload-text-30 upload-full-width">There are no bug reports to display.</p>}
                </div>

            </div>
        </Container>
    );
}

export default AdditionalUploads;
