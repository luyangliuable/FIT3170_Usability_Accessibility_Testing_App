import React, { Component } from 'react'
import { Container } from "react-bootstrap";

import './About.css';

export default class About extends Component {
  render() {
    return (
      <Container className='container-nav'>
        <div className="about-root">
          <p className="about-text-60">ABOUT US</p>

          <p className="about-text-48">BACKGROUND</p>
          <p className="about-text-30">Mobile apps are now widely used in our daily life. For users with disabilities or
                                        who are aged, many applications may have issues such as erroneous animation, font size,
                                        text overlap, or colour schema selection that negatively influence the usability and
                                        accessibility of the software. </p>


          <div className="about-vspacing-40"> </div>


          <div>
            <div className="about-div-mid">
              <img className="about-img-520-380" src={require("./content/dummy_520x380.png")}  alt={""}/>
            </div>
            <div className="about-div-mid">
              <img className="about-img-600-440" src={require("./content/dummy_600x440.png")}  alt={""}/>
            </div>
            <div className="about-div-mid">
              <p className="about-text-20">Android phone home screen with multiple applications</p>
            </div>
            <div className="about-div-mid">
              <p className="about-text-20">Graph of number of available applications in Google Play Store from December 2009 to March 2022. Peaks in Dec ‘17 and Dec ‘20.</p>
            </div>
          </div>


          <div className="about-vspacing-40"> </div>


          <p className="about-text-48">APPLICATION DEVELOPMENT</p>
          <p className="about-text-30">This application is currently being developed by a team of 17 students from Monash University.      </p>

        </div>
      </Container>
    )
  }
}
