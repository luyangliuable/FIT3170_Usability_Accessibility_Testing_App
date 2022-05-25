import React, { Component } from 'react'
import { Container } from "react-bootstrap";

import "./Results.css"

import ReportsTable from "../Results/components/ReportsTable"

export default class Results extends Component {
  render() {
    /* TODO link to backend */
    var reports = [["test_file.apk",  "100 Mb", "21/04/22", "https://ourwebsite.com.au/results/dummyid1"],
                   ["test_file2.apk", "150 Mb", "21/04/22", "https://ourwebsite.com.au/results/dummyid2"],
                   ["test_file3.apk", "60 Mb",  "20/04/22", "https://ourwebsite.com.au/results/dummyid3"]]  

    return (
      <Container className='container-nav'>
        <div className="results-root">
          <p className="results-text-60 results-text-center">RESULTS</p>

          <div className="results-vspacing-40"> </div>

          <div className="results-div-full">
            <p className="results-text-48 results-full-width">APK BUG REPORTS</p>

            {/* Display the actual table if there is data */}
            { reports.length > 0 && 
              <ReportsTable reports={reports}/> }

            {/* Display message if table is empty*/ }
            { reports.length === 0 &&
              <p className="results-text-30 results-full-width">There are no bug reports to display.</p> }
          </div>
        </div>
      </Container>
    )
  }
}
