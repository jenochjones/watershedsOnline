import {setUpMap} from "./mapPackage.js";

function ready(readyListener) {
    if (document.readyState !== "loading") {
        readyListener();
    } else {
        document.addEventListener("DOMContentLoaded", readyListener);
    }
};

ready(function () {
    setUpMap();
});