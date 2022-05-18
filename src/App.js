// import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App" data-testid='tableTest'>
      <table className='magTable'>
        <tbody>
          <tr>
            <td id='ph1'></td>
            <td id='ph2'></td>
            <td id='a1'></td>
            <td id='ph3'></td>
          </tr>
          <tr>
            <td id='a2'></td>
            <td id='ph4'></td>
            <td id='ph5'></td>
            <td id='ph6'></td>
          </tr>
          <tr>
            <td id='ph7'></td>
            <td id='a3'></td>
            <td id='ph8'></td>
            <td id='ph9'></td>
          </tr>
          <tr>
            <td id='ph10'></td>
            <td id='ph11'></td>
            <td id='ph12'></td>
            <td id='a4'></td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default App;
