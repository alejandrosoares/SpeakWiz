import LOCAL_STORAGE from './constants/localstorage';

const authenticationToken = {
  authKey: LOCAL_STORAGE.AUTH_TOKEN,

  save(token, remember) {
    sessionStorage.setItem(this.authKey, token.includes('Token') ? token : `Token ${token}`);
    if (remember) {
      localStorage.setItem(this.authKey, `Token ${token}`);
    }
  },

  get() {
    const token = sessionStorage.getItem(this.authKey);
    return token;
  },

  getFromLocalAndSave() {
    const token = localStorage.getItem(this.authKey);
    if (token) {
      this.save(token);
    }
    return token;
  },

  remove() {
    sessionStorage.removeItem(this.authKey);
    localStorage.removeItem(this.authKey);
  },
};

export default authenticationToken;
