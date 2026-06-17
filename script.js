let currentImages = [];
let currentIndex = 0;

// Image Gallery Initialization
document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll(".gallery-item");
    items.forEach((item, index) => {
        item.addEventListener("click", () => {
            openLightbox(index);
        });
    });
    updateCurrentImageList();
});

// Update the list of active/visible images for Next/Prev buttons
function updateCurrentImageList() {
    currentImages = Array.from(document.querySelectorAll(".gallery-item"))
                        .filter(item => item.style.display !== "none")
                        .map(item => item.querySelector("img").src);
}

// Category Filtering Function
function filterImages(category) {
    // Active class toggle on buttons
    const buttons = document.querySelectorAll(".btn");
    buttons.forEach(btn => btn.classList.remove("active"));
    event.target.classList.add("active");

    const items = document.querySelectorAll(".gallery-item");
    items.forEach(item => {
        if (category === "all" || item.classList.contains(category)) {
            item.style.display = "block";
        } else {
            item.style.style.display = "none";
        }
    });
    updateCurrentImageList();
}

// Lightbox Open/Close & Navigation Functions
function openLightbox(index) {
    const clickedSrc = document.querySelectorAll(".gallery-item")[index].querySelector("img").src;
    currentIndex = currentImages.indexOf(clickedSrc);
    
    if (currentIndex === -1) currentIndex = 0;

    document.getElementById("lightbox-img").src = currentImages[currentIndex];
    document.getElementById("lightbox").style.display = "flex";
}

function closeLightbox() {
    document.getElementById("lightbox").style.display = "none";
}

function changeImage(direction) {
    currentIndex += direction;
    if (currentIndex >= currentImages.length) currentIndex = 0;
    if (currentIndex < 0) currentIndex = currentImages.length - 1;
    
    document.getElementById("lightbox-img").src = currentImages[currentIndex];
}

// Close Lightbox when clicking outside the image
document.getElementById("lightbox").addEventListener("click", (e) => {
    if (e.target.id === "lightbox") {
        closeLightbox();
    }
});
