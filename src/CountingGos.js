//Trying to get it where it counts how many times 'Go!' is pressed
import React from "react";

function CountingGos() {
    const [count, setCount] = React.useState(0);
    const update = () => {
        let c = count + 1;
        setCount(c);
    }
    return (
        <div>
            <label></label> 
            <button update={update}> GO! </button>
        </div>
    )
}

export default CountingGos;

//This is not done