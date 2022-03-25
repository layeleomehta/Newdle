import React, { useState } from 'react';
import RICIBs from 'react-individual-character-input-boxes';
import { wordList } from './constants/words';

function Game(props) { 
    const [outString, setOutString] = useState("");

    // generates random word from the wordList
    const getRandomWord =()=>{
        var alphabetIndex = Math.floor(Math.random() * 26);
        var wordIndex = Math.floor(Math.random() * wordList[String.fromCharCode(97 + alphabetIndex)].length);
        var randomWord = wordList[String.fromCharCode(97 + alphabetIndex)][wordIndex];
        return randomWord; 
      }

    const handleRICIBsOutput = (string) => {
        console.log(string); 
    }
    // Renders 'num' number of squares for text input
    const renderSquares = (num) => {
        var words = []
        for(let i=0; i<num; i++){
            words.push(<span key={i}>        
                <RICIBs
                amount={5}
                handleOutputString={handleRICIBsOutput}
                inputProps={[]}
                inputRegExp={/^[a-z]$/}
              /></span>); 
        }
        return words; 
    }

    return ( 
    <div>
        <div>{renderSquares(5)}</div>
        <button className="reset-board">Click to Reset Word</button>
        <h2>{outString}</h2>
    </div>
     );
}

export default Game;
