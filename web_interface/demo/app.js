const uploadForm = document.getElementById("upload-form");
const modelList = document.getElementById("model-list");
const gpuStats = document.getElementById("gpu-stats");
const uploadStatus = document.getElementById("upload-status");

async function fetchModels() {
  const response = await fetch("/api/model/monitor");
  const models = await response.json();
  modelList.innerHTML = "";
  models.forEach((model) => {
    const item = document.createElement("li");
    item.textContent = `${model.name} — ${model.status}`;
    modelList.appendChild(item);
  });
}

async function fetchGpuStats() {
  const response = await fetch("/api/gpu/stats");
  const stats = await response.json();
  gpuStats.innerHTML = "";
  stats.forEach((stat) => {
    const item = document.createElement("li");
    item.textContent = `Utilization ${stat.utilization}% · Memory ${stat.memory_used} / ${stat.memory_total} MB`;
    gpuStats.appendChild(item);
  });
}

uploadForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const fileInput = document.getElementById("model-file");
  if (!fileInput.files.length) {
    uploadStatus.textContent = "Please choose a model file to upload.";
    return;
  }
  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  uploadStatus.textContent = "Uploading...";
  const response = await fetch("/api/model/upload", {
    method: "POST",
    body: formData,
  });
  const result = await response.json();
  uploadStatus.textContent = result.message || "Upload complete.";
  await fetchModels();
});

async function refresh() {
  await fetchModels();
  await fetchGpuStats();
}

refresh();
setInterval(fetchGpuStats, 5000);
