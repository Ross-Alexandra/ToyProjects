import React from 'react';
import Letter from '../letter_selector/letter.js'

import './game.css';


class Game extends React.Component {

    render() {

        const letters = []
        var letterCounter = 0

        // Iterate over each letter of the word.
        this.props.currentWord.split('').forEach(letter => {

            console.log(letter);

            letterCounter++;
            letters.push(
                <Letter 
                    className="game-letter"
                    key={letterCounter}
                    letter={letter}
                    activated={true}
                    letterClick={() => {}}
                />
            );
        });

        return (
            <div id="game-board" style={{gridTemplateColumns: "auto ".repeat(letterCounter)}}>
                {letters}
            </div>
        );
    }
}



export default Game;