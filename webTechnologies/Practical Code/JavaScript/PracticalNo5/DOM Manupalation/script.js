// Printing In JavaScript
console.log("Hello World");

// Selecting An Element Through DOM By Class Name
let demoClass = document.getElementsByClassName("demoClass")[0];
console.log(demoClass);
console.log(demoClass.innerHTML);

// Selecting An Element Through DOM By ID
let demoID = document.getElementById("demoID");
console.log(demoID);
console.log(demoID.innerHTML);

// By Using Query Selector
let demoQuery = document.querySelector(".demoClass");
console.log(demoQuery);
console.log(demoQuery.innerHTML);

// Handling Click Event
let button = document.querySelector("button");
button.addEventListener("click", function () {
    let newParagraph = document.createElement("p");
    newParagraph.innerHTML = "This Is New Paragraph By Click";
    document.body.appendChild(newParagraph);
});

// Handling Hover Event
let buttonHover = document.querySelector(".buttonHover");
buttonHover.addEventListener("mouseover", function () {
    let newParagraph = document.createElement("p");
    newParagraph.innerHTML = "This Is New Paragraph By Hover";
    document.body.appendChild(newParagraph);
});