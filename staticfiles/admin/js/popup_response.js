(function() {
<<<<<<< HEAD

    'use strict';

    var windowRef = window;
    var windowRefProxy;
    var windowName, widgetName;
    var openerRef = windowRef.opener;
=======
    'use strict';

    let windowRef = window;
    let windowName, widgetName;
    let openerRef = windowRef.opener;
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
    if (!openerRef) {
        // related modal is active
        openerRef = windowRef.parent;
        windowName = windowRef.name;
        widgetName = windowName.replace(/^(change|add|delete|lookup)_/, '');
        if (typeof(openerRef.id_to_windowname) === 'function') {
            // django < 3.1 compatibility
            widgetName = openerRef.id_to_windowname(widgetName);
        }
<<<<<<< HEAD
        windowRefProxy = {
            name: widgetName,
            location: windowRef.location,
=======
        windowRef = {
            name: widgetName,
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
            close: function() {
                openerRef.dismissRelatedObjectModal();
            }
        };
<<<<<<< HEAD
        windowRef = windowRefProxy;
    }

    // default django popup_response.js
    var initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch (initData.action) {
        case 'change':
            if (typeof(openerRef.dismissChangeRelatedObjectPopup) === 'function') {
                openerRef.dismissChangeRelatedObjectPopup(windowRef, initData.value, initData.obj, initData.new_value);
=======
    }

    // select before last iframe content window if exists else select openerRef
    let openerRef2;
    var iframeHTMLCollection = openerRef.document.getElementsByClassName('related-iframe');
    if (iframeHTMLCollection.length >= 2) {
        var beforeLastIframeIndex = iframeHTMLCollection.length - 2;
        openerRef2 = iframeHTMLCollection[beforeLastIframeIndex].contentWindow;
    } else {
        openerRef2 = openerRef;
    }

    // default django popup_response.js
    const initData = JSON.parse(document.getElementById('django-admin-popup-response-constants').dataset.popupResponse);
    switch (initData.action) {
        case 'change':
            if (typeof(openerRef.dismissChangeRelatedObjectPopup) === 'function') {
                openerRef2.dismissChangeRelatedObjectPopup(windowRef, initData.value, initData.obj, initData.new_value);
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
            }
            break;
        case 'delete':
            if (typeof(openerRef.dismissDeleteRelatedObjectPopup) === 'function') {
<<<<<<< HEAD
                openerRef.dismissDeleteRelatedObjectPopup(windowRef, initData.value);
=======
                openerRef2.dismissDeleteRelatedObjectPopup(windowRef, initData.value);
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
            }
            break;
        default:
            if (typeof(openerRef.dismissAddRelatedObjectPopup) === 'function') {
<<<<<<< HEAD
                openerRef.dismissAddRelatedObjectPopup(windowRef, initData.value, initData.obj);
            }
            else if (typeof(openerRef.dismissAddAnotherPopup) === 'function') {
                // django 1.7 compatibility
                openerRef.dismissAddAnotherPopup(windowRef, initData.value, initData.obj);
=======
                openerRef2.dismissAddRelatedObjectPopup(windowRef, initData.value, initData.obj);
            }
            else if (typeof(openerRef.dismissAddAnotherPopup) === 'function') {
                // django 1.7 compatibility
                openerRef2.dismissAddAnotherPopup(windowRef, initData.value, initData.obj);
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
            }
            break;
    }

<<<<<<< HEAD
})();
=======
})();
>>>>>>> 0e80b163243e2528e53a85aa689c67c56da1b044
