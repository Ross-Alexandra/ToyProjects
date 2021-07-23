import React from 'react';
import { Card } from 'react-bootstrap';
import Letter from './letter.js';
import './letter_selector.css';

class LetterSelector extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            clickedLetters: []
        }
    }

    letterClick = (letter) => {
        console.log("Letter clicked");
        this.props.letterClicked(letter);

        const clickedLetters = this.state.clickedLetters;
        clickedLetters.push(letter);
        this.setState({clickedLetters})

        console.log(clickedLetters);
    }

    render() {

        const letters = [];
        for (var i = 97; i < 123; i++) {
            const letter_int = String.fromCharCode(i);

            letters.push(
                <Letter 
                    className="letter" 
                    key={i} 
                    letterClick={this.letterClick} 
                    activated={!this.state.clickedLetters.includes(letter_int)} 
                    letter={letter_int}
                />);
        }

        const selector = (
            <Card className="letter-card">
                <Card.Body className="letter-card-body">
                    <Card.Title>Letter Selector</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">Pick a letter: find the word</Card.Subtitle>
                    <div className="letter-box">
                        {letters}
                    </div>
                </Card.Body>
            </Card>
        );

        const prompt = (
            <div className="letter-card">
                <title>Letter selection unavailable until game start</title>
            </div>
        )

        return (
            this.props.activated ? 
            (
                selector
            ) : (
                prompt
            )
        );
    }
}

export default LetterSelector;