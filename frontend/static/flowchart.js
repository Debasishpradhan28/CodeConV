const chart = sessionStorage.getItem("latestFlowchart");

if (!chart) {
    document.getElementById("diagram").innerHTML =
        "<p style='color:red;text-align:center;'>Please click View Logic first.</p>";
} else {
    mermaid.initialize({
        startOnLoad: false,
        theme: "default"
    });

    document.getElementById("diagram").innerHTML = chart;

    // Force render
    mermaid.run();
}

function goBack() {
    window.history.back();
}
