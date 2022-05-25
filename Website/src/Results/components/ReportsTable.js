import React from 'react'

import "./ReportsTable.css"

export default function ReportsTable({reports}) {
    return (
        <div className="reports-full-width">
            <table className="reports-full-width">
              <thead>
                <tr>
                  <th className="reports-table-header reports-col-size-40">Apk Name</th>
                  <th className="reports-table-header reports-col-size-20">File Size</th>
                  <th className="reports-table-header reports-col-size-20">Upload Date</th>
                  <th className="reports-table-header reports-col-size-20">Report Link</th>
                </tr>
              </thead>

              <tbody>
                { reports.map((rep, idx) => (
                  <tr>
                    <td className="reports-table-cell reports-col-size-40">{rep[0]}</td>
                    <td className="reports-table-cell reports-col-size-20">{rep[1]}</td>
                    <td className="reports-table-cell reports-col-size-20">{rep[2]}</td>
                    <td className="reports-table-cell reports-col-size-20"><a href={rep[3]}>report</a></td>
                    <div className="reports-full-width reports-line-white"> </div>
                  </tr>
                )) }
              </tbody>
            </table>
        </div>
    )
}