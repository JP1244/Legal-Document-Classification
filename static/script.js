async function convertText() {
  const inputText = document.getElementById("input-text").value;
  const fromFont = document.getElementById("fromFont").value;
  const toFont = document.getElementById("toFont").value;

  const response = await fetch("/convert", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ inputText, fromFont, toFont })
  });

  const data = await response.json();
  document.getElementById("output-text").value = data.convertedText;
}


const showMenu = (toggleId, navId) => {
    const toggle =  document.getElementById(toggleId);
    const nav = document.getElementById(navId);

    if(toggle && nav){
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show');
            toggle.classList.toggle('bx-x');
        })
    }
}

showMenu('header-toggle', 'nav-menu');

const navLink = document.querySelectorAll('.nav-link');
function linkAction(){
    navLink.forEach(n => n.classList.remove('active'));
    this.classList.add('active');
}

navLink.forEach(n => n.addEventListener('click', linkAction));