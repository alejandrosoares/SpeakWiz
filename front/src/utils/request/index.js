import LOCAL_STORAGE from '../constants/localstorage';
import authenticationToken from '../authentication';

class Request {
  constructor(build) {
    this.url = build.url;
    this.body = build.body;
    this.method = build.method;
    this.headers = build.headers;
  }

  buildRequest = () => {
    const req = {
      method: this.method,
      headers: this.headers,
      body: this.body ? JSON.stringify(this.body) : null,
    };
    return req;
  };

  send = async () => {
    const req = this.buildRequest();
    const res = await fetch(this.url, req);
    const data = await res.json();
    return {
      data,
      status: res.status,
    };
  };

  static get Builder() {
    class Builder {
      constructor(url) {
        this.url = url;
        this.method = 'GET';
        this.headers = new Headers({ 'Content-Type': 'application/json' });
        this.body = null;
      }

      withBody(body) {
        this.body = body;
        return this;
      }

      withPostMethod() {
        const csrfToken = localStorage.getItem(LOCAL_STORAGE.CSRF_TOKEN);
        this.method = 'POST';
        this.headers.set('X-CSRFToken', csrfToken);
        return this;
      }

      withDeleteMethod() {
        this.method = 'DELETE';
        return this;
      }

      withAuthentication() {
        const authToken = authenticationToken.get();
        this.headers.set('Authorization', authToken);
        return this;
      }

      build() {
        return new Request(this);
      }
    }

    return Builder;
  }
}

export default Request;
