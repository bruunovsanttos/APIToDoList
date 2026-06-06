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

async function carregarTarefas() {
    const response = await fetch("/tasks", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await response.json();

    tasksList.innerHTML = "";

    if (!response.ok) {
        tasksList.innerHTML = "<p>Nenhuma tarefa encontrada.</p>";
        return;
    }

    data.data.forEach(function (task) {
        const taskItem = document.createElement("div");

        taskItem.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>
        `;

        tasksList.appendChild(taskItem);
    });
}

if (taskForm) {
    taskForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;

        const response = await fetch("/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                title: title,
                description: description
            })
        });

        if (response.ok) {
            taskForm.reset();
            carregarTarefas();
        } else {
            alert("Erro ao criar tarefa.");
        }
    });
}

carregarTarefas();