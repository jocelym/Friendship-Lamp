import React from 'react';

export class MyButton extends React.Component {
  render(){
    return(
      <button type = "button" onClick = {this.props.onClick} class = "colorButton">
        <img
          src = {this.props.colorImg}
          alt = {this.props.colorName}
          class = 'colorPic'
        />

      </button>
    );
  };
}
