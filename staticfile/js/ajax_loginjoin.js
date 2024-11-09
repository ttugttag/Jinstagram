$('#button_join').on('click',()=>{
    console.log('클릭했다.');
    let email = $('#floatingEmail').val();
    let name = $('#floatingName').val();
    let nickname = $('#floatingUserId').val();
    let password = $('#floatingPassword').val();
    console.log('이멜 :' + email + ', 이름 :'  + name + ', 사용자ID :'  +  nickname + ', 비밀번호 :'  +  password);

    $.ajax({
        url: "/user/join/",
        data: {
            email: email,
            password: password,
            nickname: nickname,
            name: name
        },
        method: "POST",
        dataType: "json",
        success: function (data){
            alert(data.message);
//            location.replace("{% url 'user:Login' %}");
            location.replace("/user/login/");
        },
        error:function (request, status, error){
            let data = JSON.parse(request.responseText);
            console.log(data.message);
            alert(data.message);
        }
    });
});

$('#button_login').on('click', ()=>{
    let email = $('#floatingEmail').val();
    let password = $('#floatingPassword').val();

    $.ajax({
        url: "/user/login/",
        data: {
            email: email,
            password: password
        },
        method: "POST",
        dataType: "json",
        success: function (data){
            alert(data.message);
//            location.replace("{% url 'Main' %}");
            location.replace("/main/");
        },
        error:function (request, status, error){
            let data = JSON.parse(request.responseText);
            console.log(data.message);
            alert(data.message);
        }
    });
});

