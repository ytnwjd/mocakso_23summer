import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  let [글제목, 글제목변경] = useState(["여자 코트 추천", "강남 우동 맛집", "React 독학하기", "남자 코트 변경"]);
  let posts = "고기 맛집";
  let [좋아요, 좋아요변경] = useState(0);

  function 제목바꾸기() {
    var newArray = [...글제목];          //state의 복사본 생성 deep copy(값 공유가 일어나지 않고 새로운 copy본)
    newArray[0] = "남자 코트 추천";
    글제목변경( newArray );
  }

  return (
    <div className="App">
      <div className="black-nav">
        <div style={ { color : 'white', fontSize : '30px' }}>개발 Blog</div>
        
      </div>
      <div className="list">
        <button onClick={ 제목바꾸기 }>제목 변경</button>
        <h3> { 글제목[0] } <span onClick={ ()=>{ 좋아요변경(좋아요+1) } }>👍</span> { 좋아요 } </h3>
        <p>7월 10일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3> { 글제목[1] } </h3>
        <p>7월 11일 발행</p>
        <hr/>
      </div>
      <div className="list">
        <h3> { 글제목[2] } </h3>
        <p>7월 12일 발행</p>
        <hr/>
      </div>

      <Modal></Modal>
      
    </div>
  );
  }

function Modal() {
  return (
    <div className="modal">
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}

export default App;
