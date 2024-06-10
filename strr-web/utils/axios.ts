import { AxiosInstance } from 'axios'

export function addAxiosInterceptors (axiosInstance: AxiosInstance, contentType?: string): AxiosInstance {
  axiosInstance.interceptors.request.use(
    (config) => {
      const token = useBcrosKeycloak().kc.token
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
      if (contentType) {
        config.headers['Content-Type'] = contentType
      }
      return config
    },
    err => Promise.reject(err))
  return axiosInstance
}
