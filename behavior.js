var thumbnailElement = document.getElementById("smart_thumbnail");

document.addEventListener("DOMContentLoaded", function(event) {
    thumbnailElement.addEventListener("click", function() {
        if (thumbnailElement.className.includes("small")) {
            thumbnailElement.className = thumbnailElement.className.replace("small", "");
        } else {
            thumbnailElement.className += " small";
        }
    });
});