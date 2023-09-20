import { StatusCodes } from 'http-status-codes';
import Request from '../utils/request';
import { API_URL } from '../utils/constants/urls';
import formatResponseByStatusCode from '../utils/response';

const cardApi = {
  URL: `${API_URL}topics/<topic_id>/cards/`,

  async getAll(topicId, auth = false) {
    const url = this.URL.replace('<topic_id>', topicId);
    const req = auth
      ? new Request.Builder(url).withAuthentication().build()
      : new Request.Builder(url).build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },
};

export default cardApi;
