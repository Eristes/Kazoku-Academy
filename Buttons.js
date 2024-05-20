function myFunction1() {
  document.getElementById("myDropdown1").classList.toggle("show");
}
function myFunction2() {
  document.getElementById("myDropdown2").classList.toggle("show");
}
function myFunction3() {
  document.getElementById("myDropdown3").classList.toggle("show");
}
function myFunction4() {
  document.getElementById("myDropdown4").classList.toggle("show");
}
function myFunction5() {
  document.getElementById("myDropdown5").classList.toggle("show");
}
function myFunction6() {
  document.getElementById("myDropdown6").classList.toggle("show");
}
function myFunction7() {
  document.getElementById("myDropdown7").classList.toggle("show");
}
function myFunction8() {
  document.getElementById("myDropdown8").classList.toggle("show");
}
function myFunction9() {
  document.getElementById("myDropdown9").classList.toggle("show");
}
function myFunction10() {
  document.getElementById("myDropdown10").classList.toggle("show");
}
function myFunction11() {
  document.getElementById("myDropdown11").classList.toggle("show");
}
function myFunction12() {
  document.getElementById("myDropdown12").classList.toggle("show");
}
function myFunction13() {
  document.getElementById("myDropdown13").classList.toggle("show");
}
function myFunction14() {
  document.getElementById("myDropdown14").classList.toggle("show");
}
function myFunction15() {
  document.getElementById("myDropdown15").classList.toggle("show");
}
function myFunction16() {
  document.getElementById("myDropdown16").classList.toggle("show");
}
function myFunction17() {
  document.getElementById("myDropdown17").classList.toggle("show");
}
function myFunction18() {
  document.getElementById("myDropdown18").classList.toggle("show");
}
function myFunction19() {
  document.getElementById("myDropdown19").classList.toggle("show");
}
function myFunction20() {
  document.getElementById("myDropdown20").classList.toggle("show");
}
function myFunction21() {
  document.getElementById("myDropdown21").classList.toggle("show");
}
function myFunction22() {
  document.getElementById("myDropdown22").classList.toggle("show");
}
function myFunction23() {
  document.getElementById("myDropdown23").classList.toggle("show");
}
function myFunction24() {
  document.getElementById("myDropdown24").classList.toggle("show");
}
function myFunction25() {
  document.getElementById("myDropdown25").classList.toggle("show");
}
function myFunction26() {
  document.getElementById("myDropdown26").classList.toggle("show");
}
function myFunction27() {
  document.getElementById("myDropdown27").classList.toggle("show");
}
function myFunction28() {
  document.getElementById("myDropdown28").classList.toggle("show");
}
function myFunction29() {
  document.getElementById("myDropdown29").classList.toggle("show");
}
function myFunction30() {
  document.getElementById("myDropdown30").classList.toggle("show");
}
function myFunction31() {
  document.getElementById("myDropdown31").classList.toggle("show");
}
function myFunction32() {
  document.getElementById("myDropdown32").classList.toggle("show");
}
function myFunction33() {
  document.getElementById("myDropdown33").classList.toggle("show");
}
function myFunction34() {
  document.getElementById("myDropdown34").classList.toggle("show");
}
function myFunction35() {
  document.getElementById("myDropdown35").classList.toggle("show");
}
function myFunction36() {
  document.getElementById("myDropdown36").classList.toggle("show");
}
function myFunction37() {
  document.getElementById("myDropdown37").classList.toggle("show");
}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}