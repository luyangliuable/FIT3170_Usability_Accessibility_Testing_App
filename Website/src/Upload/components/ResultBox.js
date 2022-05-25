import React, { Component } from 'react'
import "./ResultBox.css"

export default class ResultBox extends Component {
  render() {
    return (
      <div className="result-box-root">
          <div className="result-box-full-width">
              <img className="result-box-icon" src={require("./content/dummy_200x256.png")}   alt={""}/>
          </div>

          <div className="result-vspacing-10"> </div>

          <div className="result-box-full-width">
              <p className="result-box-text-30">Analysing Results ...</p>
          </div>

          <div className="result-box-full-width"> 
            <div className="result-box-center-bar result-progress-bar">
              {/* TODO actual progess bar */}
              <div className="result-box-rectangle-3-5" />
              <div className="result-box-rectangle-3-6" />
              <p className="result-box-text-20 result-text-after">50%</p>
            </div>
          </div>

          <div className="result-box-full-width"> 
              {/* TODO functional button */}
            <button className="result-box-view-button result-button-disabled">View Results</button>
          </div>
      </div>
    )
  }
}
