var getHeight = function(id) {
  return document.getElementById(id).clientHeight;
};

var setOffset = function() {
  $("body").attr("data-offset", getHeight("category"));
};

var scrollEventHandler = function() {
  var topScroll = document.documentElement.scrollTop || document.body.scrollTop;
  var threshold = getHeight("nav") + getHeight("header");

  if (topScroll > threshold) {
    $("#category").addClass("fixed-top");
  } else {
    $("#category").removeClass("fixed-top");
  }
};

var MyScrollTo = function(target) {
  console.log(-getHeight("category"));

  $.scrollTo($(target), 300, {
    axis: "y",
    offset: {
      top: -100 - getHeight("category")
    }
  });
  // $.scrollTo(target, 300, {
  //   offset: -getHeight("category")*2
  // });
};

$(document).ready(function() {
  setOffset();

  $(window).scroll(scrollEventHandler);

  $(".cat-link").click(function(e) {
    e.preventDefault();
    MyScrollTo(e.target.hash);
  });

  $(".anchor").click(function(e) {
    e.preventDefault();
    MyScrollTo(e.target.getAttribute("data-target"));
  });
});
