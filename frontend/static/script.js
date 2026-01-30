const languages = [
    "Python", "Python 3", "C", "C++", "Java", "JavaScript",
    "TypeScript", "Go", "Rust", "Kotlin", "Swift", "PHP",
    "Ruby", "Dart", "R", "Bash", "PowerShell",
    "SQL", "MySQL", "PostgreSQL", "Pseudocode"
];

window.onload = () => {
    loadLanguages();
    const flowBtn = document.getElementById("flowBtn");
    if (flowBtn) flowBtn.disabled = true;
};

function loadLanguages() {
    const source = document.getElementById("sourceLang");
    const target = document.getElementById("targetLang");

    languages.forEach(lang => {
        source.add(new Option(lang, lang));
        target.add(new Option(lang, lang));
    });
}

function openFlowchart() {
    window.location.href = "/flowchart";
}

async function handleAction(mode) {
    const inputCode = document.getElementById("inputCode").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;
    const output = document.getElementById("outputCode");

    if (!inputCode.trim()) {
        alert("Please enter some code.");
        return;
    }

    output.value =
        mode === "convert"
            ? "Converting code..."
            : mode === "explain"
            ? "Explaining logic..."
            : "Generating program logic...";

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
           sessionStorage.setItem("latestFlowchart", data.result);

           document.getElementById("outputCode").value =
            `LOGIC EXTRACTED SUCCESSFULLY

        ──────── PROGRAM LOGIC (IR) ────────

          ${data.result}

        ──────── END ────────

        Click the flowchart button to visualize this logic.`;

        document.getElementById("flowBtn").disabled = false;
        return;
 }



        if (mode === "explain") {
            document.getElementById("outputCode").value =
            "PROGRAM LOGIC EXPLANATION\n\n" + data.result;
            return;
        }


document.getElementById("outputCode").value = data.result;


    } catch (err) {
        output.value = "Unable to connect to backend.";
    }
}
