import React from 'react';
import ReactDOM from 'react-dom';
import firebase from "firebase";
import './index.css';
import './firebase.js';
import {MyButton} from './colorButton';
import redPic from './icons/red.png';
import orangePic from './icons/orange.png';
import yellowPic from './icons/yellow.png';
import greenPic from './icons/green.png';
import cyanPic from './icons/cyan.png';
import bluePic from './icons/blue.png';
import purplePic from './icons/purple.png';
import magentaPic from './icons/magenta.png';
import pinkPic from './icons/pink.png';
import whitePic from './icons/white.png';

//USE IMAGE ON CLICK!!! (EVENT LISTENERS)
//USE LISTS of the colors and keys? and a component class
//Use logic in a render function

class TitleBlock extends React.Component{
  render() {
    return(
      <blockquote>
        <h1> Friendship Lamp</h1>

      </blockquote>
    );
  }
};



class DisplayAllButtons extends React.Component {
//  const firebaseApp = firebase.apps[0];
  handleClick (color){
    //alert (color);
    firebase.database().ref('lampData').set({
      lampColor: color
    })
  }
  render() {
    return(
      <div class = "colorCont">
        <MyButton colorName = "red" colorImg = {redPic} onClick = {() => this.handleClick('1')}/> &nbsp;
        <MyButton colorName = "orange" colorImg = {orangePic} onClick = {() => this.handleClick('2')}/> &nbsp;
        <MyButton colorName = "yellow" colorImg = {yellowPic} onClick = {() => this.handleClick('3')}/> &nbsp;
        <MyButton colorName = "green" colorImg = {greenPic} onClick = {() => this.handleClick('4')}/> &nbsp;
        <MyButton colorName = "cyan" colorImg = {cyanPic} onClick = {() => this.handleClick('5')}/> &nbsp;
        <br/> <br/>
        <MyButton colorName = "blue" colorImg = {bluePic} onClick = {() => this.handleClick('6')}/> &nbsp;
        <MyButton colorName = "purple" colorImg = {purplePic} onClick = {() => this.handleClick('7')}/> &nbsp;
        <MyButton colorName = "magenta" colorImg = {magentaPic} onClick = {() => this.handleClick('8')}/> &nbsp;
        <MyButton colorName = "pink" colorImg = {pinkPic} onClick = {() => this.handleClick('9')}/> &nbsp;
        <MyButton colorName = "white" colorImg = {whitePic} onClick = {() => this.handleClick('10')}/> &nbsp;
      </div>
    );
  };
}



ReactDOM.render(
  <TitleBlock/>,
  document.getElementById('title')
);


ReactDOM.render(
  <DisplayAllButtons />,
  document.getElementById('allColors')
);
