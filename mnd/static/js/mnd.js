// MND
// Custom JavaScript
// Change highlight to active menu item

$(document).ready(function () {
    let path = location.pathname;
    $('#sidebar a').removeClass('active');
    if (path === '/') {
        $("#sidebar a").eq(1).addClass('active')
    }
    else {
        $('a[href*="/' + path.split("/")[1] + '"]').addClass('active');
    };
});

// Open or close sidebar with hamburger button
$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });
    
    $('#sidebarCollapse').on('click', function () {
        // open or close navbar
        $('#sidebar, #content, button').toggleClass('open');
        // close dropdowns
        $('.collapse.in').toggleClass('in');
        // and also adjust aria-expanded attributes we use for the open/closed arrows
        // in our CSS
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
            });
});

$(document).ready(function(){
    // external links to new window
    //$('a[href^="http://"]').not('a[href*="mydomainname"]').attr('target','_blank') USE ON LIVE SITE
    $('a[href^="http://"]').attr('target','_blank')
   });


// Deprecated code

// Change highlight on active menu item

// $(document).ready(function () {
//     $('ul.list-unstyled > li').click(function (e) {     
//         $('ul.list-unstyled > li')
//             .removeClass('active');
//     });
// });