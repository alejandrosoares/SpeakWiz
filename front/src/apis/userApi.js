import { StatusCodes } from 'http-status-codes';
import Request from '../utils/request';
import { API_URL } from '../utils/constants/urls';
import formatResponseByStatusCode from '../utils/response';

const userApi = {
  URL: `${API_URL}users/`,

  async signUp(data) {
    const req = new Request.Builder(`${this.URL}sign-up/`)
      .withBody(data)
      .withPostMethod()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.CREATED, res.status, res.data);
  },

  async logIn(data) {
    const req = new Request.Builder(`${this.URL}log-in/`)
      .withBody(data)
      .withPostMethod()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },

  async getUserByToken() {
    const req = new Request.Builder(`${this.URL}get-user/`)
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },
};

export default userApi;
