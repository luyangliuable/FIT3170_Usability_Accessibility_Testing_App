import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import superagent from 'superagent';


import "./ResultBox.css";

export default function UploadBox() {
    const [buttonState, setButtonState] = useState(false);
    const [selectedFile, setSelectedFile] = useState(null);

    const canAccept = (file) => {
        /* TODO check file types */
        return null;
    };

    const onDropAccepted = useCallback(acceptedFiles => {
        console.log("upload");
        setButtonState(true);
        setSelectedFile(acceptedFiles[0]);

        // todo backend upload url
        // let req = superagent.post('http://127.0.0.1:5000/upload/apk/');
        acceptedFiles.forEach(file => {
            console.log(JSON.stringify(file));
        });


        // const file = document.getElementById('file_upload').files;

        // console.log(JSON.stringify(file));


        const req = superagent.post('http://localhost:5001/upload/apk/');
        acceptedFiles.forEach(file => {
            console.log('sending ' + file.path);
            fetch('http://localhost:5001/upload/apk', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ "mime-type": "apk", 'file': file }),
            }).then(response => response.json()).then(data => {
                console.log("done");
                setButtonState(false);
                // return data.task_id;
            });
        });

    }, []);

    const { getRootProps, getInputProps } = useDropzone({
        onDropAccepted: onDropAccepted,
        maxFiles: 1,
        disabled: buttonState,
        // validator: canAccept
    });

    return (
        <div className="result-box-root">
            <div{...getRootProps()} disabled={buttonState}>
                <input {...getInputProps()} disabled={buttonState} />

                <div className="result-box-full-width">
                    <img className="result-box-icon" src={require("./content/dummy_200x256.png")} alt={""} />
                    <img className="result-box-icon" src={require("./content/dummy_200x256.png")} alt={""} />
                </div>

                <div className="result-vspacing-10"> </div>

                <div className="result-box-full-width">
                    <p className="result-box-text-30">{selectedFile ? selectedFile.name : 'Drop APK or MP4 here'}</p>
                </div>

                <div className="result-box-full-width">
                    <div className="result-box-center-bar">
                        {/* TODO actual progess bar */}
                        <div className="result-box-line result-box-left" />
                        <div className="result-box-line result-box-right" />

                        <p className="result-box-text-20 result-text-center">or</p>
                    </div>
                </div>

                <div className="result-box-full-width">
                    {/* TODO functional button */}
                    <button className={buttonState ? "result-box-view-button result-button-disabled" : "result-box-view-button result-button-enabled"}
                        disabled={buttonState}>{buttonState ? 'Uploading...' : 'Upload File'}</button>
                </div>
            </div>
        </div>
    );
}
