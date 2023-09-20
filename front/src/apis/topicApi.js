import { StatusCodes } from 'http-status-codes';
import Request from '../utils/request';
import { API_URL } from '../utils/constants/urls';
import formatResponseByStatusCode from '../utils/response';

const topicApi = {
  URL: `${API_URL}topics/`,

  async getById(id) {
    const req = new Request.Builder(this.URL + id)
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },

  async getAll() {
    const req = new Request.Builder(this.URL).build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },
};

export default topicApi;
