import {
    Alert,
} from 'react-native';


const qs = require('qs');

const methods = {
    GET: 'GET',
    POST: 'POST',
    PUT: 'PUT',
};

const request = (method, endpoint, options) => {
    const result = new Promise((resolve, reject) => {
        let url = "https://daviwesleyvk.pythonanywhere.com/" + endpoint;

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

export const getAlunos = (token) => {
    const params = {
      pagination: true,
    };
  
    return request(methods.GET, 'api/alunos', { token });
  };

export const getToken = (nome, senha) => {
    const data = {
      username: nome,
      password: senha
    };
  
    return request(methods.POST, 'api/api-token', { params: data });
  };
