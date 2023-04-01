$(document).ready(function () {
  // Add event listener to search input field
  var searchInput = document.getElementById("search-input");
  searchInput.addEventListener("input", search);

  function search() {
    // Get the search query entered by the user
    var query = searchInput.value.toLowerCase();

    // Get all the year headers in the page
    var yearHeaders = document.querySelectorAll(".year");

    // Loop through each year header and its associated bibliography
    for (var i = 0; i < yearHeaders.length; i++) {
      var yearHeader = yearHeaders[i];
      var bibliography = yearHeader.nextElementSibling;

      // Check if the next sibling element is an ol element with the class "bibliography"
      while (
        bibliography &&
        bibliography.nodeName.toLowerCase() !== "ol" &&
        !bibliography.classList.contains("bibliography")
      ) {
        bibliography = bibliography.nextElementSibling;
      }

      // Check if any item in the bibliography matches the search query
      var items = bibliography.querySelectorAll("li");
      var hasMatch = false;
      for (var j = 0; j < items.length; j++) {
        var item = items[j];
        var title = item.querySelector(".title").textContent.toLowerCase();
        var author = item.querySelector(".author").textContent.toLowerCase();
        var periodical = item
          .querySelector(".periodical")
          .textContent.toLowerCase();
        var abstract = item.querySelector(".abstract p");
        var abstractText = abstract ? abstract.textContent.toLowerCase() : "";

        if (
          title.indexOf(query) > -1 ||
          author.indexOf(query) > -1 ||
          periodical.indexOf(query) > -1 ||
          abstractText.indexOf(query) > -1
        ) {
          hasMatch = true;
          item.style.display = "";
        } else {
          item.style.display = "none";
        }
      }

      // Hide or show the year header and bibliography based on the search query
      if (hasMatch) {
        yearHeader.style.display = "";
        bibliography.style.display = "";
      } else {
        yearHeader.style.display = "none";
        bibliography.style.display = "none";
      }
    }
  }
});
