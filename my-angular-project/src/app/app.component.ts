import { Component } from '@angular/core';
import { ApiService } from './api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-angular-project';
  constructor(private router: Router) { }
  redirectToPage(): void {
    // Navigate to the desired route or URL
    this.router.navigate(['/add']); // Example route path
  }
  
}
