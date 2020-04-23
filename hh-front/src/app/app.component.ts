import { Component } from '@angular/core';
import {CompanyService} from './company.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'hh-front';
logged = false;
  username = '';
  password = '';

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  login() {
    this.companyService.login(this.username, this.password).subscribe(res => {
      localStorage.setItem('token', res.token);
      this.logged = true;
      this.username = '';
      this.password = '';
    });
    // this.logged = true;
  }
  logout() {
    localStorage.clear();
    this.logged = false;
  }
}
