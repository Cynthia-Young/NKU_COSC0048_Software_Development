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

function changeB(videoIndex) {
  var buttons = document.getElementsByTagName('button');

  for (var i = 0; i < 4; i++) {
    buttons[i].classList.remove('active');
  }
  var targetButton = buttons[videoIndex];
  targetButton.classList.add('active');
}

function changeV(videoIndex) {
  var videos = document.getElementsByTagName('video');
  if (videos.length > 0) {
    for (var i = 0; i < videos.length; i++) {
      videos[i].pause();
      videos[i].currentTime = 0;
      videos[i].style.display = 'none';
    }
  
    var targetVideo = videos[videoIndex];
    targetVideo.style.display = 'block';
    targetVideo.play();
  }
}

function changeVideo(videoIndex) {
  changeB(videoIndex);
  changeV(videoIndex);
}

function changePage(PageIndex) {
  var divs = document.getElementsByClassName('button-container');
  var buttons = document.getElementsByTagName('button');
  for (var i = 5; i < buttons.length; i++) {
      buttons[i].classList.remove('active');
  }
  for (var i = 3; i < divs.length; i++) {
      divs[i].style.display = 'none';
  }

  var targetButton = document.getElementById(PageIndex);
  targetButton.classList.add('active');
  var targetDiv = document.getElementById(PageIndex +'Div');
  targetDiv.style.display = 'block';
}





