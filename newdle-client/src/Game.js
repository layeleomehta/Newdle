import React, { useState } from 'react';

function getNum(num){
    return num+1; 
}

let myObj = getNum(0)


function Game(props) { 
    const [myNum, setmyNum] = useState(myObj);

    return ( 
        <div>
            <h1>This is the Game component!</h1>
            <h1>{myNum}</h1>
            <button onClick={() => {setmyNum(myNum+1)}}>Hello</button>
            <h1>myProp is: {props.myProp}</h1>

        </div>
     );
}

export default Game;