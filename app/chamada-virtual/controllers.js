import {
    Alert,
    AsyncStorage
} from 'react-native';


const qs = require('qs');

const methods = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
};
const url_dev = "http://10.42.0.1:8000/"
const url_prod = "https://daviwesleyvk.pythonanywhere.com/"

const request = (method, endpoint, options) => {
    const result = new Promise((resolve, reject) => {
        let url = url_dev + endpoint;

        const headers = {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        };
        if (options.token) {
            headers.Authorization = `Token ${options.token}`;
        }

        let body = null;
        if (method === methods.GET) {
            url += qs.stringify(options.params);
        } else {
            body = JSON.stringify(options.params);
        }

        fetch(url, {
            method,
            headers,
            body,
        }).then((response) => {
            response.json().then((data) => {
                if (response.ok) {
                    resolve(data);
                } else {
                    reject(data);
                }
            }).catch(() => {
                if (!options.ignoreErrors) {
                    Alert.alert('Erro', 'Operação inválida.');
                }
                reject();
            });
        }).catch(() => {
            if (!options.ignoreErrors) {
                Alert.alert('Erro', 'Não foi possível estabelecer uma conexão com o servidor. Verifique sua internet.');
            }
            reject();
        });
    });

    return result;
};

export const returnToken = () => {
    return AsyncStorage.getItem('token')
}

export const criarDisciplina = (nome, hora, credito, id_professor, token) => {
    const data = {
        "name": nome,
        "hours": hora,
        "credit": credito,
        "teacher": [id_professor]
    }
    request(methods.POST, 'api/disciplinas', { token, params: data });
}

export const inserirFalta = (quantFaltas, matricula, disciplina, token) => {
    const data = {
        "faults": quantFaltas,
        "student": matricula,
        "subject": disciplina
    }
    return request(methods.POST, 'api/faltas', { token, params: data });
};

export const getAlunos = (token) => {

    return request(methods.GET, 'api/alunos', { token });
};

export const getToken = (nome, senha) => {
    const data = {
        username: nome,
        password: senha
    };
    return request(methods.POST, 'api/api-token', { params: data });
};

export const criarAluno = (nome, matricula, curso, disciplina, token) => {
    const data = {
        name: nome,
        id_subscription: matricula,
        course: curso,
        subject: [disciplina]
    };
    return request(methods.POST, 'api/alunos', { token, params: data });
};
