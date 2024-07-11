// Funções existentes
function showRegisterForm() {
    hideAllForms();
    document.getElementById("registerForm").style.display = "block";
}

function showEntryForm() {
    hideAllForms();
    document.getElementById("entryForm").style.display = "block";
}

function showExitForm() {
    hideAllForms();
    document.getElementById("exitForm").style.display = "block";
}

function showRecords() {
    hideAllForms();
    document.getElementById("records").style.display = "block";
    fetchRecords();
}

function hideAllForms() {
    document.getElementById("registerForm").style.display = "none";
    document.getElementById("entryForm").style.display = "none";
    document.getElementById("exitForm").style.display = "none";
    document.getElementById("records").style.display = "none";
}

// Função atualizada para utilizar Axios
function registerEmployee() {
    let employeeId = document.getElementById("employeeId").value;
    let employeeName = document.getElementById("employeeName").value;

    axios.post('/register_employee', {
        employeeId: employeeId,
        employeeName: employeeName
    })
    .then(response => {
        alert(response.data.message);
    })
    .catch(error => {
        console.error('Erro ao registrar funcionário:', error);
    });
}

// Função atualizada para utilizar Axios
function recordEntry() {
    let employeeId = document.getElementById("entryEmployeeId").value;

    axios.post('/record_entry', {
        employeeId: employeeId
    })
    .then(response => {
        alert(response.data.message);
    })
    .catch(error => {
        console.error('Erro ao registrar entrada:', error);
    });
}

// Função atualizada para utilizar Axios
function recordExit() {
    let employeeId = document.getElementById("exitEmployeeId").value;

    axios.post('/record_exit', {
        employeeId: employeeId
    })
    .then(response => {
        alert(response.data.message);
    })
    .catch(error => {
        console.error('Erro ao registrar saída:', error);
    });
}

// Função original mantida
function fetchRecords() {
    fetch('/fetch_records')
    .then(response => response.json())
    .then(records => {
        let recordsList = document.getElementById("recordsList");
        recordsList.innerHTML = ''; // Limpa a lista de registros

        records.forEach(record => {
            let recordElement = document.createElement("div");
            recordElement.innerHTML = `
                <strong>Funcionário:</strong> ${record.employee} | 
                <strong>Ação:</strong> ${record.action} | 
                <strong>Timestamp:</strong> ${record.timestamp} | 
                <strong>Foto:</strong> <img src="${record.photo}" style="max-width: 100px; max-height: 100px;">
            `;
            recordsList.appendChild(recordElement);
        });
    })
    .catch(error => console.error('Erro ao buscar registros:', error));
}

// Função original mantida
function verifyChain() {
    fetch('/verify_chain')
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Erro ao verificar cadeia:', error));
}
