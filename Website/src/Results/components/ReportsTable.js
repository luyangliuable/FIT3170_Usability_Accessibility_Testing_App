import React from 'react'

import "./ReportsTable.css"

export default function ReportsTable({ image, issues, app }) {
    return (
        <>
            <h2 style={{color:"white"}}>{app}</h2>
            <div id="report">
                <img id='report_img' src={image} alt="issue" />
                <p>
                    {
                        issues.map((issue) => (
                            <li style={{ float: "right", width: "80%", margin: "12px 0px 0px 10px" }}>{issue}</li>
                        ))
                    }
                </p>
            </div>
        </ >
    );
};
