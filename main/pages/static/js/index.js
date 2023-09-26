const navbar = document.getElementById('#navbar');

function startAnimation() {
    let evtId = null;
    setInterval(transitionImage, 3000); // 20 second refresh timer
    let time = 1000;            // 1 second
    let refreshRate = 20;       // refreshes every 20ms
    let ticks = 0;
    let iteration = Math.floor(Math.random()*2);
    let frontendImage = document.getElementById('img');
    let images = ['/static/img/ditto.svg', '/static/img/venn.svg'];
    function transitionImage() {
        evtId = setInterval(flyOldDown, 20)
    }
    function flyOldDown() {
        if (ticks >= (time / refreshRate) / 2) {
            clearInterval(evtId);
            evtId = setInterval(flyNewDown, 20);
            frontendImage.src = frontendImage[iteration % 2];
            iteration += 1;
            ticks = 0;
            frontendImage.style.top = `${500}px`
        }
        else {
            frontendImage.style.top += `${6}px`;
            ticks+=1;
        }
    }
    function flyNewDown() {
        if (ticks >= (time / refreshRate) / 2) {
            clearInterval(evtId);
            ticks = 0;
        }
        else {
            frontendImage.style.top += `${6}px`;
            ticks+=1;
        }
    }
}

var timeout = false;

function toggleSidebar(){
    if (timeout) return;
    let sidebar = document.getElementById("sidebar");
    let overlay = document.getElementById("overlay");
    console.log(sidebar.style.display);
    if (sidebar.style.display == "") {
        sidebar.style.display = "flex";
        toggleOpaque(true);
        console.log(sidebar.style.opacity);
        console.log('hi1');
    }
    else {
        sidebar.style.display = "";
        toggleOpaque(false);
        console.log('hi2');

    }
    timeout = true;
    setTimeout(() => {timeout = false}, 100)
}

function toggleOpaque(dim) {
    let navbar = document.getElementById("navbar");
    let main = document.getElementById("main");
    if (!dim) {
        main.style.opacity = "100%";
        // navbar.style.opacity = "100%";
    }
    else {
        main.style.opacity = "40%";
        // navbar.style.opacity = "40%";
    }
}

// window.onscroll = () => {}

// function scrollFunction() {
//     if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
//         navbar.style.display = block;
//     }
// }