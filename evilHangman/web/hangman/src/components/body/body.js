import React from 'react';
import LetterSelector from './letter_selector/letter_selector.js'
import Game from './game/game.js'
import {Form, Button} from 'react-bootstrap'

import './body.css';
var net = require('net');


class Body extends React.Component {

    constructor(props) {
        super(props);


        this.ENDPOINT = "127.0.0.1"
        this.PORT = 34360
        this.state = {
            gameStarted: false,
            totalGuesses: 6,
            wordLength: 6,
            currentWord: "",
            socketConnection: undefined
        }
    }
    
    startGame = (guesses, letter_count) => {
        console.log("Starting game with " + guesses + " guesses and a word length of " + letter_count);

        var updatedConnection;
        if (this.state.socketConnection === undefined) {
            // TODO: Startup the connection to the socket server

            const encoder = new TextEncoder();

            updatedConnection = new net.Socket();
            updatedConnection.connect(this.PORT, this.ENDPOINT, () => {
                console.log("Connected to socket server.");
                updatedConnection.write(guesses.toString());
                updatedConnection.write(letter_count.toString());
                updatedConnection.write("true");
            });

        }

        const newState = {
            gameStarted: true,
            currentWord: "_".repeat(this.state.wordLength),
            socketConnection: updatedConnection
        }

        this.setState(newState);
    }

    playLetter = (letter) => {
        // TODO: Send letter through the socket, and get a response word back.
        
        // TODO: Update with the response word.
        const updatedWord = this.state.currentWord.replace('_', letter)

        this.setState({currentWord: updatedWord});
    }

    render() {

        const game = (
            <div className="app-body">
                <LetterSelector activated={this.state.gameStarted} letterClicked={this.playLetter}/>
                <Game currentWord={this.state.currentWord}/>
            </div>
        );

        const promptStart = (
            <Form className="game-form">
                <Form.Group controlId="form-guesses">
                    <Form.Label>Number of guesses</Form.Label>
                    <Form.Control type="text" placeholder={this.state.totalGuesses} onChange={(e) => {this.setState({totalGuesses: e.target.value})}}/>
                    <Form.Text className="text-muted">
                        This version of hangman is really hard... we recommend at least twice as many attempts as letters.
                    </Form.Text>
                </Form.Group>

                <Form.Group controlId="form-word-length">
                    <Form.Label>Word length</Form.Label>
                    <Form.Control type="text" placeholder={this.state.wordLength} onChange={(e) => {this.setState({wordLength: e.target.value})}}/>
                </Form.Group>

                <Button variant="primary" type="button" onClick={() => {this.startGame(this.state.totalGuesses, this.state.wordLength)}}>
                    Submit
                </Button>
            </Form>
        )

        return (
            this.state.gameStarted ? 
            (
                game
            ) : (
                promptStart
            )
        );
    }
}

export default Body;