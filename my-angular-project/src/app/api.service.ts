import { Injectable } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable, BehaviorSubject } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private baseURL = 'http://localhost:8000/'
  private dataSubject: BehaviorSubject<any> = new BehaviorSubject<any>(null);
  public data$: Observable<any> = this.dataSubject.asObservable();
  constructor(private http: HttpClient,private router: Router, private httpClient: HttpClientModule) { this.getdata(); }


  // LoginData: any;
  Login2(data: { email: any; password: any;  }) {
    console.log(data);
    this.http.post(this.baseURL + "login", data).subscribe(
        (result: any) => {
            console.log(result);
        },
        (error: any) => {
            console.error(error);
        }
    );
  //   console.log(data)
  //   this.LoginData = data;
  //   this.http.post(this.baseURL + "/loginA", data).subscribe((result: any) => {
  //     console.log(result, "dfdfd");
  //     if (result.token != "abc") {
  //       localStorage.setItem("token", result.token)
  //       // this.LoginData = data;
  //       this.profile();
  //       // this.router.navigate(['/StudentDash']);

  //     }
  //     else {
  //       if (this.LoginData.staus == "student") {
  //         this.router.navigate(['/StudentDash']);
  //       }
  //       if (this.LoginData.staus == "employee") { this.router.navigate(['/employee']); }
  //     }

  //   });
  }
  // logindataAPI: any;
  // profile() {
  //   let headers = new HttpHeaders()
  //     .set("authorization", `bearer ${localStorage.getItem('token')}`)
  //   this.http.post(this.baseURL + "/profile", {}, { headers }).subscribe((result: any) => {
  //     console.log(result, "fdfd")
  //     this.logindataAPI = result;
  //     if (result.result) {
  //       if (this.LoginData.staus == "student") {
  //         this.router.navigate(['/StudentDash']);
  //       }
  //       if (this.LoginData.staus == "employee") { this.router.navigate(['/employee']); }
  //     }
  //     else { this.router.navigate(['']); }
  //   })

  // }



  signup(data: { title: string; price: string; author: string; }) {
    console.log(data);
    this.http.post(this.baseURL + "create", data).subscribe(
        (result: any) => {
            console.log(result);
        },
        (error: any) => {
            console.error(error);
        }
    );
}
  data:any
  // ngOnInit() {
  //   getdata();
  // }
getdata(){
  this.http.get(this.baseURL + "get").subscribe((result: any) => {
    console.log(result);
    this.data=result
    this.dataSubject.next(result);

  });
}
  // constructor() { }
}
