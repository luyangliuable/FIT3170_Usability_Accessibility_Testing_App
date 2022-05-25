import React from "react";
import { Row, Container, Col } from "react-bootstrap";
import { Link } from 'react-router-dom';

import "./ToolBar.css"

export default function ToolBar() {
  return (
      <Container className="nav-container" fluid='true'>
        <Row>
          <Col xxl={1} className="company-logo" >
            <Link to={"./"}>
              <img alt='logo' src={require('./favicon.ico')} />
            </Link>
          </Col>
          <Col xxl={9} className="middle-bar">
            <Col className="nav-center">
              <Link to={"./about"}>
                <h3>ABOUT</h3>
              </Link>
            </Col>
              <Col className="nav-center">
                <Link to={"./upload"}>
                  <h3>UPLOAD APK</h3>  
                </Link>  
              </Col>
              <Col className="nav-center">
                <Link to={"./results"}>
                  <h3>RESULTS</h3>
                </Link>
              </Col> 
          </Col>
          <Col xxl={2} className="nav-center">
            <Link to={"./login"}>
              <h3>LOGIN</h3>
            </Link>
          </Col>

        </Row>
      </Container>
  )
}