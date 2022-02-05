// Mozart: New Documents (MND)
// Custom JavaScript

// Change highlight to active menu item
$(document).ready(function () {
    let path = location.pathname
    let pathlist = path.split("/")
    // If Home page
    if (path == "/") {
        $('#sidebar a[href="/"]').addClass('active');
    }
    // Else if chronological index page or document page
    else if (pathlist[1] == "documents") {
        // Grab end of URL as integer
        let urldate = parseInt(pathlist[2].slice(-4));
        // Highlight appropriate chronological index page
        if (urldate <= 1779) {
            $('#sidebar a[href*="1760-1779"]').addClass('active');
        }
        else if (urldate <= 1787) {
            $('#sidebar a[href*="1780-1787"]').addClass('active');
        }
        else if (urldate >= 1788) {
            $('#sidebar a[href*="1788-1793"]').addClass('active');
        }
    }
    // Else highlight the current page
    else {
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
    // Set external links to open in new window
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

////////////////
// References //
////////////////

$(document).ready(function(){
    // For each item in bibliography, if author is "————", set
    // author attribute to current_author. The author attribute
    // is used to replace "————" in pop-up references
    current_author = ""
    $(".biblio p").each(function (){
        author = this.innerHTML.split(".")[0];
        if (author == "————"){
            $(this).attr("author", current_author)
        }
        else {current_author = author}
    });
    // Prepare popovers for bibliographic references
    $("p:not('#notes, #bibliography, .blockindent') a[href^='#'], blockquote a[href^='#']").each(function(){
        refID = this.hash.slice(1)
        refText = $(".biblio[id="+refID+"] p")[0].innerHTML
        author = refText.split(".")[0]
        if (author == "————"){
            refText = refText.replace("————", $(".biblio[id="+refID+"] p").attr("author"))
        }
        $(this).attr({
            "data-bs-toggle":"popover",
            "data-bs-placement":"bottom",
            "data-bs-trigger":"hover",
            "data-bs-html":"true",
            "data-bs-content":refText
        })
        $(this).addClass("reference")
        $(this).removeAttr("href")
    });
    $('[data-bs-toggle="popover"]').popover({container: "body"});
});

