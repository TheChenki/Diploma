var pageIndex = 0;
var pages;
var prevControl, nextControl;

$(document).on('ready', function () {
    pages = $("[data-page]");
    pages.slice(1).addClass('d-none');

    prevControl = $("[data-control='prev']");
    nextControl = $("[data-control='next']");

    $("[data-control='prev']").on('click', function () {
        if (pageIndex == 0)
            return;

        $(pages[pageIndex]).addClass('d-none');
        pageIndex--;
        $(pages[pageIndex]).removeClass('d-none');

        updateControls('prev');
    })

    $("[data-control='next']").on('click', function () {
        if (pageIndex == (pages.length - 1))
            return;

        $(pages[pageIndex]).addClass('d-none');
        pageIndex++;
        $(pages[pageIndex]).removeClass('d-none')

        updateControls('next');
    })
})

function updateControls(direction) {
    if (pageIndex == (pages.length - 1)) {
        $("[data-control='next']").addClass('page-control-inactive')
        $("[data-control='next']").removeClass('page-control')
    }
    else if (pageIndex == 0) {
        $("[data-control='prev']").addClass('page-control-inactive')
        $("[data-control='prev']").removeClass('page-control')
    }

    if(direction == 'next')
    {
        $("[data-control='prev']").addClass('page-control')
        $("[data-control='prev']").removeClass('page-control-inactive')
    }
    else if(direction == 'prev')
    {
        $("[data-control='next']").addClass('page-control')
        $("[data-control='next']").removeClass('page-control-inactive')
    }

}