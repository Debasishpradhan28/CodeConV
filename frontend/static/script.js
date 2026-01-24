const languages = [
    "Python",
    "Python 3",
    "C",
    "C++",
    "Java",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust",
    "Kotlin",
    "Swift",
    "PHP",
    "Ruby",
    "Dart",
    "R",
    "Bash",
    "PowerShell",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Pseudocode"
];

function loadLanguages() {
    const source = document.getElementById("sourceLang");
    const target = document.getElementById("targetLang");

    languages.forEach(lang => {
        const opt1 = document.createElement("option");
        opt1.value = lang;
        opt1.textContent = lang;

        const opt2 = document.createElement("option");
        opt2.value = lang;
        opt2.textContent = lang;

        source.appendChild(opt1);
        target.appendChild(opt2);
    });
}
const flowBtn = document.getElementById("flowBtn");
window.onload = loadLanguages;
flowBtn.disabled = true;


function openFlowchart() {
    window.location.href = "/flowchart";
}


async function handleAction(mode) {
    const inputCode = document.getElementById("inputCode").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    if (!inputCode.trim()) {
        alert("Please enter some code.");
        return;
    }

    document.getElementById("outputCode").value =
        mode === "convert"
            ? "Converting code..."
            : mode === "explain"
            ? "Analyzing logic..."
            : "Extracting program logic...";

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                source: sourceLang,
                target: targetLang,
                code: inputCode,
                mode: mode
            })
        });

        const data = await response.json();

if (mode === "ir") {
    sessionStorage.setItem(
        "latestFlowchart",
        data.result
    );


    document.getElementById("flowBtn").disabled = false;
}


if (mode === "explain") {
    document.getElementById("outputCode").value =
        "PROGRAM LOGIC EXPLANATION\n\n" + data.result;
} else {
    document.getElementById("outputCode").value =
        typeof data.result === "string"
            ? data.result
            : JSON.stringify(data.result, null, 2);
}



    } catch (err) {
        document.getElementById("outputCode").value =
            "Something went wrong.";
    }
}
