document.getElementById("cbx-chart").addEventListener("change", function () {
  var value = this.value;
  var dateBetween = document.querySelector(".date-between");
  var listProduct = document.querySelector(".list-product");

  switch (value) {
    case "1":
      dateBetween.style.display = "none";
      listProduct.style.display = "none";
      break;
    case "2":
      dateBetween.style.display = "none";
      listProduct.style.display = "flex";
      break;
    case "3":
      dateBetween.style.display = "none";
      listProduct.style.display = "none";
      break;
    case "4":
      dateBetween.style.display = "none";
      listProduct.style.display = "none";
      break;
    case "5":
      dateBetween.style.display = "none";
      listProduct.style.display = "none";
      break;
    case "6":
      dateBetween.style.display = "none";
      listProduct.style.display = "flex";
      break;
    case "7":
      dateBetween.style.display = "none";
      listProduct.style.display = "flex";
      break;
    case "8":
      dateBetween.style.display = "none";
      listProduct.style.display = "flex";
      break;
    case "9":
      dateBetween.style.display = "block";
      listProduct.style.display = "none";
      break;
  }
});

function selected(id) {
  var item = document.getElementById(id);
  items = document.querySelectorAll(".product");
  Array.from(items).forEach((element) => {
    element.style.backgroundColor = "#fff";
  });
  item.style.backgroundColor = "#ddd";
}
