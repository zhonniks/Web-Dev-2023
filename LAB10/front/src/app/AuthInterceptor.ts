import {HttpEvent, HttpHandler, HttpInterceptor, HttpRequest} from "@angular/common/http";
import {Injectable} from "@angular/core";
import {Observable} from "rxjs";

@Injectable()
export class AuthInterceptor implements HttpInterceptor{
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.log(req)
    const token = localStorage.getItem("token");
    if(token){
      const newReq = req.clone({
        headers: req.headers.append("Authorization", `Bearer ${token}`)
      })
      return next.handle(newReq);
    }
    return next.handle(req);
  }
}
