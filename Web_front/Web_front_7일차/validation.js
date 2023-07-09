window.addEventListener('load', function(){
    clearMessages();

    var formElement = this.document.querySelector('form');
    formElement.onsubmit = submitForm;  //submitForm의 반환 값이 false이면 submit이 동작하지 않게 된다

    // 월 추가
    var selectInput = document.querySelector('select[name="birth-month"]');
    for (var i = 1; i <= 12; i++) {
        var option = this.document.createElement('option');
        option.innerHTML = i + "월";
        option.value = i;

        selectInput.appendChild(option);
    }
});

function clearMessages() {
    var messages = document.getElementsByClassName('alert-message');
    for (var i = 0; i < messages.length; i++) {
        messages[i].style.display = 'none';
    }
}

function showMessage(inputElemnet, message) {
    var messageEle = inputElemnet.parentnode.querySelector('span');
    messageEle.style.display = 'inline';
    messageEle.innerText = message;

    inputElemnet.focus();   //inputelement에 focus가 가도록 설정
}


function submitForm() {
    // account info
    var accountInput = document.querySelector('input[name="account"]');
    var passwordInput = document.querySelector('input[name="password"]');
    var passConfirmInput = document.querySelector('input[name="password2"]');

    // select, radio, checkbox
    var selectInput = document.querySelector('select[name="birth-month"]');
    var radioInput = document.querySelector('input[name="gender"]:checked');
    var checkInput = document.querySelector('input[name="agree"]');

    console.log(accountInput.value);
    console.log(passwordInput.value);
    console.log(passConfirmInput.value);

    console.log(selectInput.value);
    console.log(radioInput.value);
    console.log(checkInput.value);


    // 검증 logic
    var success = true;
    if(accountInput.value.length < 6) {
        showMessage(accountInput, "아이디는 6자리 이상이어야 합니다.");
        success = false;
    }

    if(passwordInput.value.length < 10) {
        showMessage(passwordInput, "비밀번호는 10자리 이상이어야 합니다.");
        success = false;
    }
    
    if(passwordInput.value !== passConfirmInput.value) {
        showMessage(passConfirmInput, "비밀번호를 동일하게 입력해주세요.");
        success = false;
    }

    return success;
}