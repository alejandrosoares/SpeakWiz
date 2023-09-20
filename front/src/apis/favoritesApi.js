import { StatusCodes } from 'http-status-codes';
import Request from '../utils/request';
import buildGetParams from '../utils/request/urlParams';
import { API_URL } from '../utils/constants/urls';
import formatResponseByStatusCode from '../utils/response';

const favoritesApi = {
  URL: `${API_URL}favorites/`,

  async create(data) {
    const req = new Request.Builder(this.URL)
      .withBody(data)
      .withAuthentication()
      .withPostMethod()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.CREATED, res.status, res.data);
  },

  async get(resourceType, resourceId) {
    const params = buildGetParams({ resourceType, resourceId });
    const req = new Request.Builder(this.URL + params)
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },

  async getAll() {
    const req = new Request.Builder(`${this.URL}resources/`)
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.OK, res.status, res.data);
  },

  async delete(id) {
    const params = buildGetParams({ resourceId: id });
    const req = new Request.Builder(this.URL + params)
      .withDeleteMethod()
      .withAuthentication()
      .build();
    const res = await req.send();
    return formatResponseByStatusCode(StatusCodes.NO_CONTENT, res.status, res.data);
  },
};

export default favoritesApi;
