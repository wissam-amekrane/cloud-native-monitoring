import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,             // 10 utilisateurs simultanés
  duration: '30s',     // pendant 30 secondes
};

export default function () {
  const res = http.post('http://localhost:8000/service-age', JSON.stringify({
    birthdate: "2000-01-01"
  }), {
    headers: { 'Content-Type': 'application/json' },
  });

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1); // pause entre les appels
}