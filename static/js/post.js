// post.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const titleInput = document.getElementById("title");

    // Highlight form when typing title
    titleInput.addEventListener("input", function() {
        if (titleInput.value.trim().length > 0) {
            titleInput.style.borderColor = "#4a90e2";
        } else {
            titleInput.style.borderColor = "#ccc";
        }
    });

    // Confirmation before submitting
    form.addEventListener("submit", function(e) {
        const confirmed = confirm("Are you sure you want to submit this post?");
        if (!confirmed) {
            e.preventDefault();
        }
    });
});
