var $sideHeaderToggle = $(".side-header-toggle"),
    $hideSideHeader = $(".hide-side-header"),
    $sideHeaderClose = $(".side-header-close"),
    $sideHeader = $(".side-header");

  /*Add/Remove Show/Hide Class On Depending on Viewport Width*/
  function $sideHeaderClassToggle() {
    var $windowWidth = $window.width();
    if ($windowWidth >= 1200) {
      $sideHeader.removeClass("hide").addClass("show");
    } else {
      $sideHeader.removeClass("show").addClass("hide");
    }
  }
  $sideHeaderClassToggle();

  // Common Resize function
  function resize() {
    $sideHeaderClassToggle();
  }
  // Resize Window Resize
  $window.on("resize", function () {
    resize();
  });