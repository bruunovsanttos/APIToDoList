
const token = localStorage.getItem("token");
const taskForm = document.getElementById("task-form");
const tasksList = document.getElementById("tasks-list");
const logoutButton = document.getElementById("logout");

if (!token) {
    window.location.href = "/";
}

if (logoutButton) {
    logoutButton.addEventListener("click", async function () {
        await fetch("/logout", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        localStorage.removeItem("token");
        window.location.href = "/";
    });
}