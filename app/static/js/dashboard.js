/**
 * dashboard.js — Dynamic Dashboard Charts
 * Fetches stats from the backend API and renders Chart.js visualizations.
 */

document.addEventListener("DOMContentLoaded", async () => {
    try {
        // ── Fetch user stats ────────────────────────────────────────
        const statsRes = await fetch("/dashboard/api/stats");
        const stats = await statsRes.json();

        document.getElementById("stat-sessions").textContent = stats.total_sessions;
        document.getElementById("stat-speech").textContent = stats.total_speech_interactions;

        // ── Career Fields Doughnut Chart ────────────────────────────
        const fieldsCtx = document.getElementById("fieldsChart").getContext("2d");
        const fields = stats.career_fields || {};

        new Chart(fieldsCtx, {
            type: "doughnut",
            data: {
                labels: Object.keys(fields),
                datasets: [{
                    data: Object.values(fields),
                    backgroundColor: [
                        "#6c5ce7", "#00cec9", "#fdcb6e",
                        "#e17055", "#00b894", "#a29bfe",
                        "#74b9ff", "#fab1a0",
                    ],
                    borderWidth: 0,
                }],
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: "bottom",
                        labels: { color: "#e4e6f0", padding: 16 },
                    },
                },
            },
        });

        // ── Platform Metrics Bar Chart ──────────────────────────────
        const metricsRes = await fetch("/dashboard/api/metrics");
        const metrics = await metricsRes.json();
        const metricsCtx = document.getElementById("metricsChart").getContext("2d");

        new Chart(metricsCtx, {
            type: "bar",
            data: {
                labels: metrics.map((m) => m.name),
                datasets: [{
                    label: "Value",
                    data: metrics.map((m) => m.value),
                    backgroundColor: "rgba(108, 92, 231, .6)",
                    borderColor: "#6c5ce7",
                    borderWidth: 1,
                    borderRadius: 6,
                }],
            },
            options: {
                responsive: true,
                scales: {
                    x: { ticks: { color: "#8b8fa3" }, grid: { display: false } },
                    y: { ticks: { color: "#8b8fa3" }, grid: { color: "#2e3348" } },
                },
                plugins: {
                    legend: { display: false },
                },
            },
        });
    } catch (err) {
        console.error("Dashboard load error:", err);
    }
});
