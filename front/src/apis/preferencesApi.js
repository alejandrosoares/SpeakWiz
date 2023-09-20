import { StatusCodes } from 'http-status-codes';
import Request from '../utils/request';
import { API_URL } from '../utils/constants/urls';
import formatResponseByStatusCode from '../utils/response';

const preferencesApi = {
  URL: `${API_URL}preferences/`,

  async create(data) {
    const req = new Request.Builder(this.URL)
      .withBody(data)
      .withAuthentication()
      .withPostMethod()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.CREATED, res.status, res.data);
  },

  async getAll() {
    const req = new Request.Builder(this.URL)
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },
};

export default preferencesApi;
