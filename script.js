let selectedFile;

function selectFile() {

document
.getElementById(
"fileInput"
)
.click();

}

document
.getElementById(
"fileInput"
)
.addEventListener(
"change",
function(event) {

selectedFile =
event.target.files[0];

});

function uploadImage() {

if (!selectedFile) {

alert("Please select image");

return;

}

let formData =
new FormData();

formData.append(
"file",
selectedFile
);

document
.getElementById(
"loader"
)
.classList
.remove("hidden");

fetch("/predict", {

method: "POST",

body: formData

})

.then(
response =>
response.json()
)

.then(data => {

document
.getElementById(
"loader"
)
.classList
.add("hidden");

document
.getElementById(
"result"
)
.classList
.remove("hidden");

document
.getElementById(
"disease"
)
.innerText =
"Disease: " +
data.disease;

document
.getElementById(
"treatment"
)
.innerText =
"Treatment: " +
data.treatment;

document
.getElementById(
"confidenceBar"
)
.style.width =
data.confidence +
"%";

});
}
