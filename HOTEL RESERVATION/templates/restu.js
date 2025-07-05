$(document).ready(function () {
    // Sticky header on scroll
    $(window).scroll(function () {
      if ($(this).scrollTop() > 50) {
        $("header").addClass("sticky");
      } else {
        $("header").removeClass("sticky");
      }
    });
  
    // Set current year in the element with ID 'autodate'
    function newDate() {
      return new Date().getFullYear();
    }
  
    // Use jQuery for better compatibility and ensure the element exists
    $("#autodate").text(newDate());
  });
  