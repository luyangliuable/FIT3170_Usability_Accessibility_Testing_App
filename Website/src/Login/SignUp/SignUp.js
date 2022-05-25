import React, { Component } from 'react'
import { Row, Container, Form, Button, Col } from "react-bootstrap";
import { Link } from 'react-router-dom';

export default class SignUp extends Component {
  render() {
    return (
      <Container className='container-nav'>
      <Row className="login-root">
        <div className="login-div-group-white">
          <Col className='login-col'>
            <div className='form-div-0'>
              <Col lg={12} className='login-title'><h2 className='login'>SIGN UP</h2></Col>

              <form>
                <div className='form-div-1'>
                    <Form.Group className="mb-3" controlId="formBasicEmail">
                      <Form.Control className='input' type="email" placeholder="Name" />
                      <Form.Control className='input' type="email" placeholder="Email" />
                      <Form.Control className='input' type="email" placeholder="Password" />
                    </Form.Group>
                  </div>

                  <div className='form-div-2'>
                  <Button className='button' type="submit">Sign Up</Button>
                  </div>
              </form>
              
              <Col lg={12}>
                <Link to={"/login"}>
                  <p className='new-user'>Have an account? Log In.</p>
                </Link>
              </Col>
            </div>
          </Col>

          <Col className='image-col'>
            <Col className='logo-name'>BXER</Col>
          </Col>
        </div>
      </Row>
    </Container>
    )
  }
}
