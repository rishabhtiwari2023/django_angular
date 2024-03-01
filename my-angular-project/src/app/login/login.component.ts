import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  hide = true;
  // emailFormControl = new FormControl('', [Validators.required, Validators.email]);

  // matcher = new ErrorStateMatcher();
  err: any; type: any;
  constructor(private auth: ApiService) { }
  onChange(e: any) { this.type = e.target.value; }
  login(email: any, pass: any) {
    // if (email.value.trim().length === 0 || pass.value.trim().length === 0) {
    //   this.err = "fill these fields to Login"
    // }
    // else {
    this.err = "";
    let data = { "email": email.value, "password": pass.value};
    let res = this.auth.Login2(data);

    // }
  }
}
