document.addEventListener('DOMContentLoaded', () => {
    const taskForm = document.getElementById('task-form');
    const taskInput = document.getElementById('task-input');
    const taskList = document.getElementById('task-list');

    const fetchTasks = async () => {
        const response = await fetch('/tasks/');
        const tasks = await response.json();
        taskList.innerHTML = '';
        tasks.forEach(task => addTaskToDOM(task));
    };

    const addTaskToDOM = task => {
        const li = document.createElement('li');
        li.textContent = task.description;
        li.dataset.id = task.id;
        if (task.completed) {
            li.classList.add('completed');
        }
        li.addEventListener('click', async () => {
            const response = await fetch(`/tasks/${task.id}`, {
                method: task.classList.contains('completed') ? 'DELETE' : 'PATCH',
            });
            if (response.ok) {
                if (task.classList.contains('completed')) {
                    li.remove();
                } else {
                    li.classList.toggle('completed');
                }
            }
        });
        taskList.appendChild(li);
    };

    taskForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const description = taskInput.value;
        const response = await fetch('/tasks/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ description }),
        });
        if (response.ok) {
            const newTask = await response.json();
            addTaskToDOM(newTask);
            taskInput.value = '';
        }
    });

    fetchTasks();
});





// ___________________________________________________________________________________








// document.addEventListener('DOMContentLoaded', () => {
//     const taskList = document.getElementById('task-list');

//     const fetchTasks = async () => {
//         const response = await fetch('/tasks/');
//         const tasks = await response.json();
//         taskList.innerHTML = '';
//         tasks.forEach(task => addTaskToDOM(task));
//     };

//     const addTaskToDOM = task => {
//         const li = document.createElement('li');
//         li.textContent = task.description;
//         li.dataset.id = task.id;
//         if (task.completed) {
//             li.classList.add('completed');
//         }
//         li.addEventListener('click', async () => {
//             const response = await fetch(`/tasks/${task.id}`, {
//                 method: 'PATCH'
//             });
//             const updatedTask = await response.json();
//             if (updatedTask.completed) {
//                 li.classList.add('completed');
//             } else {
//                 taskList.removeChild(li);
//                 fetch(`/tasks/${task.id}`, { method: 'DELETE' });
//             }
//         });
//         taskList.appendChild(li);
//     };

//     fetchTasks();
// });