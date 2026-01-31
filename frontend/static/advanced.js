async function runAnalysis(mode) {

    const code = sessionStorage.getItem("latestCode");

    if (!code) {
        alert("Please go back and enter code first.");
        return;
    }

    const output = document.getElementById("analysisOutput");
    output.textContent = "AI is analyzing your code...\nPlease wait...";

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                code: code,
                mode: mode
            })
        });

        const data = await response.json();
        output.textContent = data.result;

    } catch (err) {
        output.textContent = "Unable to connect to backend.";
    }
}

function goBack() {
    window.location.href = "/";
}
