const token = localStorage.getItem("token");
const taskForm = document.getElementById("task-form");
const tasksList = document.getElementById("tasks-list");
const logoutButton = document.getElementById("logout");

let editingTaskId = null;

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

    if (!response.ok || data.data.length === 0) {
        tasksList.innerHTML = "<p>Nenhuma tarefa encontrada.</p>";
        return;
    }

    data.data.forEach(function (task) {
        const taskItem = document.createElement("div");

        taskItem.innerHTML = `
            <h3>${task.title}</h3>
            <p>${task.description}</p>

            <button
                type="button"
                class="edit-task"
                data-id="${task.id_task}"
                data-title="${task.title}"
                data-description="${task.description}">
                Editar
            </button>

            <button
                type="button"
                class="delete-task"
                data-id="${task.id_task}">
                Excluir
            </button>
        `;

        tasksList.appendChild(taskItem);
    });

    const editButtons = document.querySelectorAll(".edit-task");

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            editingTaskId = button.getAttribute("data-id");

            document.getElementById("title").value =
                button.getAttribute("data-title");

            document.getElementById("description").value =
                button.getAttribute("data-description");
        });
    });

    const deleteButtons = document.querySelectorAll(".delete-task");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", async function () {

            const taskId = button.getAttribute("data-id");

            const response = await fetch(`/tasks/${taskId}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            });

            if (response.ok) {
                await carregarTarefas();
            } else {
                alert("Erro ao excluir tarefa.");
            }
        });
    });
}

if (taskForm) {
    taskForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;

        const url = editingTaskId
            ? `/tasks/${editingTaskId}`
            : "/tasks";

        const method = editingTaskId
            ? "PUT"
            : "POST";

        const response = await fetch(url, {
            method: method,
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

            editingTaskId = null;

            await carregarTarefas();

        } else {
            alert("Erro ao salvar tarefa.");
        }
    });
}

carregarTarefas();