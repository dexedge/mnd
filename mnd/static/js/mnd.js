// MND
// Custom JavaScript
// Change highlight to active menu item

$(document).ready(function () {
    let path = location.pathname
    let pathlist = path.split("/");
    $('#sidebar a').removeClass('active');
    if (path == "/") {
        $('#sidebar a[href="/"]').addClass('active');
    }
    else if (pathlist[1] == "documents") {
        if (pathlist[2] == "1760-1779") {
            $('#sidebar a[href="' + path + '"]').addClass('active');
        }
        else if (pathlist[2] == "1780-1787") {
            $('#sidebar a[href*="' + path + '"]').addClass('active');
        }
        else if (pathlist[2] == "1788-1793") {
            $('#sidebar a[href="' + path + '"]').addClass('active');
        }
    }
    else if (pathlist[1] != "" && pathlist[2] == "") {
        $('#sidebar a[href="' + path + '"]').addClass('active');
    }
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
    $('a[href^="http://"], a[href^="https://"]').attr('target','_blank')
   });

// If there is a TOC, add return arrow to Bibliography
// and Notes
$(document).ready(function(){
    let toc = $("#toc").html()
    if (toc) {
        $("#bibliography").append(" (<a href='#toc'>⇧</a>)");
        $("#notes").append(" (<a href='#toc'>⇧</a>)");
    }
});


// Deprecated code

// Change highlight on active menu item

// $(document).ready(function () {
//     $('ul.list-unstyled > li').click(function (e) {     
//         $('ul.list-unstyled > li')
//             .removeClass('active');
//     });
// });