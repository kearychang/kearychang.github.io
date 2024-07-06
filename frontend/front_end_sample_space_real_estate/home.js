$(document).ready(function() {
    $('.carousel-caption-bot').click(function() {
        $("html, body").animate({ scrollTop: $(document).height() }, 1000);
        return false;
    });
});