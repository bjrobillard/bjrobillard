import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Title from './Title';
import CountingGos from './CountingGos';
import Author from './Author';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

const title = ReactDOM.createRoot(document.getElementById('title'));
title.render(<Title />);

const countingGos = ReactDOM.createRoot(document.getElementById('countingGo'));
countingGos.render(<CountingGos />);

const author = ReactDOM.createRoot(document.getElementById('author'));
author.render(<Author />);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
