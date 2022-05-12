//Trying to get it where it counts how many times 'Go!' is pressed
import React from "react";

function CountingGos() {
    const [count, setCount] = React.useState(0);
    const update = () => {
        let c = count + 1;
        setCount(c);

        var a = document.getElementById("userInput").value;

        if (a < 30) {
            alert(a + " is not allowed - Enter a number BETWEEN 30 and 100");
        }

        else if (a > 100) {
            alert(a + " is not allowed - Enter a number BETWEEN 30 and 100");
        }

        else {
            //setting numbers based on input
            document.getElementById("headerStuff").innerHTML = a;
            document.getElementById("a1").innerHTML = a -= 20;
            document.getElementById("a2").innerHTML = a -= 1;
            document.getElementById("a3").innerHTML = a += 3;
            document.getElementById("a4").innerHTML = a -= 1;
            //setting constant numbers
            document.getElementById("ph1").innerHTML = 8;
            document.getElementById("ph2").innerHTML = 11;
            document.getElementById("ph3").innerHTML = 1;
            document.getElementById("ph4").innerHTML = 2;
            document.getElementById("ph5").innerHTML = 7;
            document.getElementById("ph6").innerHTML = 12;
            document.getElementById("ph7").innerHTML = 3;
            document.getElementById("ph8").innerHTML = 9;
            document.getElementById("ph9").innerHTML = 6;
            document.getElementById("ph10").innerHTML = 10;
            document.getElementById("ph11").innerHTML = 5;
            document.getElementById("ph12").innerHTML = 4;


            const ph1 = document.getElementById('ph1');
            ph1.style.backgroundColor = 'purple';

            const ph3 = document.getElementById('ph3');
            ph3.style.backgroundColor = 'red';

            const ph10 = document.getElementById('ph10');
            ph10.style.backgroundColor = 'red';

            const a4 = document.getElementById('a4');
            a4.style.backgroundColor = 'purple';

            //changing color of a diagonal
            const ph4 = document.getElementById('ph4');
            ph4.style.backgroundColor = 'green';

            const ph8 = document.getElementById('ph8');
            ph8.style.backgroundColor = 'blue';

            //changing column color
            const ph2 = document.getElementById('ph2');
            ph2.style.backgroundColor = 'yellow';

            const a3 = document.getElementById('a3');
            a3.style.backgroundColor = 'yellow';

            const ph11 = document.getElementById('ph11');
            ph11.style.backgroundColor = 'yellow';
        }
    }

    return (
        <div>
            <button onClick={update}> GO! </button>
            <label data-testid="amtTestID" style={{ fontsize: 25 }} className='amt'>Amount of #'s put in: {count}</label>
        </div>
    )
}

export default CountingGos;

//This is not done