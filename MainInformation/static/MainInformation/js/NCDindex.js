// 在页面加载完成后执行初始设置
window.addEventListener('DOMContentLoaded', function() {
  var videos = document.getElementsByTagName('video');
  for (var i = 0; i < videos.length; i++) {
    if (i === 0) {
      videos[i].style.display = 'block'; // 显示第一个视频
      videos[i].play();
    } else {
      videos[i].style.display = 'none'; // 隐藏其他视频
    }
  }
});

function changeVideo(videoIndex) {
  var videos = document.getElementsByTagName('video');
  var buttons = document.getElementsByTagName('button');

  for (var i = 0; i < videos.length; i++) {
    videos[i].pause();
    videos[i].currentTime = 0;
    videos[i].style.display = 'none';
    buttons[i].classList.remove('active');
  }

  var targetVideo = videos[videoIndex];
  var targetButton = buttons[videoIndex];
  targetVideo.style.display = 'block';
  targetVideo.play();
  targetButton.classList.add('active');
}

function changePage(PageIndex) {
  var buttons = document.getElementsByTagName('button');
  for (var i = 5; i < buttons.length; i++) {
      buttons[i].classList.remove('active');
  }

  var targetButton = document.getElementById(PageIndex);
  targetButton.classList.add('active');
}





