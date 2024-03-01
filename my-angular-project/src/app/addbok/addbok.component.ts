import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-addbok',
  templateUrl: './addbok.component.html',
  styleUrls: ['./addbok.component.css']
})
export class AddbokComponent {
  constructor(private auth: ApiService) {
    
   }
  
  reg(t:HTMLInputElement,p:HTMLInputElement,a:HTMLInputElement){
    let data = {
      "title":t.value,"price":p.value,"author":a.value
    }
    let res = this.auth.signup(data);
  }
}
