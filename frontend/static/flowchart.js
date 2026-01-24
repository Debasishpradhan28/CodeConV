const chart = sessionStorage.getItem("latestFlowchart");

if (!chart) {
    alert("Please click View Logic first.");
} else {
    document.getElementById("diagram").innerHTML = chart;
    mermaid.initialize({ startOnLoad: true });
}
function goBack() {
    window.history.back();
}
