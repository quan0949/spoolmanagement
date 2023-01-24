var $sideHeaderToggle = $(".side-header-toggle"),
    $sideHeaderClose = $(".side-header-close"),
    $sideHeader = $(".side-header");

  /*Add/Remove Show/Hide Class On Depending on Viewport Width*/
  function $sideHeaderClassToggle() {
    $sideHeader.removeClass("show").addClass("hide");
  }
  $sideHeaderClassToggle();