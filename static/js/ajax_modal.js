$('#button_write_feed').on('click', ()=>{
//    alert("공유를 시작 합니다");
    const image = $('#input_image').css("background-image").replace(/^url\(['"](.+)['"]\)/, '$1');
    const content = $('#input_content').val();
    const profile_image = $('#input_profile_image').attr('src');
    const nickname = $('#input_user_id').text();

    const file = files[0];

    let fd = new FormData();

    fd.append('file', file);
    fd.append('image', image);
    fd.append('content', content);
    fd.append('profile_image', profile_image);
    fd.append('nickname', nickname);

    if(image.length <= 0)
    {
        alert("이미지가 비어있습니다.");
    }
    else if(content.length <= 0)
    {
        alert("설명을 입력하세요");
    }
    else if(profile_image.length <= 0)
    {
        alert("프로필 이미지가 비어있습니다.");
    }
    else if(nickname.length <= 0)
    {
        alert("사용자 id가 없습니다.");
    }
    else{
        writeFeed(fd);
        console.log(files[0]);
    }
});

function writeFeed(fd) {
    $.ajax({
        url: "/content/upload/",
        data: fd,
        method: "POST",
        processData: false,
        contentType: false,
        success: function (data) {
            console.log("성공");
        },
        error: function (request, status, error) {
            console.log("에러");
        },
        complete: function() {
            console.log("무조건실행");
            location.reload();
        }
    })
};


