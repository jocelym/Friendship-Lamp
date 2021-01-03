import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import redPic from './icons/red.png';
import orangePic from './icons/orange.png';
import yellowPic from './icons/yellow.png';
import greenPic from './icons/green.png';
import cyanPic from './icons/cyan.png';
import bluePic from './icons/blue.png';
import purplePic from './icons/purple.png';
import magentaPic from './icons/magenta.png';
import pinkPic from './icons/pink.png';

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

class MyButton extends React.Component {
  render(){
    return(
      <button type = "button" onClick = {this.changeState} class = "colorButton">
        <img
          src = {this.props.colorImg}
          class = 'colorPic'
        />
        //<p> {this.props.colorName} </p>
      </button>
    );
  };
}

class DisplayAllButtons extends React.Component {
  render() {
    return(
      <div class = "colorCont">
        <MyButton colorName = "red" colorImg = {redPic}/> &nbsp;
        <MyButton colorName = "orange" colorImg = {orangePic}/> &nbsp;
        <MyButton colorName = "yellow" colorImg = {yellowPic}/> &nbsp;
        <MyButton colorName = "green" colorImg = {greenPic}/> &nbsp;
        <MyButton colorName = "cyan" colorImg = {cyanPic}/> &nbsp;
        <br/> <br/>
        <MyButton colorName = "blue" colorImg = {bluePic}/> &nbsp;
        <MyButton colorName = "purple" colorImg = {purplePic}/> &nbsp;
        <MyButton colorName = "magenta" colorImg = {magentaPic}/> &nbsp;
        <MyButton colorName = "pink" colorImg = {pinkPic}/> &nbsp;
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
