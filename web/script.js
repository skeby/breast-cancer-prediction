const apiUrl = "https://breast-cancer-prediction-jzta.onrender.com";

// Top Breast cancer dataset features
const featureNames = [
  "worst area",
  "worst concave points",
  "mean concave points",
  "worst radius",
  "worst perimeter",
  "mean perimeter",
  "mean concavity",
  "mean area",
  "worst concavity",
  "mean radius",
];
const inputsDiv = document.getElementById("inputs");

// Generate inputs dynamically
featureNames.forEach((name, index) => {
  const formField = document.createElement("div");
  formField.className = "form-field";
  const label = document.createElement("label");
  label.textContent = name;
  const input = document.createElement("input");
  input.type = "number";
  input.step = "any";
  input.required = true;
  input.name = `feature-${index}`;
  formField.appendChild(label);
  formField.appendChild(input);
  inputsDiv.appendChild(formField);
});

document.getElementById("form").addEventListener("submit", async function (e) {
  e.preventDefault();
  const form = e.target;
  const features = Array.from(form.elements)
    .filter((el) => el.type === "number")
    .map((el) => parseFloat(el.value));

  const res = await fetch(`${apiUrl}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ features }),
  });

  const data = await res.json();
  if (data.prediction !== undefined) {
    alert(
      data.prediction === 1 ? "Prediction: Malignant" : "Prediction: Benign"
    );
  } else {
    alert("Error: " + data.error);
  }
});
