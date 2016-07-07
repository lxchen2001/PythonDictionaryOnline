function gAjax(url, data, success, error) {
    $.ajax({
        async: true,
        global: false,
        cache: false,
        type: "POST",
        url: url,
        data: data,
        dataType: "html",
        success: function (msg) {
            success(msg);
        },
        error: function (msg) {
            error(msg);
        }
    });
}