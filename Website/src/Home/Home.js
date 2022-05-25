import React, { Component } from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import "./Home.css"

export default class Home extends Component {
  render() {
    return (
      <Container fluid="true">
        <Row className="hero">
            <Col className='hero-text'>
                <h1>HELPING DEVLOPERS. <br/> HELPING USERS.</h1>
            </Col>
        </Row>
      </Container>
    )
  }
}
