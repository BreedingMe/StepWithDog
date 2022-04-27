$(document).ready(function () {
    // 최초 로딩 시 게시글 카드 목록 보이기
    $('#post-list-wrapper').show();
    $('#recommend-list-wrapper').hide();

    // 게시글 목록 불러오기
    getPostList();
});

function openPostCardList() {
    // 카드 목록 전환 버튼 CSS 변경
    $('#post-list-button').addClass('active');
    $('#recommend-list-button').removeClass('active');

    // 글쓰기 버튼 보이기
    $('#post-upload-button').show();

    // 카드 목록 전환
    $('#post-list-wrapper').show();
    $('#recommend-list-wrapper').hide();

    // 게시글 목록 불러오기
    getPostList();
}

function openRecommendCardList() {
    // 카드 목록 전환 버튼 CSS 변경
    $('#post-list-button').removeClass('active');
    $('#recommend-list-button').addClass('active');

    // 글쓰기 버튼 숨기기
    $('#post-upload-button').hide();

    // 카드 목록 전환
    $('#post-list-wrapper').hide();
    $('#recommend-list-wrapper').show();

    // 추천 목록 불러오기
    getRecommendList();
}

function openPostPopup(index) {
    // 게시글 팝업 보이기
    $('#post-popup').show();

    // 게시글 불러오기
    let post_id = $(`#post-${index}`).data('id');

    getPost(post_id);
}

function closePostPopup() {
    // 게시글 팝업 내용 초기화
    $('#post-popup-content').empty();

    // 게시글 팝업 숨기기
    $('#post-popup').hide();
}

function openPostUploadPopup() {
    // 게시글 업로드 팝업 보이기
    $('#post-upload-popup').show();
}

function closePostUploadPopup() {
    // 게시글 업로드 팝업 초기화
    clearPostUploadPopup();

    // 게시글 업로드 팝업 숨기기
    $('#post-upload-popup').hide();
}

function clearPostUploadPopup() {
    // 게시글 업로드 팝업 초기화
    $('#title-input').val('');
    $('#address-input').val('');
    $('#image-file').val(undefined);
    $('#custom-file-label').text('');
    $('#content-input').val('');
}

function changeImageFile() {
    // 파일명 출력
    $('#custom-file-label').text($('#image-file')[0].files[0].name);
}

function getPostList() {
    // 게시글 카드 목록 초기화
    $('#post-list-wrapper').empty();

    // 게시글 목록 요청
    $.ajax({
        type: 'GET',
        url: '/post-list',
        data: {},
        success: function (response) {
            let post_list = response['data'];

            for (let index = 0; index < post_list.length; index++) {
                let id = post_list[index]['_id'];
                let thumbnail = post_list[index]['thumbnail'];
                let title = post_list[index]['title'];

                let temp_html = `<div id="post-${index}" class="col-sm-4 post-card-wrapper" data-id="${id}">
                                    <div class="card" onclick="openPostPopup(${index})">
                                        <div class=embed-responsive-4by3">
                                            <img src="${thumbnail}" class="card-img-top embed-responsive-item">
                                        </div>

                                        <div class="card-body">
                                            <h5 class="card-title">${title}</h5>
                                        </div>
                                    </div>
                                </div>`;

                $('#post-list-wrapper').append(temp_html);
            }
        }
    });
}

function getRecommendList() {
    // 추천 카드 목록 초기화
    $('#recommend-list-wrapper').empty();

    // 추천 목록 요청
    $.ajax({
        type: 'GET',
        url: '/recommend-list',
        data: {},
        success: function (response) {
            let recommend_list = response['data'];

            for (let index = 0; index < recommend_list.length; index++) {
                let park_name = recommend_list[index]['park_name'];
                let park_address = recommend_list[index]['park_address'];
                let park_tel = recommend_list[index]['park_tel'];

                let temp_html = `<div class="card">
                                    <div class="card-body recommend-card-wrapper">
                                        <div class="recommend-card-title">${park_name}</div>
                                        <div class="recommend-card-address">${park_address}</div>
                                        <div class="recommend-card-tel">${park_tel}</div>
                                    </div>
                                </div>`;

                $('#recommend-list-wrapper').append(temp_html);
            }
        }
    });
}

function getPost(post_id) {
    // 게시글 요청
    $.ajax({
        type: 'GET',
        url: `/post/${post_id}`,
        data: {},
        success: function (response) {
            let post = response['data'];

            let title = post['title'];
            let image = post['image'];
            let content = post['content'];
            let address = post['address'];

            let temp_html = `<div class="modal-header">
                                <h2 class="modal-title">${title}</h2>
                                <button type="button" class="close" onclick="closePostPopup()">×</button>
                            </div>

                            <div class="modal-body">
                                <img src="${image}" class="popup-image">
                                <div>${content}</div>
                                <hr/>
                                <div>주소: ${address}</div>
                            </div>`;

            $('#post-popup-content').append(temp_html);
        }
    });
}

function uploadPost() {
    let title = $('#title-input').val();
    let address = $('#address-input').val();
    let image = $('#image-file')[0].files[0];
    let content = $('#content-input').val();

    // 입력 검사
    if (title == '') {
        alert('제목이 입력되지 않았습니다!');

        return;
    }

    if (address == '') {
        alert('주소가 입력되지 않았습니다!');

        return;
    }

    if (image == undefined) {
        alert('사진이 선택되지 않았습니다!');

        return;
    }

    if (content == '') {
        alert('내용이 입력되지 않았습니다!');

        return;
    }

    // 게시글 업로드
    let formData = new FormData();

    formData.append('title', title);
    formData.append('address', address);
    formData.append('image', image);
    formData.append('content', content);

    $.ajax({
        type: 'POST',
        url: '/post',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function () {
            clearPostUploadPopup();
            closePostUploadPopup();
            getPostList();
        },
        error: function () {
            alert('사진의 크기가 너무 큽니다!');
        }
    });
}