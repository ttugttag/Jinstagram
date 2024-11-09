$('#nav_bar_add_box').click(function () {
    $('#modal_add_feed').css({
        display: 'flex',
        top : window.pageYOffset + 'px'
    });

    $(document.body).css({
        overflow: 'hidden'
    });
})

$(".close_modal").click(function () {
    $('#modal_add_feed').css({
        display: 'none',
    });
    $('#modal_add_feed_content').css({
        display: 'none',
    });

    $(document.body).css({
        overflow: 'visible'
    });
})

$('.modal_image_upload')
    .on("dragover", dragOver)
    .on("dragleave", dragOver)
    .on("drop", uploadFiles);

function dragOver(e){
    e.stopPropagation();
    e.preventDefault();

    if (e.type == "dragover") {
        $(e.target).css({
            "background-color": "black",
            "outline-offset": "-20px"
        });
    } else {
        $(e.target).css({
            "background-color": "white",
            "outline-offset": "-10px",
        });
    }
}

function uploadFiles(e){
    e.stopPropagation();
    e.preventDefault();
    console.log(e.dataTransfer)
    console.log(e.originalEvent.dataTransfer)

    e.dataTransfer = e.originalEvent.dataTransfer;

    files = e.dataTransfer.files;
    console.log(files)

    if (files.length > 1) {
        alert('하나만 올려라.');
        return;
    }

    if (files[0].type.match(/image.*/)) {
        $('#modal_add_feed_content').css({
            display : 'flex',
            top : window.pageYOffset + 'px'
        });

        $('.modal_image_upload_content').css({
            "background-image": "url(" + window.URL.createObjectURL(files[0]) + ")",
            "outline": "none",
            "background-size": "contain",
            "background-repeat" : "no-repeat",
            "background-position" : "center"
        });
        $('#modal_add_feed').css({
            display: 'none'
        })
    }else{
        alert('이미지가 아닙니다.');
        return;
    }
};
