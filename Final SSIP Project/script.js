
document.getElementById("feedbackForm").addEventListener("submit", function(event) {
    var email = document.getElementById("email").value;
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    var rating = parseInt(document.getElementById("rating").value);
    var emailError = document.getElementById("emailError");
    var ratingError = document.getElementById("ratingError");

    // Reset error messages
    emailError.textContent = "";
    ratingError.textContent = "";

    if (!emailPattern.test(email)) {
        emailError.textContent = "Please enter a valid email address.";
        event.preventDefault(); // Prevent the form from submitting
    } else if (rating < 1 || rating > 10) {
        ratingError.textContent = "Rating must be between 1 and 10.";
        event.preventDefault();
    } else {
        // Simulate a successful form submission (replace this with actual form submission code)
        alert("Feedback submitted successfully!");
        clearForm(); // Clear the form fields
        event.preventDefault(); // Prevent the form from submitting for demonstration purposes
    }
});

function clearForm() {
    // Clear form fields after successful submission
    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = "";
    document.getElementById("email").value = "";
    document.getElementById("comments").value = "";
    document.getElementById("rating").value = "";
}