import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 10,           
  duration: '30s',     
};

export default function () {
  const res = http.post('http://localhost:8000/service-poids', JSON.stringify({
    height: 175  
  }), {
    headers: { 'Content-Type': 'application/json' },
  });

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1); // pause entre les appels
}
