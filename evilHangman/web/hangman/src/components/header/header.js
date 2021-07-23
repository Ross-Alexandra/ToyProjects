import React from 'react';
import { Container, Row, Navbar } from 'react-bootstrap';
import "./header.css";

class Header extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            logo_img: "Hangman-logo-evilless.png"
        };

        this.evillessLogo = "Hangman-logo-evilless.png";
        this.evilLogo = "Hangman-logo.png";
    }

    render() {

        const logo_img = this.state.logo_img;

        return (
            <header>
                <Navbar fixed="top" color="light" className="nav-header border-bottom border-gray" alt="Evil Hangman" style={ {height: "10%" }}>
                    <Container>
                        <Row noGutters className="position-relative w-100 align-items-center">
                            <img className="logo-img" onMouseEnter={() => {this.setState({logo_img: this.evilLogo})}} src={logo_img}></img>
                        </Row>
                    </Container>
                </Navbar>
            </header>
        )
    }

}

export default Header;