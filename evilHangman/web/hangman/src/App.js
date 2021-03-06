import './App.css';
import React, { Component } from 'react';
import Header from './components/header/header.js';
import Body from './components/body/body.js';

class App extends Component {

    render() {
        return (
            <div className="App">
                <Header />
                <Body />
                <footer>
                    <div className="fixed-bottom border-top border-grey app-footer">
                        <div className="copyright">(Evil) Hangman by Ross Alexandra © 2020</div>
                        <div className="contact">For help, bug reports, etc please contact me at Ross-Alexandra@outlook.com</div>
                        <div className="github" style={{ marginTop: ".25vh" }}>
                            <a href="https://github.com/Ross-Alexandra">
                                { /* SVG courtesy of github.com */}
                                <svg class="octicon octicon-mark-github v-align-middle" height="2.5vh" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
                            </a>
                        </div>
                    </div>
                </footer>
                <link
                    rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
                    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
                    crossorigin="anonymous"
                />
            </div>
        );
    }
}

export default App;
