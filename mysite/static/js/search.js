$("input.typeahead").typeahead({
    onSelect: function(item) {
        console.log(item);
    },
    ajax: {
        url: "/search/",
        timeout: 500,
        displayField: "title",
        triggerLength: 1,
        method: "get",
        loadingClass: "loading-circle",
        preDispatch: function (query) {
//            showLoadingMask(true);
            return {
                search: query
            }
        },
        preProcess: function (data) {
//            showLoadingMask(false);
            if (data.success === false) {
                // Hide the list, there was some error
                return false;
            }
            // We good!
            return JSON.parse(data.search);
        }
    }
});