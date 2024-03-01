import { Component } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  constructor(private auth: ApiService) {
    
  }
  data:any;
  ngOnInit() {
    this.auth.data$.subscribe((result: any) => {
      this.data = result;
      console.log(this.data)
    });}
}
