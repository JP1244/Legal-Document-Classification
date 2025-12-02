function handleUpload() {
  const input = document.getElementById('fileInput');
  const file = input.files[0];

  if (!file) {
    alert("Please choose a file.");
    return;
  }

  document.getElementById("file-name").innerText = `Uploading: ${file.name}`;

  const formData = new FormData();
  formData.append("file", file);

  fetch("/upload", {
    method: "POST",
    body: formData,
  })
    .then((res) => {
      if (res.redirected) {
        window.location.href = res.url;
      } else {
        return res.json();
      }
    })
    .then((data) => {
      if (data && data.error) {
        document.getElementById("file-name").innerText = "Error: " + data.error;
      }
    })
    .catch((err) => {
      console.error(err);
      document.getElementById("file-name").innerText = "Upload failed.";
    });
}
