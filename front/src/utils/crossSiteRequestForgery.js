import { API_URL } from './constants/urls';
import Request from './request';
import LOCAL_STORAGE from './constants/localstorage';

(async () => {
  const url = `${API_URL}users/get-csrf-token/`;
  const req = new Request.Builder(url).build();
  const res = await req.send();
  const { data } = res;
  localStorage.setItem(LOCAL_STORAGE.CSRF_TOKEN, data.value);
})();
