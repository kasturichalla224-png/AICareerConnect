/**
 * app.js — Global JavaScript
 * Shared utilities loaded on every page.
 */

// Auto-dismiss flash alerts after 5 seconds
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".alert").forEach((alert) => {
        setTimeout(() => {
            alert.style.transition = "opacity .4s ease";
            alert.style.opacity = "0";
            setTimeout(() => alert.remove(), 400);
        }, 5000);
    });
});
